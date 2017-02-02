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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_helper

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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    # ----
    # helper
    # ----

    def test_helper_1(self):
        v = collatz_helper(1, 10)
        self.assertEqual(v, 20)

    def test_helper_2(self):
        v = collatz_helper(9500, 16201)
        self.assertEqual(v, 276)

    def test_helper_3(self):
        v = collatz_helper(962, 6358)
        self.assertEqual(v, 262)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(16201, 9500)
        self.assertEqual(v, 276)

    def test_eval_3(self):
        v = collatz_eval(146, 998513)
        self.assertEqual(v, 525)

    def test_eval_4(self):
        v = collatz_eval(145998, 152014)
        self.assertEqual(v, 370)

    def test_eval_5(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 16201, 9500, 276)
        self.assertEqual(w.getvalue(), "16201 9500 276\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 146, 998513, 525)
        self.assertEqual(w.getvalue(), "146 998513 525\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n9500 16201\n146 998513\n145998 152014\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n9500 16201 276\n146 998513 525\n145998 152014 370\n")

    def test_solve2(self):
        r = StringIO("7894 84516\n9855 78\n8493 94516\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "7894 84516 351\n9855 78 262\n8493 94516 351\n")

    def test_solve3(self):
        r = StringIO("4518 945163\n15493 451987\n95 154886\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "4518 945163 525\n15493 451987 449\n95 154886 375\n")

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
