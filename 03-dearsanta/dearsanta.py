#!/usr/bin/env python3
"""
Dear Santa, I have been good this year and want:
1. [from Twitter, I want [thing]],
2. repeat to 50k.
Maybe ignore tweets with @ or links or #.

A joint entry for NaNoGemMo ("write code that writes a novel")
and PROCJAM ("make things that make things").

https://github.com/hugovk/NaNogenMo/2016
https://github.com/NaNoGenMo/2016/issues/20
https://hugovk.itch.io/dear-santa
http://www.procjam.com

Notes:
https://github.com/sixohsix/twitter/blob/master/twitter/stream_example.py
https://dev.twitter.com/streaming/reference/post/statuses/filter
"""

import argparse
import datetime as dt
import html

import pytz
from twitter.oauth import OAuth
from twitter.stream import TwitterStream  # , Timeout, HeartbeatTimeout, Hangup
from twitter.util import printNicely


def timestamps():
    utc_now = dt.datetime.utcnow()

    us_pacific = pytz.timezone("US/Pacific")
    us_eastern = pytz.timezone("US/Eastern")
    london = pytz.timezone("Europe/London")
    helsinki = pytz.timezone("Europe/Helsinki")
    india = pytz.timezone("Asia/Calcutta")
    china = pytz.timezone("Asia/Shanghai")
    japan = pytz.timezone("Asia/Tokyo")
    sydney = pytz.timezone("Australia/Sydney")

    for tz in [
        us_pacific,
        us_eastern,
        london,
        pytz.UTC,
        helsinki,
        india,
        china,
        japan,
        sydney,
    ]:
        timezone_name = tz.localize(utc_now).tzname()
        local_date = (
            pytz.utc.localize(utc_now).astimezone(tz).strftime("%d %B %Y, %H:%M")
        )
        printNicely(f"{local_date} {timezone_name}")
    printNicely("")


def intro():
    printNicely("Dear Santa,")
    printNicely("")
    printNicely("This year I have been good.")
    printNicely("")


def outro(one_more):
    printNicely("")
    printNicely(
        "Thank you Santa, I hope you can fit all these things in your "
        "sleigh and down the chimney."
    )
    printNicely("")
    printNicely("I hope the reindeer are well.")
    printNicely("")
    printNicely("Love,")
    printNicely("")
    printNicely("Twitter")
    printNicely("")
    printNicely(f"P.S. I almost forgot: {one_more}")
    printNicely("")


def split_from(target, text):
    """Split text from the target to the end"""
    pos = text.lower().find(target.lower())
    if pos > 0:
        return text[pos:]
    else:
        return None


def process_tweet(text, target):
    """Check it's ok, remove some stuff, and print"""
    if text.startswith("RT ") or "@" in text or "#" in text or "http" in text:
        return None
    text_lower = text.lower()

    exclude = [
        "all i want",
        "alls i want",
        "everything i want",
        "that i want",
        "what i want",
    ]
    if any(substr in text_lower for substr in exclude):
        return None
    return split_from(target, text)


def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__ or "")
    parser.add_argument(
        "-t",
        "--token",
        required=True,
        help="The Twitter Access Token.",
    )
    parser.add_argument(
        "-ts",
        "--token-secret",
        required=True,
        help="The Twitter Access Token Secret.",
    )
    parser.add_argument(
        "-ck",
        "--consumer-key",
        required=True,
        help="The Twitter Consumer Key.",
    )
    parser.add_argument(
        "-cs",
        "--consumer-secret",
        required=True,
        help="The Twitter Consumer Secret.",
    )
    parser.add_argument(
        "-us",
        "--user-stream",
        action="store_true",
        help="Connect to the user stream endpoint.",
    )
    parser.add_argument(
        "-ss",
        "--site-stream",
        action="store_true",
        help="Connect to the site stream endpoint.",
    )
    parser.add_argument(
        "-to",
        "--timeout",
        help="Timeout for the stream (seconds).",
    )
    parser.add_argument(
        "-ht",
        "--heartbeat-timeout",
        help="Set heartbeat timeout.",
        default=90,
    )
    parser.add_argument(
        "-nb",
        "--no-block",
        action="store_true",
        help="Set stream to non-blocking.",
    )
    parser.add_argument(
        "-tt",
        "--track-keywords",
        default="i want",
        help="Search the stream for specific text.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    first_one = True
    word_count = 0

    # When using twitter stream you must authorize.
    auth = OAuth(args.token, args.token_secret, args.consumer_key, args.consumer_secret)

    # These arguments are optional:
    stream_args = dict(
        timeout=args.timeout,
        block=not args.no_block,
        heartbeat_timeout=args.heartbeat_timeout,
    )

    query_args = dict()
    if args.track_keywords:
        query_args["track"] = args.track_keywords

    if args.user_stream:
        stream = TwitterStream(
            auth=auth, domain="userstream.twitter.com", **stream_args
        )
        tweet_iter = stream.user(**query_args)
    elif args.site_stream:
        stream = TwitterStream(
            auth=auth, domain="sitestream.twitter.com", **stream_args
        )
        tweet_iter = stream.site(**query_args)
    else:
        stream = TwitterStream(auth=auth, **stream_args)
        if args.track_keywords:
            tweet_iter = stream.statuses.filter(**query_args)
        else:
            tweet_iter = stream.statuses.sample()

    # Iterate over the sample stream.
    for tweet in tweet_iter:
        # You must test that your tweet has text. It might be a delete
        # or data message.
        if tweet is None:
            pass
        #     printNicely("-- None --")
        # elif tweet is Timeout:
        #     printNicely("-- Timeout --")
        # elif tweet is HeartbeatTimeout:
        #     printNicely("-- Heartbeat Timeout --")
        # elif tweet is Hangup:
        #     printNicely("-- Hangup --")
        elif tweet.get("text"):
            processed = process_tweet(tweet["text"], args.track_keywords)
            if processed:
                # &amp; -> & etc.
                processed = html.unescape(processed)
                if first_one:
                    first_one = False
                    keep_one_back = processed
                else:
                    printNicely(processed)
                word_count += len(processed.split())

        if word_count > 51000:
            break

        # else:
        #     printNicely("-- Some data: " + str(tweet))

    return keep_one_back


if __name__ == "__main__":
    timestamps()
    intro()
    one_more = main()
    outro(one_more)

# End of file
