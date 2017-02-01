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


from Collatz import *

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
        s = "-1 9999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -1)
        self.assertEqual(j, 9999)

    def test_read_3(self):
        s = "111 200000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  111)
        self.assertEqual(j, 200000)

    def test_read_4(self):
        s = "58 11\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  58)
        self.assertEqual(j, 11)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10, the_cache={})
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200, the_cache={})
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210, the_cache={})
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000, the_cache={})
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(5, 333, the_cache={})
        self.assertEqual(v, 144)

    def test_eval_6(self):
        v = collatz_eval(2, 2223, the_cache={})
        self.assertEqual(v, 183)

    def test_eval_7(self):
        v = collatz_eval(788, 375, the_cache={})
        self.assertEqual(v, 171)

    # ----------------------------
    # collatz_compute helper function
    # -----------------------------

    def test_compute_1(self):
        v = collatz_compute(1, the_cache={})
        self.assertEqual(v, 1)

    def test_compute_2(self):
        v = collatz_compute(10, the_cache={})
        self.assertEqual(v, 7)

    def test_compute_3(self):
        v = collatz_compute(17, the_cache={})
        self.assertEqual(v, 13)

    # ----------------------------
    # collatz_compute helper function
    # -----------------------------

    def test_cache_1(self):
        v = check_cache(1, the_cache={})
        self.assertEqual(v, 1)

    def test_cache_2(self):
        v = check_cache(10, the_cache={})
        self.assertEqual(v, 7)

    def test_cache_3(self):
        v = check_cache(17, the_cache={})
        self.assertEqual(v, 13)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 17, 11, 20999)
        self.assertEqual(w.getvalue(), "17 11 20999\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1000, -910, 20786)
        self.assertEqual(w.getvalue(), "1000 -910 20786\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO(
            "1 10\n100 200\n201 210\n900 1000\n5 333\n2 2223\n788 375\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n5 333 144\n2 2223 183\n788 375 171\n")

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
