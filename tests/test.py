import unittest

import sys
import os
import json

sys.path.insert(1, '../src/')

import app
from items_calc import calc_pages

class TestPageCalc(unittest.TestCase):

        #legacy page1 - 0-99 ; page2 = 100 - 199 ;page3 = 200 - 299; page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
    def test_calc1(self):
        expected_arr = [4,5,6]
        #page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 
        pages = calc_pages(2,300) # 300 - 599
        self.assertEqual(expected_arr, pages)

    def test_calc2(self):
        expected_arr = [4,5,6,7]
        #page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
        pages = calc_pages(2,301) # 301 - 601
        self.assertEqual(expected_arr, pages)

    def test_calc3(self):
        expected_arr = [2,3]
        # page2 = 100 - 199 ;page3 = 200 - 299; page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
        pages = calc_pages(2,150) # 150 - 299
        self.assertEqual(expected_arr, pages)

    def test_calc4(self):
        expected_arr = [1]
        # page2 = 100 - 199 ;page3 = 200 - 299; page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
        pages = calc_pages(1,50) # 150 - 299
        self.assertEqual(expected_arr, pages)

    def test_calc5(self):
        expected_arr = [1]
        # page2 = 100 - 199 ;page3 = 200 - 299; page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
        pages = calc_pages(2,50) # 150 - 299
        self.assertEqual(expected_arr, pages)

    def test_calc6(self):
        expected_arr = [2]
        # page2 = 100 - 199 ;page3 = 200 - 299; page4 = 300 - 399; page 5 = 400 - 499; page6 = 500-599 ; page7= 600-699
        pages = calc_pages(3,50) # 150 - 299
        self.assertEqual(expected_arr, pages)

class TestAppPageGet(unittest.TestCase):

    def test_get_sync1(self):
        expected = None

        with open('./10000.json','r') as f:
            expected = json.load(f)

        pages = app.get_sync(2,10000)   
        self.assertEqual(expected, pages)

    def test_get_sync2(self):
        expected = None

        with open('./1030.json','r') as f:
            expected = json.load(f)

        pages = app.get_sync(2,1030)
        self.assertEqual(expected, pages)

    def test_get_async3(self):
        expected = None

        with open('./10000.json','r') as f:
            expected = json.load(f)

        pages = app.get_async(2,10000)         
        self.assertEqual(expected, pages)

    def test_get_async4(self):
        
        expected = None

        with open('./1030.json','r') as f:
            expected = json.load(f)

        pages = app.get_async(2,1030)
        self.assertEqual(expected, pages)

if __name__ == '__main__':
    unittest.main()

