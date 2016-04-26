# Examples #

Look at the file located in data/example1.txt


```python
Updating doc for data/example1.txt
comment_blocks = get_comment_blocks(file, comment_symbol = "\#'")
{(20, 2), (27, 2), (2, 6), (9, 3)}
select_comment_blocks(file, comment_blocks, condition = "@export")
{(2, 6), (9, 3)}
select_comment_blocks(file, comment_blocks, condition = "<TAG2INCLUDE>")
{(2, 6)}
get_line_index(file, main_function, condition = "<TAG2INCLUDE>")
[5, 6]
get_functions_informations(file, func_to_get_infos, tag_func_name = "@name", tag_func_desc = "@title")
{('FUNCTIO NAME', 'FUNCTION DESC')}
format_itemize(functions_informations, comment_symbol = "\#'", tag = "<TAG2INCLUDE>")
#' <TAG2INCLUDE>
#' \itemize{
#'  \item FUNCTIO NAME: FUNCTION DESC
#' }
#' <TAG2INCLUDE>
```



