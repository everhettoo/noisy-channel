from unittest import TestCase
from proba_distributor import ProbaDistributor
import utility as util


class Test(TestCase):
    def setUp(self):
        # 588,124,220,187 (vocab-size)
        self.denominator = 225955251755.0

        # Defining the probability P(w) for a word in corpus based on its occurrence.
        self.p = ProbaDistributor(util.datafile('../data/count_2w.tsv'))
        print(f'Total words in corpus\t:{self.p.denominator:,}.\r\n')

        self.assertEqual(self.denominator, self.p.denominator)

    def test_double_word1(self):
        # count(3rd floor) = 272,543
        w = '3rd floor'

        w_cnt = self.p[w]
        print(f'Total count({w})\t\t:{w_cnt:,}.')

        # P(3rd floor) =  	272,543 / 225,955,251,755 = 1.20618 x 10^-06
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_double_word2(self):
        # count(2nd year) = 275,672
        w = '2nd year'

        w_cnt = self.p[w]
        print(f'Total count({w})\t\t:{w_cnt:,}.')

        # P(2nd year) =  275,672 / 225,955,251,755 = 1.22002 x 10^-06
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_relative_proba(self):
        # count(3rd floor) = 272,543
        a = '3rd floor'
        # count(2nd year) = 275,672
        b = '2nd year'

        condition = self.p(a) < self.p(b)
        print(f'{self.p(a)} < {self.p(b)}: {condition}.')
        self.assertTrue(condition)

    def test_pw_unknown1(self):
        w = 'dooohhh good'

        # P(dooohhh good) =  1 / 225,955,251,755 = 4.42565 x 10^-12
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_pw_unknown2(self):
        w = 'korenge'

        # P(korenge) =  1 / 225,955,251,755 = 4.42565 x 10^-12
        proba = self.p(w)
        print(f'P({w})\t\t\t\t:{proba:,}.')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_relative_proba_for_unknown(self):
        a = 'dooohhh good'
        b = 'korenge'

        # 4.42565 x 10^-12 = 4.42565 x 10^-12
        condition = self.p(a) == self.p(b)
        print(f'{self.p(a)} = {self.p(b)}: {condition}.')
        self.assertTrue(condition)
