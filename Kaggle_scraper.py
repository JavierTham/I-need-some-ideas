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

# 1. get_topic() not modular enough
# 2. need to find way to keep track of kernels already seen
# 3. require another function to get kernels from new page
# 4. require public functions for clients/users

class KernelList:
    page = 1
    sort_by = "hotness"
    curr_selection = {}
    kernel_titles = []

    # function to get a list of kernels ("code" in Kaggle)
    def get_kernels(self, page):
        # restrict sorting to 1 category only as we only want the popular ones which would be well written 
        kernels = api.kernels_list(page = page, sort_by = self.sort_by, page_size = 20)

        # get the references
        kernel_refs = [getattr(kernel, 'ref') for kernel in kernels]

        # get the titles
        self.kernel_titles = [getattr(kernel, 'title') for kernel in kernels]

        # create a dictionary to store current selection of kernels
        self.curr_selection = dict(zip(self.kernel_titles, kernel_refs))

    # pick 1 random topic from list of 20
    def get_topic(self):
        # choose random kernel
        topic_idx = random.randint(0, len(self.curr_selection) - 1)
        kernel_title = self.kernel_titles[topic_idx]
        
        # remove from curr_selection
        self.curr_selection.pop(kernel_title)
        self.kernel_titles.remove(kernel_title)
        return kernel_title

KL = KernelList()
KL.get_kernels(1)
print(KL.get_topic())
print(KL.get_topic())
print(KL.get_topic())
print(KL.get_topic())
print(KL.get_topic())
print(KL.get_topic())
print(KL.get_topic())