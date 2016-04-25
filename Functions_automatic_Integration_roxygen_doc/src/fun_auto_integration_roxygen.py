#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This program is designed to write a pseudo doc from comments
    into the files of the musclr package (INRA Grignon)

    Usage: python3 list_func_roxygen.py directory


    @author Jerome Pivert <pivertjerome@gmail.com>
"""


##########
# Import #
##########
import os
import sys
import re
import glob # best. module. ever.


def get_comment_blocks(file_content, comment_symbol):
    """
        This function return a set of tuples containing the starting position
        of a comment block and it's length

        A block comment is defined by:
            line starting with a comment_symbol
            no empty lines nor non commented lines
    """


    comment_blocks = set()
    in_block = False # block delimiter
    block_start = int() # starting index of a block
    block_length = 0

    for index, line in enumerate(file_content):
        is_commented = line.startswith(comment_symbol)
        # comment line OK AND NOT in block yet -- define new block
        if is_commented and not in_block:
            in_block = True
            block_start = index
            block_length += 1
        # comment line AND in block -- block_length ++
        elif is_commented and in_block:
            block_length += 1
        # encounter not commented line in a block -- end of block
        elif in_block:
            comment_blocks.add((block_start, block_length))
            in_block = False
            block_length = 0
        # uncommented line -- ignore
        else:
            continue

    # Only if a commented line ends the file
    if in_block: comment_blocks.add((block_start, block_length))
    return comment_blocks


def select_comment_blocks(file_content, comment_blocks, condition):
    """
        For a block comment, search the ones that match the condition
        The condition is a term that should be retrieved or not in the comment
        blocks defined by comment_blocks

        Return a set containing the tuples in comment_blocks for which their
        block is matching the condition
    """
    matching_blocks = set()

    # i = block start; j = block size
    for i, j in comment_blocks:
        for line in file_content[i:i+j]:
            if condition in line:
                matching_blocks.add((i,j))
            else:
                continue

    return matching_blocks



if __name__ == "__main__":
    #@resume: class for colors (ASCII code) used for coloring terminal output such as print
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'


    filename = "/home/jerome/Documents/DEV/misc/misc/Functions_automatic_Integration_roxygen_doc/data/example1.txt"
    print(bcolors.HEADER + "Updating doc for " + bcolors.ENDC + filename)
    with open(filename, 'r') as INFILE:
        file = INFILE.readlines()
        comment_blocks = get_comment_blocks(file, "#\'")
        print(comment_blocks)

        export_matching_blocks = select_comment_blocks(file, comment_blocks, "@export")
        print(matching_blocks)