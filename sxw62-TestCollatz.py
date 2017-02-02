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

    # exception catch move to collatz_eval
    # def test_read_1(self): #read reversed string; reverse to normal
        # s = "10 1\n"
        # i, j = collatz_read(s)
        # self.assertEqual(i, 1)
        # self.assertEqual(j, 10)
        
    def test_read_2(self): #read decimals
        s = "1 10.0\n"
        with self.assertRaises(ValueError) as context:
            collatz_read(s)
    
    # exception catch moved to collatz_solve
    # def test_read_3(self): #blank string/blank
        # s = "\n"
        # with self.assertRaises(EmptyError) as context:
            # collatz_read(s)
    
    def test_read_3(self): #read non-numeric characters; raise error
        s = "a b\n"
        with self.assertRaises(ValueError) as context:
            collatz_read(s)
            
    def test_read_4(self): #read negatives; raise error
        s = "-10 1\n"
        with self.assertRaises(ValueError) as context:
            collatz_read(s)

    def test_read_5(self): #read zero; raise error
        s = "0 10\n"
        with self.assertRaises(ValueError) as context:
            collatz_read(s)

    def test_read_5(self): #read range of 1
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)
        
    def test_read_6(self): #read more or less than 2 inputs
        s = "1 10 20\n"
        with self.assertRaises(IndexError) as context:
            collatz_read(s)
    def test_read_7(self):
        s = "1\n"
        with self.assertRaises(IndexError) as context:
            collatz_read(s)
        
    
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
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)
        

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
            
    def test_solve_1(self): #solve for blank line
        r = StringIO("1 10\n \n100 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n")
        
    def test_solve_2(self):
        r = StringIO("1 10\na b\n100 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n")
        
    def test_solve_3(self):
        r = StringIO("a b\n-10 1\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n")

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
