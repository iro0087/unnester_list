# Unnester

Class composed of a function whose its goal is to manipulate nested list.

## Usage:

`unnester.ns(input_l, dim_end=1, strt_l=[], rtn_l=[], id_rec_main=0, wrk_l=None, flag_l=[])`

The two paramters you need to know are input_l and dim_end. The fact that it is a recursive function requires the presence of the others paramters that are used each iteration of the recursive function.

input_l: The nested list you want to unnest to a certain point.
dim_end: The dimension from which you want to keep. 

`unnester.ns(input_l=[1, [5, [[2], 4, [23, 3, 3]]], 2, 3334, [4, [55, 56], 7, [77, [66, 67], 78], 2, [33, 5]], 3, [5, 6], 4], dim_end=3, strt_l=[], rtn_l=[], flag_l=[])`

will return:

`[1, 5, [2], 4, [23, 3, 3], 2, 3334, 4, 55, 56, 7, 77, [66, 67], 78, 2, 33, 5, 3, 5, 6, 4]`

`unnester.ns([1, [2], 3], dim_end=1, strt_l=[], rtn_l=[], flag_l=[])`

will return

[1, [2], 3]

`unnester.ns([1, [2], 3], dim_end=2, strt_l=[], rtn_l=[], flag_l=[])`

will return

[1, 2, 3]

Here, we are forced to declare the list parameters in the function call because if not declared, it will take their last value. 
This is the case for python 3.11.6.



