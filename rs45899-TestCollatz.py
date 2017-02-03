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

from Collatz import collatz_read, collatz_cycle_len, collatz_raw_eval, collatz_eval, collatz_print, collatz_solve

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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "4 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 4)
        self.assertEqual(j, 100)

    def test_read_3(self):
        s = "30 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 30)
        self.assertEqual(j, 2)

    def test_read_4(self):
        s = "500000 1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 500000)
        self.assertEqual(j, 1000000)

    # ---------
    # cycle_len
    # ---------

    def test_cycle_len_1(self):
        c = collatz_cycle_len(1)
        self.assertEqual(c, 1)

    def test_cycle_len_2(self):
        c = collatz_cycle_len(4)
        self.assertEqual(c, 3)

    def test_cycle_len_3(self):
        c = collatz_cycle_len(30)
        self.assertEqual(c, 19)

    def test_cycle_len_4(self):
        c = collatz_cycle_len(500000)
        self.assertEqual(c, 152)

    # --------
    # raw_eval
    # --------

    def test_raw_eval_1(self):
        v = collatz_raw_eval(1, 10)
        self.assertEqual(v, 20)

    def test_raw_eval_2(self):
        v = collatz_raw_eval(4, 100)
        self.assertEqual(v, 119)

    def test_raw_eval_3(self):
        v = collatz_raw_eval(30, 2)
        self.assertEqual(v, 112)
    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(4, 100)
        self.assertEqual(v, 119)

    def test_eval_3(self):
        v = collatz_eval(30, 2)
        self.assertEqual(v, 112)

    def test_eval_4(self):
        v = collatz_eval(500000, 1000000)
        self.assertEqual(v, 525)

    def test_eval_5(self):
        v = collatz_eval(139686, 342056)
        self.assertEqual(v, 443)

    def test_eval_6(self):
        v = collatz_eval(919524, 491469)
        self.assertEqual(v, 525)

    def test_eval_7(self):
        v = collatz_eval(128138, 617447)
        self.assertEqual(v, 470)

    def test_eval_8(self):
        v = collatz_eval(203089, 209178)
        self.assertEqual(v, 373)

    def test_eval_9(self):
        v = collatz_eval(645599, 53931)
        self.assertEqual(v, 509)

    def test_eval_10(self):
        v = collatz_eval(188485, 610406)
        self.assertEqual(v, 470)
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 1)
        self.assertEqual(w.getvalue(), "1 10 1\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 4, 100, 1)
        self.assertEqual(w.getvalue(), "4 100 1\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 30, 2, 1)
        self.assertEqual(w.getvalue(), "30 2 1\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 500000, 1000000, 1)
        self.assertEqual(w.getvalue(), "500000 1000000 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n4 100\n30 2\n20 34\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n4 100 119\n30 2 112\n20 34 112\n")

    def test_solve_2(self):
        r = StringIO("1 10000\n400 54206\n3212 20\n203 300040\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10000 262\n400 54206 340\n3212 20 217\n203 300040 443\n")

    def test_solve_3(self):
        r = StringIO("1 1000000\n41212 100\n304142 2\n209392 304\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1000000 525\n41212 100 324\n304142 2 443\n209392 304 383\n")
# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
