#!/usr/bin/env python
# -*- coding: utf-8 -*-

# anki-space-behaviour
# Copyright (C) @viql

from aqt.reviewer import Reviewer
from aqt import mw

config = mw.addonManager.getConfig(__name__)

def newOnEnterKey(self):
    if self.state == "question":
        self._getTypedAnswer()
    if self.state == "answer" and config.get("mode") == "show_answer":
        self._getTypedAnswer()

Reviewer.onEnterKey = newOnEnterKey