#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singeltone(type):
    instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls.__name__ not in Singeltone.instances:            
            Singeltone.instances[cls.__name__] = type.__call__(cls, *args, **kwargs)
        return Singeltone.instances[cls.__name__]


class Test(object):
    __metaclass__ = Singeltone


inst0 = Test()
inst1 = Test()
print(id(inst1) == id(inst0))
