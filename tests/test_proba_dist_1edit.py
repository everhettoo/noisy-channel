from unittest import TestCase
from proba_distributor import ProbaDistributor
import channel_v1


class PDist1EditTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # 39,073 (vocab-size)
        cls.denominator = 39073

        # Defining the probability P(w) for a 1 edit words in corpus based on its occurrence.
        cls.p = ProbaDistributor(channel_v1.datafile('../data/count_1edit.tsv'))
        print(f'[Setup]Total words in corpus: {cls.p.denominator:,}.\r\n')

    def test_orange(self):
        # P(ec|ce) =  27 / 39,073 = 0.000691014255368157
        w = 'ec|ce'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_apple(self):
        # P(pa|p) =  23 / 39,073 = 0.000691014255368157
        w = 'pa|p'
        w_cnt = self.p[w]
        proba = self.p(w)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator, proba)

    def test_relative_proba(self):
        a = 'ec|ce'
        b = 'pa|p'
        condition = self.p(a) > self.p(b)
        print(f'P({a}) > P{b}: {condition}.\r\n')
        self.assertTrue(condition)

    def test_unknown1(self):
        # P(dooohhh) =  1 / 39,073 = 0.000025593120569191
        w = 'dooohhh'
        proba = self.p(w)
        print(f'P({w}) = 1 / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(1 / self.p.denominator, proba)

    def test_unknown2(self):
        # P(korenge) =  1 / 39,073 = 0.000025593120569191
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
