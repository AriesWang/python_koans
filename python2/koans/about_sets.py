#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)
        only=set(['MacLeod', 'Ramirez', 'Matunas',
             'Malcolm'])

        self.assertEqual(only, there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set(['2','5' ,'4' ,'3' ,'1' ]), set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        list_c=['1', '2', '3', '4', '5']
        self.assertEqual(list_c, sorted(set('13245')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = set(['MacLeod', 'Wallace', 'Willie'])
        warriors = set(['MacLeod', 'Wallace', 'Leonidas'])
        diff=set(['Willie'])
        union=set(['MacLeod', 'Wallace', 'Willie', 'Leonidas'])
        mix=set(['MacLeod', 'Wallace'])
        covariance=set(['Willie', 'Leonidas'])

        self.assertEqual(diff, scotsmen - warriors)
        self.assertEqual(union, scotsmen | warriors)
        self.assertEqual(mix, scotsmen & warriors)
        self.assertEqual(covariance, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in set([127, 0, 0, 1]))
        self.assertEqual(True, 'cow' not in set('apocalypse now'))

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')))

        self.assertEqual(False, set('cake') > set('pie'))
