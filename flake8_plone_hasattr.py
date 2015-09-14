# -*- coding: utf-8 -*-
import re


HASATTR_RE = re.compile(r'(^|.*\s)(?P<h>hasattr)\(.+\).*')


class PloneHasattrChecker(object):
    name = 'flake8_plone_hasattr'
    version = '0.1'
    message = 'P002 found "hasattr", consider replacing it'

    def __init__(self, tree, filename):
        self.filename = filename

    def run(self):
        with open(self.filename) as f:
            lines = f.readlines()

            for lineno, line in enumerate(lines, start=1):
                found = HASATTR_RE.search(line)
                if found:
                    yield lineno, line.find('hasattr'), self.message, type(self)
