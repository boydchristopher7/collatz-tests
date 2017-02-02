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
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):

    def test_get_cycle_length(self):
        n = 1
        cache = {}
        solution = get_cycle_length(n, cache)
        self.assertEqual(solution,  1)

    def test_get_cycle_length2(self):
        n = 2
        cache = {}
        solution = get_cycle_length(n, cache)
        self.assertEqual(solution, 2)

    def test_get_cycle_length3(self):
        n = 4
        cache = {}
        solution = get_cycle_length(n, cache)
        self.assertEqual(solution, 3)

    def test_get_cycle_length4(self):
        n = 4
        cache = {2: 2}
        solution = get_cycle_length(n, cache)
        self.assertEqual(solution, 3)

    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "15    1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  15)
        self.assertEqual(j, 1000000)

    def test_read3(self):
        s = "  5    10  \n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5)
        self.assertEqual(j, 10)


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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(2, 1)
        self.assertEqual(v, 2)

    def test_eval_6(self):
        v = collatz_eval(908238, 159304)
        self.assertEqual(v, 525)

    def test_eval_7(self):
        v = collatz_eval(807248, 59461)
        self.assertEqual(v, 509)


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")


    def test_print2(self):
        w = StringIO()
        collatz_print(w, 1, 155, 20)
        self.assertEqual(w.getvalue(), "1 155 20\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO("1    1\n1    1")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n1 1 1\n")

    def test_solve3(self):
        r = StringIO("900    1000     \t   \n\n\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n")

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
