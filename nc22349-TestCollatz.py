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

from Collatz import cache, collatz_read, get_cache_low, get_cache_high, max_for_cached_range, collatz_single_num_eval, collatz_range_eval, collatz_eval, collatz_print, collatz_solve


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
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 1)

    def test_read_3(self):
        s = "a b"
        self.assertFalse(collatz_read(s))

    def test_read_4(self):
        s = "-1 3"
        self.assertFalse(collatz_read(s))

    def test_read_5(self):
        s = "3.14 159"
        self.assertFalse(collatz_read(s))

    def test_read_6(self):
        s = "1 1"
        self.assertFalse(collatz_read(s))

    def test_read_7(self):
        s = "4 14 4"
        self.assertFalse(collatz_read(s))

    # ----
    # get_cache_low
    # ----

    def test_low_1(self):
        self.assertEqual(get_cache_low(1), 1)

    def test_low_2(self):
        self.assertEqual(get_cache_low(20000), 20001)

    def test_low_3(self):
        self.assertEqual(get_cache_low(27874), 40001)

    # ----
    # get_cache_high
    # ----

    def test_high_1(self):
        self.assertEqual(get_cache_high(20000), 20000)

    def test_high_2(self):
        self.assertEqual(get_cache_high(20001), 20000)

    def test_high_3(self):
        self.assertEqual(get_cache_high(999999), 999999)

    # ----
    # max_for_cached_range
    # ----

    def test_cached_range_1(self):
        self.assertEqual(max_for_cached_range(20001, 980000), 525)

    def test_cached_range_2(self):
        self.assertEqual(max_for_cached_range(160001, 820000), 509)

    def test_cached_range_3(self):
        self.assertEqual(max_for_cached_range(20001, 240000), 443)


    # ----
    # single_num_eval
    # ----

    def test_single_eval_1(self):
        v = collatz_single_num_eval(3)
        self.assertEqual(v, 8)

    def test_single_eval_2(self):
        v = collatz_single_num_eval(31)
        self.assertEqual(v, 107)

    def test_single_eval_3(self):
        v = collatz_single_num_eval(44)
        self.assertEqual(v, 17)


    # ----
    # range_eval
    # ----       

    def test_range_eval_1(self):
        v = collatz_eval(999999, 1000000)
        self.assertEqual(v, 259)

    def test_range_eval_2(self):
        v = collatz_eval(820002, 860000)
        self.assertEqual(v, 525)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(175000, 982115)
        self.assertEqual(v, 525)
        
    def test_eval_2(self):
        v = collatz_eval(162385, 822322)
        self.assertEqual(v, 509)
        
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 57, 60, 33)
        self.assertEqual(w.getvalue(), "57 60 33\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")       

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
        r = StringIO("225 18\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "225 18 125\n")

    def test_solve_3(self):
        r = StringIO("\n")
        w = StringIO()
        self.assertFalse(collatz_solve(r, w))
    

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
