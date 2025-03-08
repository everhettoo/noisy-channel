from unittest import TestCase
import utility as util
from proba_distributor import ProbaDistributor


class Test(TestCase):
    def setUp(self):
        # 1 edit vocab size
        self.denominator = 39073

        # Peter Norvig assumes that spelling error occurs every 20 words (pg. 235).
        self.spell_error = 1. / 20.

        # Defining the probability P(w) for a word in corpus based on its occurrence.
        self.p = ProbaDistributor(util.datafile('../data/count_1edit.tsv'))
        print(f'Total words in corpus\t:{self.p.denominator:,}.\r\n')

        self.assertEqual(self.denominator, self.p.denominator)

    def test_product(self):
        prod = util.product([1, 2, 3])
        self.assertEqual(1 * 2 * 3, prod)

    def test_pedit_unknown(self):
        # An unknown word.
        w = 'oraneg'

        # P(oraneg) = 1 / 39073 = 2.55931 x 10^-05
        p_w = self.p(w)

        # Manual calculation
        manual_prod = self.spell_error * p_w
        print(f'Manual product is {manual_prod:.8f}')

        calculated_prod = util.pedit(w, self.p, self.spell_error)
        print(f'Manual product is {calculated_prod:.8f}')

        condition = manual_prod == calculated_prod
        self.assertTrue(condition)

    def test_pedit_relative(self):
        # An unknown word.
        a = 'oraneg'
        b = 'orange'

        # 1 / 39073 = 2.55931 x 10^-05 = 1 / 39073 = 2.55931 x 10^-05
        condition = self.p(a) == self.p(b)
        self.assertTrue(condition)
