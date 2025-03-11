from unittest import TestCase
from src.proba_distributor import ProbaDistributor
from src import channel_v1


class TestPEdit(TestCase):
    @classmethod
    def setUpClass(cls):
        # 1 edit vocab size
        cls.denominator = 39073
        # Peter Norvig assumes that spelling error occurs every 20 words (pg. 235).
        cls.spell_error = 1. / 20.

        # Defining the probability P(w) for a 2 words in corpus based on its occurrence.
        cls.p = ProbaDistributor(channel_v1.datafile('../data/count_1edit.tsv'))
        print(f'[Setup]Total words in corpus: {cls.p.denominator:,}.\r\n')

    def test_product(self):
        nums = [1, 2, 3]
        prod = channel_v1.product(nums)
        print(f'Product of {nums} = {prod:,}')
        self.assertEqual(1 * 2 * 3, prod)

    def test_pedit_unknown(self):
        # The word not found in corpus => P(oraneg) = 1 / 39073 = 2.55931 x 10^-05
        w = 'oraneg'
        p_w = self.p(w)

        # Manual calculation to verify the pedit outcome.
        manual_prod = self.spell_error * p_w
        print(f'Manual: {self.spell_error} x {p_w} = {manual_prod:.8f}')

        pedit_prod = channel_v1.pedit(w, self.p, self.spell_error)
        print(f'Pedit : {self.spell_error} x {p_w} = {pedit_prod:.8f}')

        condition = manual_prod == pedit_prod
        print(f'manual = pedit: {condition}.\r\n')
        self.assertTrue(condition)

    def test_pedit_edit1(self):
        # The word found in corpus => 133 / 39,073 x 0.05 (spelling error) = 0.00017019425178512016
        w = 'i|is'
        w_cnt = self.p[w]
        proba = channel_v1.pedit(w, self.p, self.spell_error)
        print(f'P({w}) = {self.p[w]:,} / {self.p.denominator:,} = {proba}.\r\n')
        self.assertEqual(w_cnt / self.p.denominator * self.spell_error, proba)
