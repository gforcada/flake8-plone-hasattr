# -*- coding: utf-8 -*-
import re


try:
    from flake8.engine import pep8 as stdin_utils
except ImportError:
    from flake8 import utils as stdin_utils


HASATTR_RE = re.compile(r'(^|.*\s)(?P<h>hasattr)\(.+\).*')


class PloneHasattrChecker(object):
    name = 'flake8_plone_hasattr'
    version = '0.2'
    message = 'P002 found "hasattr", consider replacing it'

    def __init__(self, tree, filename):
        self.filename = filename

    def run(self):
        if self.filename == 'stdin':
            lines = stdin_utils.stdin_get_value().splitlines(True)
        else:
            with open(self.filename) as f:
                lines = f.readlines()

        for lineno, line in enumerate(lines, start=1):
            found = HASATTR_RE.search(line)
            if found:
                yield lineno, line.find('hasattr'), self.message, type(self)
