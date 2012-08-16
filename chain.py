#!/usr/bin/env python
# -*- coding: utf-8 -*-

def chain(*args):
    cur_i = 0
    seq = []
    for i in args:
        for j in i: seq.append(j)
    last = len(seq) - 1
    while True:
        yield seq[cur_i]
        if cur_i != last: cur_i += 1
        else: cur_i = 0

if __name__ == '__main__':
    s0 = range(5)
    s1 = range(5,11)
    end = len(s0) + len(s1)    
    c = chain(s0, s1)
    for i in range(end+10):
        print i, c.next()