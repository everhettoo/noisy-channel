from unittest import TestCase
from proba_distributor import ProbaDistributor
import utility as util


class Test(TestCase):
    def setUp(self):
        # 588,124,220,187 (vocab-size)
        self.denominator = 588124220187

        # Defining the probability P(w) for a word in corpus based on its occurrence.
        self.p = ProbaDistributor(util.datafile('../data/count_1w.tsv'))
        print(f'Total words in corpus\t:{self.p.denominator:,}.\r\n')

        self.assertEqual(self.denominator, self.p.denominator)

    def test_orange(self):
        # count(orange) = 37,316,112
        w = 'orange'

        w_cnt = self.p[w]
        print(f'Total count({w})\t\t:{w_cnt:,}.')

        # P(orange) =  37,316,122 / 588,124,220,187.0 = 6.34494 x 10^-05
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_apple(self):
        # count(apple) = 50,551,171
        w = 'apple'

        w_cnt = self.p[w]
        print(f'Total count({w})\t\t:{w_cnt:,}.')

        # P(apple) =  50,551,171 / 588,124,220,187.0 = 8.59532 x 10^-05
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_relative_proba(self):
        # count(orange) = 37,316,112
        a = 'apple'
        # count(apple) = 50,551,171
        b = 'orange'

        condition = self.p(a) > self.p(b)
        print(f'{self.p(a)} > {self.p(b)}: {condition}.')
        self.assertTrue(condition)

    def test_pw_unknown1(self):
        w = 'dooohhh'

        # P(dooohhh) =  1 / 588,124,220,187.0 = 1.70032 x 10^-12.
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_pw_unknown2(self):
        w = 'korenge'

        # P(korenge) =  1 / 588,124,220,187.0 = 1.70032 x 10^-12.
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_relative_proba_for_unknown(self):
        a = 'dooohhh'
        b = 'korenge'

        # 1.70032 x 10^-12 = 1.70032 x 10^-12
        condition = self.p(a) == self.p(b)
        print(f'{self.p(a)} = {self.p(b)}: {condition}.')
        self.assertTrue(condition)
