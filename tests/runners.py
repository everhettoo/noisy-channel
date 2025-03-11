from unittest import TestSuite, TextTestRunner

from tests.test_proba_dist_1word import PDistWord1TestCase
from tests.test_proba_dist_2word import PDistWord2TestCase
from test_pedit import TestPEdit


def test_suite_pdist_word1():
    suite = TestSuite()
    suite.addTest(PDistWord1TestCase('test_orange'))
    suite.addTest(PDistWord1TestCase('test_apple'))
    suite.addTest(PDistWord1TestCase('test_relative_proba'))
    suite.addTest(PDistWord1TestCase('test_unknown1'))
    suite.addTest(PDistWord1TestCase('test_unknown2'))
    suite.addTest(PDistWord1TestCase('test_relative_proba_for_unknown'))
    return suite


def test_suite_pdist_word2():
    suite = TestSuite()
    suite.addTest(PDistWord2TestCase('test_double_word1'))
    suite.addTest(PDistWord2TestCase('test_double_word2'))
    suite.addTest(PDistWord2TestCase('test_relative_proba'))
    suite.addTest(PDistWord2TestCase('test_unknown1'))
    suite.addTest(PDistWord2TestCase('test_unknown2'))
    suite.addTest(PDistWord2TestCase('test_relative_proba_for_unknown'))
    return suite

def test_pedit():
    suite = TestSuite()
    suite.addTest(TestPEdit('test_product'))
    suite.addTest(TestPEdit('test_pedit_unknown'))
    suite.addTest(TestPEdit('test_pedit_edit1'))
    return suite


if __name__ == '__main__':
    runner = TextTestRunner()
    print('Running test for word 1 ...\r\n')
    runner.run(test_suite_pdist_word1())

    print('\r\nRunning test for word 2 ...\r\n')
    runner.run(test_suite_pdist_word2())

    print('\r\nRunning test for pedit ...\r\n')
    runner.run(test_pedit())
