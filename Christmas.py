# -*- coding: utf-8-*-
import re
import datetime

WORDS = ["HOW" "LONG" "DAYS" "UNTIL" "CHRISTMAS" "SANTA" "WHEN" "IS" "MANY" "PRESENTS"];

def handle(text, mic, profile):
    d1 = datetime.datetime.today()
    d2 = datetime.datetime(2016,12,25)
    difference = (d2-d1).days
    mic.say("It's " + str(difference) + " days until christmas");


def isValid(text):
    return bool(re.search(r'\b((days|how long)(until|til)|when is)|(christmas|santa)\b', text, re.IGNORECASE))
