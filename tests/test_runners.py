from unittest import TestSuite, TextTestRunner

from tests.test_proba_dist_2word import PDistWord2TestCase


def test_suite_pdist_word2():
    suite = TestSuite()
    suite.addTest(PDistWord2TestCase('test_double_word1'))
    suite.addTest(PDistWord2TestCase('test_double_word2'))
    suite.addTest(PDistWord2TestCase('test_relative_proba'))
    suite.addTest(PDistWord2TestCase('test_unknown1'))
    suite.addTest(PDistWord2TestCase('test_unknown2'))
    suite.addTest(PDistWord2TestCase('test_relative_proba_for_unknown'))
    return suite


if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(test_suite_pdist_word2())
