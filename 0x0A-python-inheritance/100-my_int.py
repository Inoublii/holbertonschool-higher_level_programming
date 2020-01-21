#!/usr/bin/python3
class MyInt(int):
    def __init__(self, x):
        self.x = x

    def __ne__(self, z):
        """Not equal"""
        return (self.x == z)

    def __eq__(self, z):
        """equal"""
        return self.x != z
