"""
Author: Joseph Lefevre
"""
from .base import GroupFusedLasso


class GFLLARS(GroupFusedLasso):
    def __init__(self):
        raise NotImplementedError

    def detect(self, X, **kwargs):
        """
        Detect the breakpoints in X.
        :param X:
        :param kwargs:
        :return:
        """
        raise NotImplementedError
