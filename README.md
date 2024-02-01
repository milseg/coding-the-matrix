# Coding the matrix solutions

Programming labs solutions for Philip N. Klein's textbook 'Coding the Matrix: Linear Algebra through Computer Science Applications’

Code written using Python 3.6.0 on Ubuntu 22.04 over `[wsl](https://learn.microsoft.com/pt-br/windows/wsl/)` 

Each chapter’s work is setup within a folder with a number indicating the sequence in which the chapter appear plus the chapter name using underscores to separate words
`[n]_[chapter_underscore_convention]`

So folder **1_The_Function** is referred to programming labs contained in the chapter **The Function**, which is the first(number one) to appear in the book.

Generally, the main files for the chapter has the same name of the chapter followed by the word problems. **i. e.** Folder **1_The_Function** contains the main file **The_Function_problems.py.** Other core solution files are named with ****the title of the corresponding lab

# Comments

- Solution for **problem 11.8.6** isn’t implemented in this repo
- Solution for optional **task 12.12.8** isn’t implemented in this repo, but can easily be deducted by the solutions for tasks right before it.
- Instead of separating code for **tasks 13.13.1 to 13.13.5**, a single block solves all of that range and is implemented on the file `[The_Linear_Program_learning.py](14_The_Linear_Program/The_Linear_Program_learning.py)`
- Each chapter lab is isolated into a folder which required me to copy auxiliary files repeatedly. I plan to replace this approach moving these files to a single folder and setting them up into python modules search path. Observations about the core files naming are stated in the previous section to help you find the relevant code
- Although python current version is above from 3.6, solve module used between the labs will require a lower version. I recommend you using `[pyenv](https://github.com/pyenv/pyenv)` to manage older python installations.
- File 13_The_Eigenvector/data/inverseindex has been removed from commit history because of github file size constraint. You can find it at `[resources](http://resources.codingthematrix.com/inverseindex)`
- It is rewarding to solve this book labs. It would give you a new perspective beyond the abstract and theoretical math lessons you could have elsewhere. I recommend!

# References

- http://resources.codingthematrix.com/
- http://grading.codingthematrix.com/edition1/index.html
- http://resources.codingthematrix.com/images/
- http://resources.codingthematrix.com/matrix_resources/images/
- https://realpython.com/intro-to-pyenv/
