#!/usr/bin/env python
# encoding: utf-8
"""
Take a timestamp like:
25/11/2016 23:05:03

Convert it to:
25 November 2016, 13:05 PST
25 November 2016, 16:05 EST
25 November 2016, 21:05 GMT
25 November 2016, 21:05 UTC
25 November 2016, 23:05 EET
26 November 2016, 02:35 IST
26 November 2016, 05:05 CST
26 November 2016, 06:05 JST
26 November 2016, 08:05 AEDT
"""
from __future__ import print_function, unicode_literals
from dateutil.parser import parse  # pip install python-dateutil
import argparse
import pytz  # pip install pytz


def utc_to_local(utc_dt, local_tz):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)  # .normalize might be unnecessary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a timestamp into eight others.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'timestamp',
        help="Input timestamp")
    args = parser.parse_args()

    # print(args.timestamp)
    indate = parse(args.timestamp, dayfirst=True, yearfirst=False)

    local_tz = pytz.timezone('Europe/Helsinki')
    # print(indate, local_tz)

    localdt = local_tz.localize(indate)

    us_pacific = pytz.timezone('US/Pacific')
    us_eastern = pytz.timezone('US/Eastern')
    london = pytz.timezone('Europe/London')
    india = pytz.timezone('Asia/Calcutta')
    china = pytz.timezone('Asia/Shanghai')
    japan = pytz.timezone('Asia/Tokyo')
    sydney = pytz.timezone('Australia/Sydney')

    for tz in [us_pacific, us_eastern, london, pytz.UTC, local_tz, india,
               china, japan, sydney]:
        timezone_name = tz.localize(indate).tzname()
        local_date = localdt.astimezone(tz).strftime("%d %B %Y, %H:%M")

        print("{} {}".format(local_date, timezone_name))

        # x = tz.localize(indate)
        # print("{} ({})".format(localdt.astimezone(tz), x.tzname()))

        # print()


# End of file
