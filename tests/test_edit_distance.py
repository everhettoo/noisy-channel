from unittest import TestCase

import spell
from edit_distance import EditDistance


class TestEditDistance(TestCase):
    def test_spell_edits(self):
        w = 'acommodation'

        candidates = spell.correction(w)
        print(candidates)
        print(len(candidates))

    def test_edits(self):
        w = 'poliec'

        ed = EditDistance()
        candidates = ed.edits(w).items()
        # candidates = ed.edits(w)
        print(len(candidates))

        c, edit = max(candidates, key=lambda p: (lambda c, e: (ed.pedit(e) * ed.pd_lang_model(c)))(*p))
        print(edit)

    def test_correction(self):
        w = 'poliec'

        ed = EditDistance()
        # candidates = ed.edits(w)
        candidates = ed.correct(w)
        print(f'final word : {candidates}')