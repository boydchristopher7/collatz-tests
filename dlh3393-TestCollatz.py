#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, use_cache, regular_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_reg_1(self):
        v = regular_solve(1, 10)
        self.assertEqual(v, 20)

    def test_reg_2(self):
        v = regular_solve(100, 200)
        self.assertEqual(v, 125)

    def test_reg_3(self):
        v = regular_solve(201, 210)
        self.assertEqual(v, 89)

    def test_eval_1(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
    #flip test
    def test_eval_2(self):
        v = collatz_eval(100000, 10000)
        self.assertEqual(v, 351)
    #corner case
    def test_eval_3(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_4(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_5(self):
        v = collatz_eval(89, 90)
        self.assertEqual(v, 31)
    def test_cache_1(self):
        v = use_cache(1000, 2001)
        self.assertEqual(v, 182)
    def test_cache_2(self):
        v = use_cache(1000, 999999)
        self.assertEqual(v, 525)
    def test_cache_3(self):
        v = use_cache(2000, 3001)
        self.assertEqual(v, 217)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n100000 10000\n1 1\n10 10\n89 90\n1000 2001\n1000 999999\n2000 3001\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n100000 10000 351\n1 1 1\n10 10 7\n89 90 31\n1000 2001 182\n1000 999999 525\n2000 3001 217\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
