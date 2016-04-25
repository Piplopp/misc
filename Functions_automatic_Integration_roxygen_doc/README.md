# Examples #

Look at the file located in data/example1.txt


---
## Functions
### get\_comment\_blocks(file\_content, comment\_symbol)
This function aims to return a set of tuples containing the starting position of a comment block in the `file_content`.

With _example1.txt_ and `comment_symbol = "#"` it should return (set not ordered, be carefull):

```python
{(25, 2), (7, 3), (2, 4), (18, 2)}
```

### select\_comment\_blocks(file\_content, comment\_blocks, condition)
Return a set containing the tuples in `comment_blocks` for which their block is matching the `condition`

With _example1.txt_ and `condition = "@export"` it should return:


```python
{(7, 3), (2, 4)}
```