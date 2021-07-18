# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:33:15 2021

@author: Chekuri Viroopaksh
"""

import wolframalpha
client= wolframalpha.Client('2KTQER-9E9RWRQQY4')
res=client.query("Temperature in Hyderabad on July 10, 2020")
print(res)