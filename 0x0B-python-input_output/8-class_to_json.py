#!/usr/bin/python3

"""This module defines a python class-to-JSON function"""

def class_to_json(obj):
    """Returns the dictionary description of a simple data structure for JSON serilization of an object"""
    return obj.__dict__
