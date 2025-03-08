from unittest import TestCase
import improved_norvig_ngram as nv
import pandas as pd


class Test(TestCase):
    def test_pw(self):
        dist = nv.Pdist(nv.datafile('../data/count_1edit.tsv'))
        proba = dist['apple']
        print(proba)

    def test_misspelled_words(self):
        # df = pd.read_csv('../data/COUNT_1W.TSV', sep='\t')
        # df = pd.read_csv('../data/COUNT_2W.TSV', sep='\t')
        # print(df.shape)
        # w = 'apple'
        # candidates = nv.edits(w).items()
        # # c, edit = max(candidates, key=lambda (c, e): nv.Pedit(e) * nv.Pw(c))
        # c, edit = max(candidates, key=lambda p: (lambda c, e: (nv.Pedit(e) * nv.Pw(c)))(*p))
        # x('apple','babble')
        # print(x)
        # x = lambda a: a + b
        # print(x(3, 2))
        # res = nv.correct('choosespain')
        res = nv.correct('contant')
        print(res)

    def test_product(self):
        product = nv.product({1, 2, 3})
        self.assertEqual(product, 6)

    def test_datafile(self):
        line = nv.datafile('../data/count_1edit.tsv')
        # Yields next line only when called.
        for l in line:
            print(l)

    def test_lambda(self):
        # w = 'apple'
        # candidates = nv.edits(w).items()
        # # c, edit = max(candidates, key=lambda (c, e): nv.Pedit(e) * nv.Pw(c))
        # c, edit = max(candidates, key=lambda p: (lambda c, e: (nv.Pedit(e) * nv.Pw(c)))(*p))
        # x('apple','babble')
        # print(x)
        # x = lambda a: a + b
        # print(x(3, 2))
        res = nv.correct('constent')
        print(res)

    def test_pedit(self):
        proba = nv.Pedit('apple')
        print(proba)
        # print(f'proba for the is \t:{nv.Pedit("appel")}')
        # print(f'proba for book is \t:{nv.Pedit("book")}')

    def test_pw(self):
        # print(f'proba for the is \t:{nv.Pw("thewqw")}')
        print(f'proba for book is \t:{nv.Pw("verylongwordisneededrighttakeit")}')
        # val = nv.Pw('the')
        # print(val)

    def test_avoid_long_words(self):
        # The larger the number, the larger the result with negative exponent.
        # This should be number of tokens in the corpus.
        N = 1
        x = 2

        # ** is the exponentiation operator: 2^5
        total = x ** N
        print(total)

        print(f'print apple: {nv.avoid_long_words("apple", N)}')
        print(f'print orang: {nv.avoid_long_words("orang", N)}')
        print(f'print orange: {nv.avoid_long_words("orange", N)}')
