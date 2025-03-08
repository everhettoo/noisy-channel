import re, string, random, glob, operator, heapq
from collections import defaultdict
from functools import reduce
from math import log10

from functools import reduce


################################
# Utility/Independent functions.
################################
def product(nums):
    """Return the product of a sequence of numbers."""
    return reduce(operator.mul, nums, 1)


def datafile(name, sep='\t'):
    """Read key,value pairs from file."""
    file = open(name)
    for line in file:
        yield line.split(sep)


class Pdist(dict):
    """A probability distribution estimated from counts in datafile."""

    def __init__(self, data=[], N=None, missingfn=None):
        # Load all KPV from datafile.
        try:
            for key, count in data:
                # k1 = self.get(key)
                self[key] = self.get(key, 0) + int(count)
        except Exception as e:
            print(e)

        # The following line ported for python3.
        # self.N = float(N or sum(self.itervalues()))

        # Ever:  N is number of tokens in corpus. If none not defined then sum of all the key's (proba values) assigned.
        # N is the number of tokens in the corpus.
        self.N = float(N or sum(self.values()))

        # Ever (pg. 224): If no f(x) to handle missing word, the default proba is 1/N.
        self.missingfn = missingfn or (lambda k, N: 1. / N)

    def __call__(self, key):
        if key in self:
            return self[key] / self.N
        else:
            return self.missingfn(key, self.N)


################################
# Module functions.
################################
p_spell_error = 1. / 20.

P1edit = Pdist(datafile('../data/count_1edit.tsv'))


def Pedit(edit):
    """The probability of an edit; can be '' or 'a|b' or 'a|b+c|d'."""
    if edit == '':
        return (1. - p_spell_error)

    return p_spell_error * product(P1edit(e) for e in edit.split('+'))


def avoid_long_words(key, N):
    """Estimate the probability of an unknown word."""
    return 10. / (N * 10 ** len(key))


# Ever: Google corpus has a trillion tokens.
N = 1024908267229  ## Number of tokens
Pw = Pdist(datafile('../data/count_1w.tsv'), N, avoid_long_words)


def corrections(text):
    """Spell-correct all words in text."""
    return re.sub('[a-zA-Z]+', lambda m: correct(m.group(0)), text)


def correct(w):
    """Return the word that is the most likely spell correction of w."""
    candidates = edits(w).items()

    # c, edit = max(candidates, key=(lambda c, e: Pedit(e) * Pw(c)))
    c, edit = max(candidates, key=lambda p: (lambda c, e: (Pedit(e) * Pw(c)))(*p))
    return c


def edits(word, d=2):
    "Return a dict of {correct: edit} pairs within d edits of word."
    results = {}

    def editsR(hd, tl, d, edits):
        def ed(L, R):
            return edits + [R + '|' + L]

        C = hd + tl
        if C in Pw:
            e = '+'.join(edits)
            if C not in results:
                results[C] = e
            else:
                results[C] = max(results[C], e, key=Pedit)
        if d <= 0: return
        extensions = [hd + c for c in alphabet if hd + c in PREFIXES]
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
        if len(tl) >= 2 and tl[0] != tl[1] and hd + tl[1] in PREFIXES:
            editsR(hd + tl[1], tl[0] + tl[2:], d - 1,
                   ed(tl[1] + tl[0], tl[0:2]))
            ## Body of edits:

    editsR('', word, d, [])
    return results


alphabet = 'abcdefghijklmnopqrstuvwxyz'

PREFIXES = set(w[:i] for w in Pw for i in range(len(w) + 1))
