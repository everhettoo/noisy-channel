from unittest import TestCase

from channel_v1 import datafile, ChannelV1

from proba_distributor import ProbaDistributor


def display_trace(trace):
    # Reads the max-args produced by calculate_proba.
    max_proba = max(trace.values())

    # Trace the max-args key from the trace.
    for k, v in trace.items():
        if v == max_proba:
            print(f'-> MAXARGS({k} -> {v})')
        else:
            print(f'{k} -> {v}')


class TestChannelV1(TestCase):
    @classmethod
    def setUpClass(cls):
        # 588,124,220,187 (vocab-size)
        cls.denominator = 588124220187

        # Defining the probability P(w) for a 2 words in corpus based on its occurrence.
        cls.p = ProbaDistributor(datafile('../data/count_1w.tsv'))
        print(f'[Setup]Total words in corpus: {cls.p.denominator:,}.\r\n')

    def test_correction1(self):
        # require 1 edit ec|ce (27)
        w = 'poliec'

        channel = ChannelV1()
        # candidates = ed.edits(w)
        candidates = channel.correct(w)
        print(f'final word : {candidates}')

        display_trace(channel.trace)

    def test_edits(self):
        w = 'poliec'

        ed = ChannelV1()
        # candidates = ed.edits(w).items()
        candidates = ed.edits(w)
        print(len(candidates))

    def test_correction(self):
        w = 'oraneg'

        channel = ChannelV1()
        # candidates = ed.edits(w)
        candidates = channel.correct(w)
        print(f'final word : {candidates}')

        display_trace(channel.trace)
