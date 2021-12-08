# I need some ideas 
Creative juices aren't flowing 24/7, since I can't generate ideas on my own, why not let the computer do it for me?

## Problem
It might be difficult to think of topics for projects, or choose among the thousands of notebooks/papers/blogs to read from.

## Solution
Kaggle has many datasets to explore and well written code to learn from. I can pick a dataset/notebook randomly from there.

<br>

<br>

### Other problems/issues
I had this thought that, rather than just pushing and documenting the completed working code, I should also document and record the challenges and thought processes I had while doing it.
This can help me to reflect on possible ways to improve my process and understand why I do certain things.

- Initially wanted to do manual scraping on kaggle using either, request/html or selenium, to practice scraping
- However, I managed to find the [Kaggle API](https://github.com/Kaggle/kaggle-api) which I used instead as working with APIs is good practice too
- There was a problem that the API is for command line only 
  - Of course we could find ways to run shell commands in python however I wanted to try implementing my own functions
  - The method I can think of now is to go deeper into Kaggle's github and look at the source code
- I managed to get it to pull the kernels with the `kernels_list()` function
  - I can only get the name of the kernel, but I can't find a way to retrieve the url too

6/12/2020
- Turns out that the retrieved kernels from `kernels_list()` were actually `Kernel` objects which can be found [here](kaggle/models/kaggle_models_extended.py)
- We can retrieve the `ref` attribute of `Kernel` objects which can be appended behind the base url

8/12/2020
- Tried to encapsulate everything into a class `KernelList` so that I have a place to store the current selection
- Python's innate mutability makes me feel that I'm not employing "good" OOP principles
