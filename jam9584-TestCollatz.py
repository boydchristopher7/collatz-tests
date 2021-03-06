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
        s = "67 89\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  67)
        self.assertEqual(j, 89)

    def test_read_3(self):
        s = "988 1110\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  988)
        self.assertEqual(j, 1110)
    

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
        v = collatz_eval(500, 599)
        self.assertEqual(v, 137)

    def test_eval_6(self):
        v = collatz_eval(606, 666)
        self.assertEqual(v, 145)

    def test_eval_7(self):
        v = collatz_eval(4001, 9999)
        self.assertEqual(v, 262)

    def test_eval_8(self):
        v = collatz_eval(10000, 11111)
        self.assertEqual(v, 268)

    def test_eval_9(self):
        v = collatz_eval(62533, 77777)
        self.assertEqual(v, 351)
        
    
        

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 15, 115, 119)
        self.assertEqual(w.getvalue(), "15 115 119\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 303, 404, 144)
        self.assertEqual(w.getvalue(), "303 404 144\n")


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
        r = StringIO("15 115\n303 404\n499 598\n200 701\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "15 115 119\n303 404 144\n499 598 137\n200 701 145\n")

    def test_solve_3(self):
        r = StringIO("777 1425\n867 5309\n4440 6661\n9000 9001\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "777 1425 182\n867 5309 238\n4440 6661 262\n9000 9001 141\n")

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
