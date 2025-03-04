from typing import Iterator

from astroid.nodes import NodeNG

from pygolf.rules import *

from .phase import Phase


class AlwaysApplyPhase(Phase):
    def generate_rules(self, ast: NodeNG) -> Iterator[AstroidRule]:
        yield FormatToFString()
        yield RangeForToComprehensionFor()
        yield ComprehensionForAssignToMapAssign()
        yield ListAppend()
