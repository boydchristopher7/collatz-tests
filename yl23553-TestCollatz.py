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

from Collatz import collatz_read, collatz_eval, collatz_calc, collatz_print, collatz_solve

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

    def test_read_more_than_two_nums(self):
        s = "20 30 40\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 20)
        self.assertEqual(j, 30)

    def test_read_empty_string(self):
        s = "\n"
        self.assertRaises(IndexError, lambda: collatz_read(s))

    def test_read_decimals(self):
        s = "1.1 999.99\n"
        self.assertRaises(ValueError, lambda: collatz_read(s))

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

    def test_eval_reverse_range_input(self):
        v = collatz_eval(999, 1)
        self.assertEqual(v, 179)

    def test_eval_no_range(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_zero_to_one(self):
        self.assertRaises(AssertionError, lambda: collatz_eval(0, 1))

    def test_eval_negative_range(self):
        self.assertRaises(AssertionError, lambda: collatz_eval(-150, -50))

    def test_return_value_validity(self):
        max_cycle = collatz_eval(100, 200)
        self.assertTrue(type(max_cycle) is int)

    # ----
    # calc helper function
    # ----
    def test_calc_correct_result(self):
        max_cycle = collatz_calc(50, 99, 0)
        self.assertEqual(max_cycle, 119)

    def test_calc_smaller_max_cycle_than_given(self):
        max_cycle = collatz_calc(1, 400, 532)
        self.assertEqual(max_cycle, 532)

    def test_calc_return_validity(self):
        max_cycle = collatz_calc(400, 500, 0)
        self.assertTrue(type(max_cycle) is int)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

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
        r = StringIO("6 19\n300 500\n1300 1332\n9999 10343\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "6 19 21\n300 500 144\n1300 1332 177\n9999 10343 242\n")

    def test_solve_3(self):
        r = StringIO("263591 843712\n896248 549708 525")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "263591 843712 525\n896248 549708 525\n")

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
