# Dear Santa,

<img src="https://hugovk.github.io/NaNoGenMo-2016/03-dearsanta/dearsanta.jpg" alt="Santa Claus readings letters: Christmas, Florida" width="400">

*A contemporary epistolary novel generated from the crowd*

Things people on Twitter want.

A joint entry for [NaNoGemMo](https://github.com/NaNoGenMo/2016) ("write code that writes a novel") and [PROCJAM](https://hugovk.itch.io/dear-santa) ("make things that make things").

## Generated output

* [6th November 2016](2016-11-06.txt) (51,181 words)
* [9th November 2016, during a US presidential election victory speech](2016-11-09a-victoryspeech.txt) (19,358 words)
* [9th November 2016, on US presidential election results day](2016-11-09b-resultsday.txt) (51,177 words)
* [24th November 2016, Thanksgiving](2016-11-24-thanksgiving.txt) (51,166 words)
* [25th November 2016, Black Friday](2016-11-25-blackfriday.txt) (51,150 words)


## What it does

1. From Twitter, find tweets containing "I want".
2. Ignore those with @ or # or RT.
3. Ignore those "all i want", "alls i want", "everything i want", "that i want" or "what i want".
4. Chop from the "I want" onwards.
5. Repeat until over 50,000 words.

## How to do it

For example, run like `./doit.sh > yyyy-mm-dd.txt` where doit.sh is:

```bash
date "+%x %H:%M:%S"

python stream_dear_santa.py \
     -t "TODO" \
    -ts "TODO" \
    -ck "TODO" \
    -cs "TODO"

date "+%x %H:%M:%S"
```

dateconvert.py converts "29/11/2016 21:29:24" into:

> 29 November 2016, 11:29 PST<br>
29 November 2016, 14:29 EST<br>
29 November 2016, 19:29 GMT<br>
29 November 2016, 19:29 UTC<br>
29 November 2016, 21:29 EET<br>
30 November 2016, 00:59 IST<br>
30 November 2016, 03:29 CST<br>
30 November 2016, 04:29 JST<br>
30 November 2016, 06:29 AEDT
