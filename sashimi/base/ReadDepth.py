#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u"""
Created by ygidtu@gmail.com at 2019.12.06

Changelog:
    1. move several attributes and functions to corresponding file objects, turn this into pure data class
    2. add transform to log2, log10 or zscore transform the data while plotting
"""
from typing import Dict, Optional

import numpy as np
from scipy.stats import zscore

from sashimi.base.Junction import Junction


class ReadDepth(object):
    u"""
    Migrated from SplicePlot ReadDepth class

    add a parent class to handle all the position comparison
    """

    def __init__(self,
                 wiggle: np.array,
                 junctions_dict: Optional[Dict[Junction, int]] = None,
                 side_plus: Optional[np.array] = None,
                 side_minus: Optional[np.array] = None,
                 plus: Optional[np.array] = None,
                 minus: Optional[np.array] = None,
                 junction_dict_plus: Optional[np.array] = None,
                 junction_dict_minus: Optional[np.array] = None,
                 strand_aware: bool = False):
        u"""
        init this class
        :param wiggle: a numpy.ndarray object represented the whole read coverage, should be summation of plus and minus
        :param junctions_dict: a dict represented the coordinate of each intron as well as frequency
        :param side_plus: a numpy.ndarray object represented the forward site coverage
        :param side_minus: a numpy.ndarray object represented the reverse site coverage
        :param plus: a numpy.ndarray object represented the forward strand read coverage
        :param minus: a numpy.ndarray object represented the reverse strand read coverage
        :param strand_aware: strand specific depth
        :param junction_dict_plus: these splice junction from plus strand
        :param junction_dict_minus: these splice junction from minus strand
        """
        self.wiggle = wiggle
        self.junctions_dict = junctions_dict
        self.strand_aware = strand_aware
        self.max = max(self.wiggle)
        self.plus = plus
        self.minus = minus * -1 if minus is not None else minus
        self.junction_dict_plus = junction_dict_plus
        self.junction_dict_minus = junction_dict_minus
        self.side_plus = side_plus
        self.side_minus = side_minus * -1 if side_minus is not None else side_minus

    def __add__(self, other):

        """
            __add__ allows two ReadDepth objects to be added together using the + symbol

            Both self and other must have the same low and high attributes

            return value:
                A new ReadDepth object containing the sum of the two original ReadDepth objects
        """

        if len(self.wiggle) == len(other.wiggle):
            junctions = self.junctions_dict
            for i, j in other.junctions_dict.items():
                if i in junctions.keys():
                    junctions[i] += j
                else:
                    junctions[i] = j
            return ReadDepth(
                self.wiggle + other.wiggle,
                junctions_dict=junctions,
                plus=self.plus + other.plus,
                minus=self.minus + other.minus
            )

    def add_customized_junctions(self, other):
        u"""
        Add customized junctions to plot
        :param other:
        :return:
        """
        new_junctions_dict = {}

        for key, value in self.junctions_dict.items():
            if key in other.junctions_dict:
                new_junctions_dict[key] = value + other.junctions_dict[key]
            else:
                new_junctions_dict[key] = value

        for key, value in list(other.junctions_dict.items()):
            if key not in self.junctions_dict:
                new_junctions_dict[key] = value

        self.junctions_dict = new_junctions_dict
        return new_junctions_dict

    def transform(self, log_trans: str):
        funcs = {"10": np.log10, "2": np.log2, "zscore": zscore}

        if log_trans in funcs.keys():
            self.wiggle = funcs[log_trans](self.wiggle + 1)

            if self.plus is not None:
                self.plus = funcs[log_trans](self.plus + 1)

            if self.minus is not None:
                self.minus = -funcs[log_trans](np.abs(self.minus + 1))


if __name__ == '__main__':
    pass