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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    def test_read_2(self):
        s = "1 1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1000000)

    def test_read_3(self):
        s = "2 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  2)
        self.assertEqual(j, 999999)

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

    def test_eval_5(self):
        v = collatz_eval(53, 64)
        self.assertEqual(v, 113)

    def test_eval_6(self):
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_7(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1000, 25001, 282)
        self.assertEqual(w.getvalue(), "1000 25001 282\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 28, 14387, 282)
        self.assertEqual(w.getvalue(), "28 14387 282\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, -1, -50, 0)
        self.assertEqual(w.getvalue(), "-1 -50 0\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("22 55\n53 64\n3000 5000\n1 1000000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "22 55 113\n53 64 113\n3000 5000 238\n1 1000000 525\n")

    def test_solve_3(self):
        r = StringIO("15 6171\n6171 17647\n950943 970599\n16 500000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "15 6171 262\n6171 17647 279\n950943 970599 458\n16 500000 449\n")


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
