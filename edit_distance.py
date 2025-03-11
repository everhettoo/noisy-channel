import operator
from functools import reduce

from proba_distributor import ProbaDistributor


def datafile(name, sep='\t'):
    """Reads key,value pairs from file."""
    with open(name, 'r') as file:
        # file = open(name)
        for line in file:
            yield line.split(sep)


def product(nums):
    """Returns the product of a sequence of numbers."""
    return reduce(operator.mul, nums, 1)


class EditDistance:
    def __init__(self):
        self.pd_lang_model = ProbaDistributor(datafile('../data/count_1w.tsv'))
        self.pd_error_model = ProbaDistributor(datafile('../data/count_1edit.tsv'))
        self.spell_error = 1. / 20.
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # Obtaining prefixes from lang model.
        self.PREFIXES = set(w[:i] for w in self.pd_lang_model for i in range(len(w) + 1))

        self.trace = {}

    def pedit(self, edit, p: ProbaDistributor = None):
        # TODO: According pg 234, this is the noisy model P(w|c). Need to verify.
        """The probability of an edit; can be '' or 'a|b' or 'a|b+c|d'."""
        if edit == '':
            return 1. - self.spell_error

        if p:
            return self.spell_error * product(p(e) for e in edit.split('+'))
        else:
            return self.spell_error * product(self.pd_error_model(e) for e in edit.split('+'))

    def calculate_proba(self, p):
        """Calculate the probability of P(w|c)P(c)."""

        word = p[0]  # estimated correct c for misspelled w.
        edits = p[1]  # noise edits for estimated word c.

        # Calculates P(w|c)P(c) --> error model x lang model.
        proba = self.pedit(edits) * self.pd_lang_model(word)

        # Adding for tracing.
        self.trace[word] = proba

        return proba

    def correct(self, w):
        """Return the word that is the most likely spell correction of w."""

        candidates = self.edits(w).items()

        # Norvig's original code was disabled because it doesn't work with python 3.0.
        # c, edit = max(candidates, key=(lambda c, e: Pedit(e) * Pw(c)))

        # The original lambda expression was modified to work with python 3.0.
        # c, edit = max(candidates,
        #               key=lambda p: (
        #                   lambda c, e: (
        #                           self.pedit(e) * self.Pw(c)
        #                   )
        #               )(*p))

        # A substitution for Norvig's lambda for tracing.
        c, edit = max(candidates, key=self.calculate_proba)

        # Reads the max-args produced by calculate_proba.
        max_proba = max(self.trace.values())

        # Trace the max-args key from the trace.
        for k, v in self.trace.items():
            if v == max_proba:
                print(f'MAXARGS({k} -> {v})')
            else:
                print(f'{k} -> {v}')

        # for a in candidates: print(f'{a[0]}:{a[1]}')

        return c

    def edits(self, word, d=2):
        """Return a dict of {correct: edit} pairs within d edits of word."""
        results = {}

        def editsR(hd, tl, d, edits):
            def ed(L, R):
                return edits + [R + '|' + L]

            C = hd + tl
            if C in self.pd_lang_model:
                e = '+'.join(edits)
                if C not in results:
                    results[C] = e
                else:
                    results[C] = max(results[C], e, key=self.pedit)
            if d <= 0: return
            extensions = [hd + c for c in self.alphabet if hd + c in self.PREFIXES]
            p = (hd[-1] if hd else '<')  ## previous character
            ## Insertion
            for h in extensions:
                editsR(h, tl, d - 1, ed(p + h[-1], p))
            if not tl: return
            ## Deletion
            editsR(hd, tl[1:], d - 1, ed(p, p + tl[0]))
            for h in extensions:
                if h[-1] == tl[0]:  ## Match
                    editsR(h, tl[1:], d, edits)
                else:  ## Replacement
                    editsR(h, tl[1:], d - 1, ed(h[-1], tl[0]))
                    ## Transpose
            if len(tl) >= 2 and tl[0] != tl[1] and hd + tl[1] in self.PREFIXES:
                editsR(hd + tl[1], tl[0] + tl[2:], d - 1,
                       ed(tl[1] + tl[0], tl[0:2]))
                ## Body of edits:

        editsR('', word, d, [])
        return results
