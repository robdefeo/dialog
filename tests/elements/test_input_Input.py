from dialog.process import GrammarProcessResponse
from dialog.process.action_response import ActionProcessResponse
from dialog.process.grammar_response import GrammarMatchType

__author__ = 'robdefeo'
from unittest import TestCase
from unittest.mock import Mock

from dialog.elements import Folder, Goto, Grammar, Action
from dialog.elements.input import Input as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(
            children=[
                Grammar(items=[Mock()]),
                Action(),
                Goto()
            ]
        )

        folder = Folder(
            children=[actual]
        )
        dialog = Mock()
        folder._set_dialog(dialog)

        self.assertEqual(
            dialog,
            actual.children[0].dialog
        )
        self.assertEqual(
            dialog,
            actual.children[1].dialog
        )
        self.assertEqual(
            dialog,
            actual.children[2].dialog
        )


class process_Tests(TestCase):
    maxDiff = None

    def test_grammar_no_match(self):
        grammar = Mock(spec=Grammar)
        grammar.process = Mock(return_value=GrammarProcessResponse(GrammarMatchType.none))
        target = Target(
            children=[
                grammar,
                Action(),
                Goto()
            ]
        )
        actual = target.process(None)
        self.assertEqual(
            None,
            actual
        )

    def test_grammar_exact_match(self):
        grammar = Mock(spec=Grammar)
        grammar.process = Mock(return_value=GrammarProcessResponse(GrammarMatchType.exact))
        action = Mock(spec=Action)
        action.process = Mock(return_value=ActionProcessResponse("test_name", "test_value"))
        target = Target(
            children=[
                grammar,
                action,
                Goto()
            ]
        )
        actual = target.process(None)
        self.assertEqual(
            None,
            actual
        )
