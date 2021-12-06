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
def get_kernels(page):
    # restrict sorting to 1 category only as we only want the popular ones which would be well written 
    return api.kernels_list(page = page, sort_by = 'hotness', page_size = 20)

# pick 1 random topic from list of 20
def get_topic(page):
    kernels = get_kernels(page)
    kernel_refs = [getattr(kernel, 'ref') for kernel in kernels]
    kernel_titles = [getattr(kernel, 'title') for kernel in kernels]
    kernel_dict = dict(zip(kernel_titles, kernel_refs))

    topic_idx = random.randint(1, len(kernels) - 1)
    return kernel_titles[topic_idx]

print(get_topic(1))


