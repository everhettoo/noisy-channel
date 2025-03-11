from unittest import TestCase
from src import channel_v1
from src.proba_distributor import ProbaDistributor


class PDistWord2TestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # 588,124,220,187 (vocab-size)
        cls.denominator = 225955251755.0

        # Defining the probability P(w) for a 2 words in corpus based on its occurrence.
        cls.p = ProbaDistributor(channel_v1.datafile('../data/count_2w.tsv'))
        print(f'[Setup]Total words in corpus: {cls.p.denominator:,}.\r\n')

    def test_double_word1(self):
        # P(3rd floor) = 272,543 / 225,955,251,755 = 1.20618 x 10^-06
        w = '3rd floor'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_double_word2(self):
        # P(2nd year) = 275,672 / 225,955,251,755 = 1.22002 x 10^-06
        w = '2nd year'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_relative_proba(self):
        a = '3rd floor'
        b = '2nd year'
        condition = self.p(a) < self.p(b)
        print(f'P({a}) < P{b}: {condition}.\r\n')
        self.assertTrue(condition)

    def test_unknown1(self):
        # P(dooohhh good) =  1 / 225,955,251,755 = 4.42565 x 10^-12
        w = 'dooohhh good'
        proba = self.p(w)
        print(f'P({w}) = 1 / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_unknown2(self):
        # P(korenge) =  1 / 225,955,251,755 = 4.42565 x 10^-12
        w = 'korenge'
        proba = self.p(w)
        print(f'P({w}) = 1 / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_relative_proba_for_unknown(self):
        a = 'dooohhh good'
        b = 'korenge'
        condition = self.p(a) == self.p(b)
        print(f'P({a}) = P{b}: {condition}.\r\n')
        self.assertTrue(condition)
