# Examples #

Look at the file located in data/example1.txt


---
## Functions
### get\_comment\_blocks(file\_content, comment\_symbol)
This function aims to return a set of tuples containing the starting position of a comment block in the `file_content`.

With _example1.txt_ and `comment_symbol = "#"` it should return (set not ordered, be carefull):

```python
{(26, 2), (8, 3), (2, 5), (19, 2)}
```

### select\_comment\_blocks(file\_content, comment\_blocks, condition)
Return a set containing the tuples in `comment_blocks` for which their block is matching the `condition`

With _example1.txt_ and `condition = "@export"` it should return:


```python
{(8, 3), (2, 5)}
```

With _example1.txt_ and `condition = "<TAG2INCLUDE>"` it should return:


```python
{(2, 5)}
```

### get\_functions\_informations(file\_content, comment\_block, tag\_func\_name, tag\_func\_desc)
Return a set of tuples containing the name of the function and its description. The evaluated comment blocks are defined by comment_block

With _example1.txt_, `tag_func_name = "@name"`, `tag_func_desc = "@title"` and considering the blocks without "<TAG2INCLUDE>" (aka set difference between the two results shown above) it should return:

```python
{("ANOTHER NAME", "ANOTHER TITLE")}
```