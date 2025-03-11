from unittest import TestCase

from channel_v1 import ChannelV1


class TestChannelV1(TestCase):
    def test_edits(self):
        w = 'poliec'

        ed = ChannelV1()
        # candidates = ed.edits(w).items()
        candidates = ed.edits(w)
        print(len(candidates))

    def test_correction(self):
        w = 'oraneg'

        ed = ChannelV1()
        # candidates = ed.edits(w)
        candidates = ed.correct(w)
        print(f'final word : {candidates}')
