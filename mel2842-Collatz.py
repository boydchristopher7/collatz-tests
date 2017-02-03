#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# cycle_length
# ------------


def cycle_length(n):
    c = 1
    while n > 1:
        if (n % 2) == 0:
            n = (n // 2)
        else:
            n = (3 * n) + 1
        c += 1
    return c

# ------------
# re_order
# ------------


def re_order(i, j):
    if (j < i):
        temp = j
        j = i
        i = temp
    return (i, j)

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    i, j = re_order(i, j)

    # Each entry in the dictionary is the max cycle length of a range of
    # 20,000. Each key is the first number of that range.
    cache = {1: 279, 20001: 324, 40001: 340, 60001: 351, 80001: 333, 100001: 354, 120001: 344, 140001: 383, 160001: 370, 180001: 365, 200001: 386, 220001: 443, 240001: 368, 260001: 407, 280001: 389, 300001: 384, 320001: 384, 340001: 441, 360001: 423, 380001: 436, 400001: 449, 420001: 418, 440001: 387, 460001: 444, 480001:
             426, 500001: 470, 520001: 408, 540001: 452, 560001: 421, 580001: 434, 600001: 447, 620001: 509, 640001: 429, 660001: 442, 680001: 442, 700001: 504, 720001: 424, 740001: 424, 760001: 468, 780001: 468, 800001: 450, 820001: 525, 840001: 419, 860001: 432, 880001: 445, 900001: 476, 920001: 507, 940001: 414, 960001: 458}
    keys = list(cache.keys())
    max_length = 0
    idx = i

    while (idx <= j):

        if ((idx in keys) and (idx + 19999 <= j)):
            length = cache[idx]
            idx += 19999
        else:
            length = cycle_length(idx)
            idx += 1

        if (length > max_length):
            max_length = length

    return (max_length)

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
