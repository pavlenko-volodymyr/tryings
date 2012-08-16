# -*- coding: utf-8 -*- 

from __future__ import division
import sys
from pprint import pprint


def calculate_with_capitalization(startmoney, period, rate, increase_money):
    
    currmoney = startmoney
    month_rate = (rate / 100) / period
    finall_money = []

    for i in xrange(period):
        before = round(currmoney, 2)
        month_money = round(month_rate * currmoney, 2)
        after_calc = currmoney = round(increase_money + before + month_money, 2)
        finall_money.append(
            (
                before, month_money, increase_money, after_calc
            )
        )

    pprint(finall_money)
    print(sum(i[1] for i in finall_money))


def calculate_without_capitalization(startmoney, period, rate, increase_money):

    currmoney = startmoney
    month_rate = (rate / 100) / period
    finall_money = []

    for i in xrange(period):
        before = round(currmoney, 2)
        month_money = round(month_rate * currmoney, 2)
        after_calc = currmoney = round(increase_money + before, 2)
        finall_money.append(
            (
                before, month_money, increase_money, after_calc
            )
        )

    pprint(finall_money)
    print(sum(i[1] for i in finall_money))