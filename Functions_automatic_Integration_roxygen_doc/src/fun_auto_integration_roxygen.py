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

########
# Misc #
########
#@resume: class for colors (ASCII code) used for coloring terminal output such as print
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'



#############
# Main shit #
#############
def get_comment_blocks(file_content, comment_symbol):
    """
        This function return a set of tuples containing the starting position
        of a comment block and it's length

        A block comment is defined by:
            line starting with a comment_symbol
            no empty lines nor non commented lines


        file_content   : list containing the current file
        comment_symbol : string defining a comment line
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


        file_content   : list containing the current file
        comment_blocks : set of tuples with the loc and len of comment blocks
        condition      : string to be find in a comment block
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


def get_line_index(file_content, comment_block, condition):
    """
        Similar to select_comment_blocks except that it returns the index
        of the lines matching the condition within the block, if only one
        condition found, simule 2 matchs on same line (start and end)
        WARNING: only one block allowed

        file_content   : list containing the current file
        comment_blocks : set of tuples with the loc and len of comment blocks
        condition      : string to be find in a comment block
    """

    # Check if len == 1
    if len(comment_block) != 1:
        raise ValueError("comment_block must be of length 1, " + len(comment_block) + " given")

    condition_index = list()

    block_start, block_len = next(iter(comment_block))
    for index, line in enumerate(file_content):
        # Before block
        if index < block_start:
            continue
        # Inside the block
        elif index >= block_start and  index < block_start + block_len:
            if condition in line:
                condition_index.append(index)
        # Break when outside block
        else:
            break
    
    if len(condition_index) == 1:
        condition_index += condition_index

    return condition_index


def get_functions_informations(file_content, comment_blocks, tag_func_name, tag_func_desc):
    """
        For several comment blocks return a set of tuples containing the name
        and the title of the functions defined by the comment blocks

        It will remove all char before the tags so a line like
        # <TAG_DESC> description of the function
        will be returned as "description of the function"


        file_content   : list containing the current file
        comment_blocks : set of tuples with the loc and len of comment blocks
        tag_func_name  : tag of the line where the name of the func is located
        tag_func_desc  : tag of the line where the desc of the func is located
    """
    functions_informations = set()


    reg_name = re.compile(r"^.*"+tag_func_name+"\s+(.*)$")
    reg_desc = re.compile(r"^.*"+tag_func_desc+"\s+(.*)$")
    # name_found = False
    # desc_found = False


    # i = block start; j = block size
    for i, j in comment_blocks:
        name_found = False
        desc_found = False
        # Parse a comment block
        for line in file_content[i:i+j]:
            # Find the name of the function
            if not name_found:
                name_search = re.search(reg_name, line)
                if name_search:
                    name = name_search.group(1).strip()
                    name_found = True
            # Find the desc of the function
            if not desc_found:
                desc_search = re.search(reg_desc, line)
                if desc_search:
                    desc = desc_search.group(1).strip()
                    desc_found = True
            
            # If name && desc already found just add && break
            if name_found and desc_found:
                functions_informations.add((name, desc))
                break

    return functions_informations


def format_itemize(informations, comment_symbol, tag):
    """
        Write a latex itemize for all data in informations and return
        it as a list, need comment_symbol

        informations   : set of tuple containing (name, desc) of a func
        comment_symbol : string defining a comment line
        tag            : tag of the main function to include between
    """

    lines = list()

    lines.append(comment_symbol + " " + tag + "\n")
    lines.append(comment_symbol + " \itemize{\n")
    for name, desc in informations:
        raw = comment_symbol + "\t\item " + name + ": " + desc + "\n"
        lines.append(raw)
    lines.append(comment_symbol + " }\n")
    lines.append(comment_symbol + " " + tag + "\n")

    return lines


def update_file_list(file_content, tag_index, formated_informations):
    """
        Return the list file_content with formated_informations inserted at
        tag_index position.

        file_content          : list containing the current file
        tag_index             : position, in list, of tags to insert between
        formated_informations : preformated_func_infos
    """

    file_content[tag_index[0]: tag_index[1]+1] = formated_informations
    return file_content


def run_example():
    """
        Use the file data/example1.txt and print step by step the results
        Alternatively you can find the results of this function on the
        README

        It creates a file example1_out.txt in the same directory and then delete it
    """


if __name__ == "__main__":



    if len(sys.argv) > 1:
        for filename in glob.iglob(sys.argv[1]+'*'):
            # parse file
            print(bcolors.HEADER + "Updating doc for " + bcolors.ENDC + filename)
            with open(filename, 'r') as INFILE:
                file = INFILE.readlines()

    filename = "data/example1_out.txt"
    print(bcolors.HEADER + "Updating doc for " + bcolors.ENDC + filename)
    with open(filename, 'r') as INFILE:
        file = INFILE.readlines()

    # Identify comment blocks
    comment_blocks = get_comment_blocks(file, "#\'")
    print(comment_blocks)

    # Filter all comment blocks
    export_matching_blocks = select_comment_blocks(file, comment_blocks, "@export")
    print(export_matching_blocks)

    main_function = select_comment_blocks(file, comment_blocks, "<TAG2INCLUDE>")
    print(main_function)

    # Get informations about the functions defined by the filtered comment blocks
    include_tag_index = get_line_index(file, main_function, "<TAG2INCLUDE>")
    print(include_tag_index)

    func_to_get_infos = export_matching_blocks ^ main_function # symmetric difference
    functions_informations = get_functions_informations(file, func_to_get_infos, "@name", "@title")
    print(functions_informations)

    # Assemble informations in an itemize
    itemize = format_itemize(functions_informations, "#\'", "<TAG2INCLUDE>")
    print(''.join(itemize))

    # Insert into file_content
    file = update_file_list(file, include_tag_index, itemize)
    #print(''.join(file))

    filename = "data/example1_out.txt"
    with open(filename, 'w') as OUTFILE:
        OUTFILE.write(''.join(file))

    input("End example (it will remove the created file)")
    os.system('rm ' + filename)