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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, re_order

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
        s = "1000 5000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1000)
        self.assertEqual(j, 5000)

    def test_read_3(self):
        s = "15 27\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  15)
        self.assertEqual(j, 27)

    # ----
    # cycle_length
    # ----

    def test_cycle_1(self):
        c = cycle_length(10)
        self.assertEqual(c, 7)

    def test_cycle_2(self):
        c = cycle_length(184)
        self.assertEqual(c, 19)

    def test_cycle_3(self):
        c = cycle_length(5478)
        self.assertEqual(c, 42)

    # ----
    # re_order
    # ----

    def test_order_1(self):
        i, j = re_order(10, 1)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_order_2(self):
        i, j = re_order(5, 15)
        self.assertEqual(i, 5)
        self.assertEqual(j, 15)

    def test_order_3(self):
        i, j = re_order(1000, 30)
        self.assertEqual(i, 30)
        self.assertEqual(j, 1000)

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
        collatz_print(w, 18, 30, 25)
        self.assertEqual(w.getvalue(), "18 30 25\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 2, 3)
        self.assertEqual(w.getvalue(), "1 2 3\n")

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
        r = StringIO("5 7\n18 109\n50 200\n1000 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 7 17\n18 109 119\n50 200 125\n1000 10000 262\n")

    def test_solve_3(self):
        r = StringIO("1 100\n5000 5500\n10000 20000\n1 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 100 119\n5000 5500 192\n10000 20000 279\n1 1000 179\n")

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
