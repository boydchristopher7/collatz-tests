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

# # #write test cases
    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "102 800\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  102)
        self.assertEqual(j, 800)

    def test_read3(self):
        s = "10 15\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 15)
    def test_read4(self):
        s = "a 11 \n"
        result = collatz_read(s)
        self.assertFalse(result)
    def test_read5(self):
        s = "1"
        result = collatz_read(s)
        self.assertFalse(result)

    def test_read6(self):
        s = "-10 -15\n"
        result = collatz_read(s)
        self.assertFalse(result)
   

    def test_read7(self):
        s = "-10 15 16\n"
        result = collatz_read(s)
        self.assertFalse(result) 


#     # # ----
#     # # eval
#     # # ----

    def test_eval_1(self):
        v = collatz_eval(5, 10)

        self.assertEqual(v, 20)

    def test_eval_2(self):
        # same number
        v = collatz_eval(10101010191,10101011910)
        self.assertEqual(v,598)

    def test_eval_3(self):

        v = collatz_eval(512,4040)

        self.assertEqual(v,238)
    def test_eval_4(self):

        v = collatz_eval(15,10)

        self.assertEqual(v,18)

    def test_eval_5(self):

        v = collatz_eval(230,232)

        self.assertEqual(v,128)

    



#     # -----
#     # print
#     # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print2(self):
        w = StringIO()
        collatz_print(w, 102, 800, 171)
        self.assertEqual(w.getvalue(), "102 800 171\n")
    def test_print3(self):
        w = StringIO()
        collatz_print(w, 1, 101, 119)
        self.assertEqual(w.getvalue(), "1 101 119\n")


# #     # -----
# #     # solve
# #     # -----

# # # write test cases

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    # i < j
    def test_solve2(self):
        r = StringIO("102 800\n5 8\n1 101\n10 15\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "102 800 171\n5 8 17\n1 101 119\n10 15 18\n")

    def test_solve3(self):
        r = StringIO("1003 101\n100 200\n16 1994\n512 4040\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "101 1003 179\n100 200 125\n16 1994 182\n512 4040 238\n")
   


# ----
# main
# ----

if __name__ == "__main__":
    main()

#--
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
