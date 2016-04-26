#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    Provide command line analysis and verification
"""

import argparse
import os

def read_args(args):
    """ Read cli argument """

    parser = __create_parser()
    arg = vars(parser.parse_args(args))

    return arg



def __create_parser():
    """ Create the args parser """

    parser = argparse.ArgumentParser(
        usage       = "./%(prog)s [-h] [--example] [--c '#'] [-b '@export'] [-m '<TAG2INCLUDE>'] [--tagname '@name'] [--tagdesc '@title'] -i DIRECTORY \n", 
        description = "Automatic update of documentation for R scripts",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("--example", action = "store_true", help = "Run example")
    parser.add_argument("--comment", default = "#\'", help = "define comment symbol")
    parser.add_argument("-i", type = __isdir, required = True,
        help = "Directory where the files to update are located")
    parser.add_argument("-b", "--block", default = "@export",
        help = "tag for filtering comment blocks to insert")
    parser.add_argument("-m", "--main", default = "<TAG2INCLUDE>",
        help = "tag for finding the main comment block where the --blocks will be inserted")
    parser.add_argument("--tagname", default = "@name",
        help = "in a bloc, tag to identify function name")
    parser.add_argument("--tagdesc", default = "@title",
        help = "in a bloc, tag to identify function desc")
    return parser



def __isfile(val):
    """Check  if the path is leading to a file."""
    val = str(val)

    if not os.path.isfile(val):
        raise argparse.ArgumentTypeError(val + " is not a file")

    return val


def __isdir(val):
    """Check  if the path is leading to a directory."""
    val = str(val)

    if not os.path.isdir(val):
        raise argparse.ArgumentTypeError(val + " is not a directory")

    return val