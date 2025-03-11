from unittest import TestCase

from src.channel_v1 import datafile, ChannelV1

from src.proba_distributor import ProbaDistributor


def display_candidate_trace(trace):
    # Reads the max-args produced by calculate_proba.
    max_proba = max(trace.values())

    # Trace the max-args key from the trace.
    for k, v in trace.items():
        if v == max_proba:
            print(f'-> ARGMAX({k} -> {v})')
        else:
            print(f'{k} -> {v}')


def display_edit_trace(trace, candidate):
    # Trace the max-args key from the trace.
    for k, v in trace.items():
        if k == candidate:
            print(f'-> ESTIMATE(W):({k} -> {v})')
        else:
            print(f'{k} -> {v}')


class TestChannelV1(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trace = False

        # Defining the probability P(w) for a 2 words in corpus based on its occurrence.
        cls.p_lang_model = ProbaDistributor(datafile('../data/count_1w.tsv'))
        cls.p_error_model = ProbaDistributor(datafile('../data/count_1edit.tsv'))
        cls.channel = ChannelV1(lang_model=cls.p_lang_model,
                                error_model=cls.p_error_model,
                                spell_error=(1. / 20.),
                                alphabet='abcdefghijklmnopqrstuvwxyz')

        print(f'[Setup]Total words in lang model: {cls.p_lang_model.denominator:,}.')
        print(f'[Setup]Total words in error model: {cls.p_error_model.denominator:,}.\r\n')

    def test_police(self):
        # P(w|c) => P(ec|ce): 27 / 39,073 = 0.000691014255368157
        # P(c) => P(police): 64,198,152 / 588,124,220,187 = 0.000109157470133754
        # TODO: Need manual verification for argmax-c (Pc|w) = argmax-c P(w|c) x P(c).

        # w = 'poliec'
        w = 'poliec'
        expected = 'police'
        c = self.channel.correct(w)
        print(f'Candidate: {c}')

        if self.trace:
            print('\r\nDisplay candidates-trace:')
            display_candidate_trace(self.channel.candidate_trace)
            print('\r\nDisplay candidates-edit-trace:')
            display_edit_trace(self.channel.edit_trace, c)

        self.assertEqual(expected, c)

    def test_orange(self):
        w = 'oraneg'
        expected = 'orange'
        c = self.channel.correct(w)
        print(f'Candidate: {c}')

        if self.trace:
            print('\r\nDisplay candidates-trace:')
            display_candidate_trace(self.channel.candidate_trace)
            print('\r\nDisplay candidates-edit-trace:')
            display_edit_trace(self.channel.edit_trace, c)

        self.assertEqual(expected, c)
