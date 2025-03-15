from unittest import TestCase
from proba_distributor import ProbaDistributor
import channel_v1


class PDistWord1TestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # 588,124,220,187 (vocab-size)
        cls.denominator = 588124220187

        # Defining the probability P(w) for a 1 words in corpus based on its occurrence.
        cls.p = ProbaDistributor(channel_v1.datafile('../data/count_1w.tsv'))
        print(f'[Setup]Total words in corpus: {cls.p.denominator:,}.\r\n')

    def test_orange(self):
        # P(orange) =  37,316,122 / 588,124,220,187.0 = 6.34494 x 10^-05
        w = 'orange'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_apple(self):
        # P(apple) =  50,551,171 / 588,124,220,187.0 = 8.59532 x 10^-05
        w = 'apple'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_relative_proba(self):
        a = 'apple'
        b = 'orange'
        condition = self.p(a) > self.p(b)
        print(f'P({a}) > P{b}: {condition}.\r\n')
        self.assertTrue(condition)

    def test_unknown1(self):
        # P(dooohhh) =  1 / 588,124,220,187.0 = 1.70032 x 10^-12.
        w = 'dooohhh'
        proba = self.p(w)
        print(f'P({w}) = 1 / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_unknown2(self):
        # P(korenge) =  1 / 588,124,220,187.0 = 1.70032 x 10^-12.
        w = 'korenge'
        proba = self.p(w)
        print(f'P({w}) = 1 / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_relative_proba_for_unknown(self):
        a = 'dooohhh'
        b = 'korenge'
        condition = self.p(a) == self.p(b)
        print(f'P({a}) = P{b}: {condition}.\r\n')
        self.assertTrue(condition)
