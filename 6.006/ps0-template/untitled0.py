# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 01:09:46 2020

@author: marlo
"""

def make_box(color):
    def create_image(h, w):
        return {'height': h, 'width': w, 'pixels': [color for _ in range(h*w)]}
    return create_image

maker = make_box(40)
im = maker(20, 30)