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
from Collatz import collatz_compute_cycle, collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_helper

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
      s = "1000 108031\n"
      i, j = collatz_read(s)
      self.assertEqual(i,  1000)
      self.assertEqual(j, 108031)

    def test_read_3(self):
      s = "99999 5\n"
      i, j = collatz_read(s)
      self.assertEqual(i,  99999)
      self.assertEqual(j, 5)

    # ----
    # eval_helper
    # ----

    def test_collatz_eval_helper_1(self):
      v = collatz_eval_helper(1, 10)
      self.assertEqual(v, 20)

    def test_collatz_eval_helper_2(self):
      v = collatz_eval_helper(100,200)
      self.assertEqual(v,125)

    def test_collatz_eval_helper_3(self):
      v = collatz_eval_helper(201,210)
      self.assertEqual(v,89)

    def test_collatz_eval_helper_4(self):
      v = collatz_eval_helper(900, 1000)
      self.assertEqual(v, 174)

    # ----
    # compute_cycle
    # ----

    def test_collatz_compute_cycle_1(self):
      v = collatz_compute_cycle(9)
      self.assertEqual(v, 20)
    def test_collatz_compute_cycle_2(self):
      v = collatz_compute_cycle(49268)
      self.assertEqual(v, 159)
    def test_collatz_compute_cycle_3(self):
      v = collatz_compute_cycle(896729)
      self.assertEqual(v, 158)

    # ----
    # eval
    # ----

    def test_eval_1(self):
      v = collatz_eval(1,10)
      self.assertEqual(v, 20)

    def test_eval_2(self):
      v = collatz_eval(1,11)
      self.assertEqual(v, 20)

    def test_eval_3(self):
      v = collatz_eval(50, 100000)
      self.assertEqual(v, 351)

    def test_eval_4(self):
      v = collatz_eval(79802, 34508)
      self.assertEqual(v,351)

    def test_eval_5(self):
      v = collatz_eval(1100, 1200)
      self.assertEqual(v, 182)

    def test_eval_6(self):
      v = collatz_eval(999000, 999999)
      self.assertEqual(v, 396)

    # -----
    # print
    # -----

    def test_print_1(self):
       w = StringIO()
       collatz_print(w, 999000, 999999, 396)
       self.assertEqual(w.getvalue(), "999000 999999 396\n")

    def test_print_2(self):
       w = StringIO()
       collatz_print(w, 1, 10, 20)
       self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_3(self):
       w = StringIO()
       collatz_print(w, 79802, 34508, 351)
       self.assertEqual(w.getvalue(), "79802 34508 351\n")

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
       r = StringIO("801054 534234\n173072 379217\n153618 925901\n")
       w = StringIO()
       collatz_solve(r, w)
       self.assertEqual(
         w.getvalue(), "801054 534234 509\n173072 379217 443\n153618 925901 525\n")

    def test_solve_3(self):
       r = StringIO("78430 444444\n401456 638112\n297261 573755\n")
       w = StringIO()
       collatz_solve(r, w)
       self.assertEqual(
         w.getvalue(), "78430 444444 449\n401456 638112 509\n297261 573755 470\n")

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
