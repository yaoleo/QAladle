#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2019/11/27 17:22:19
@Author  :   jyzhang 
@Contact :   yaodi163@163.com
@Description : 
'''

from abc import abstractclassmethod

from component import Component
from serializable import Serializable

class NNModel(Component, Serializable):
    @abstractclassmethod
    def train_on_batch(self, x: list, y: list):
        pass
