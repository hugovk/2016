#!/usr/bin/env python
# encoding: utf-8
"""
A boring diary. Or is it a rubbish reference book? Just clock times:
"The time is twelve am. Twelve oh one am. Twelve oh two pm... And thirty
seconds."
"""

import inflect
from random import randint


def upperfirst(x):
    return x[0].upper() + x[1:]


p = inflect.engine()

out = []
chapter = 0


for hour in range(0, 24):
    chapter += 1
    out.append("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChapter {}\n\n".format(chapter))

    for minute in range(0, 60):
        for second in range(0, 60):
            if hour >= 12:
                ampm = "pm"
            else:
                ampm = "am"
            if hour == 0:
                hour = 12
            if hour > 12:
                hour -= 12

            if 0 < minute < 10:
                mins = " oh {}".format(p.number_to_words(minute))
            elif minute > 10:
                mins = " " + p.number_to_words(minute)
            else:
                mins = ""

            if second > 0:
                sec = " and {} {}".format(
                    p.number_to_words(second),
                    p.plural("second", second))
            else:
                sec = ""

            if randint(1, 100) < 50:
                thetimeis = "The time is now"
            else:
                thetimeis = "It's"

            if randint(1, 100) < 33 and second > 0:
                line = upperfirst(sec.lstrip()) + "."
            elif 33 < randint(1, 100) < 67:
                line = "{} {}{} {}{}.".format(
                    thetimeis, p.number_to_words(hour), mins, ampm, sec)
            else:
                line = "{}{} {}{}.".format(
                    p.number_to_words(hour), mins, ampm, sec)
                line = upperfirst(line)

#             print line

            out.append(line)

            if randint(1, 100) < 20:
                out.append("\n\n")


print " ".join(out)
