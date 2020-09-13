#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "manuel Velasco and John Wilkinson"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""

    """Create a command line parser object with 1 argument definitions."""
    parser = argparse.ArgumentParser(
        description="echo.py")
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument(
        'text', help='this text give usage')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if ns.title:
        print(ns.text.title())
    elif ns.lower:
        print(ns.text.lower())
    elif ns.upper:
        print(ns.text.upper())
    else:
        print(ns.text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
