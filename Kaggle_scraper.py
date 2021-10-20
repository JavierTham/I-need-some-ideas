import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import random

api = KaggleApi()
api.authenticate()

# kernels_list() function to get published code
""" kernels_list(...) 

    Parameters
    ==========
    page: the page of results to return (default is 1)
    page_size: results per page (default is 20)
    dataset: if defined, filter to this dataset (default None)
    competition: if defined, filter to this competition (default None)
    parent_kernel: if defined, filter to those with specified parent
    search: a custom search string to pass to the list query
    mine: if true, group is specified as "my" to return personal kernels
    user: filter results to a specific user
    language: the programming language of the kernel
    kernel_type: the type of kernel, one of valid_list_kernel_types (str)
    output_type: the output type, one of valid_list_output_types (str)
    sort_by: if defined, sort results by this string (valid_list_sort_by)
"""

# function to get a list of kernels ("code" in Kaggle)
def get_kernels(sort_by, page):
    return api.kernels_list(page = page, sort_by = sort_by, page_size = 2)

# sclass SortBy:
    # not sure if I should create an ENUM for the options
    # {key: 0 for key in api.valid_list_sort_by}  

# pick 1 random topic from list of 20
def get_topic(sort_by, page):
    lst_of_topics = get_kernels(sort_by, page)
    topic_idx = random.randint(1, len(lst_of_topics) - 1)
    return lst_of_topics[topic_idx]

# get input (sort_by and page)
#sort_by, page = input().split(" ")
#code = get_topic(sort_by, page)
#print(code)

# need to find way to get url