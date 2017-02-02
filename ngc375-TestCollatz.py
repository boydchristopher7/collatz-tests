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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cache

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "50 60\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 50)
        self.assertEqual(j, 60)

    def test_read_3(self):
        s = "978 145676\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 978)
        self.assertEqual(j, 145676)

    def test_read_4(self):
        s = "505126 136299\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 136299)
        self.assertEqual(j, 505126)

    #-----
    #cache
    #-----

    def test_cache_1(self):
        tmp_length, tmp_small, tmp_large = collatz_cache(1,10)
        self.assertEqual(tmp_length, 1)
        self.assertEqual(tmp_small, 1000000)
        self.assertEqual(tmp_large, 0)

    def test_cache_2(self):
        tmp_length, tmp_small, tmp_large = collatz_cache(500000,500000)
        self.assertEqual(tmp_length, 1)
        self.assertEqual(tmp_small, 1000000)
        self.assertEqual(tmp_large, 0)

    def test_cache_3(self):
        tmp_length, tmp_small, tmp_large = collatz_cache(1,1000000)
        self.assertEqual(tmp_length, 525)
        self.assertEqual(tmp_small, 1)
        self.assertEqual(tmp_large, 1000000)

    def test_cache_4(self):
        tmp_length, tmp_small, tmp_large = collatz_cache(225000,725000)
        self.assertEqual(tmp_length, 509)
        self.assertEqual(tmp_small, 230001)
        self.assertEqual(tmp_large, 720000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 676, 775, 171)
        self.assertEqual(w.getvalue(), "676 775 171\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 100, 100000, 351)
        self.assertEqual(w.getvalue(), "100 100000 351\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 537200, 1000000, 525)
        self.assertEqual(w.getvalue(), "537200 1000000 525\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

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
