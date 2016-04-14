Number Sense Generator Program
==============================

About
-----

This program is made for the Dulles High School UIL Number Sense team. The main code is written in Python and the test generated is written in a LaTeX format that must be compiled separately. When run, the program generates a test used mainly for practice purposes and should not be mistaken for one that generates a realistic test. The writer does not have any affiliation with the University Interscholastic League.

In order to run it, download the files, open a terminal with Python loaded on it, and move to the project directory. Once you are there, type <code>python NumberSenseGenerator.py</code> and a file called "test.tex" would have been generated. Copy the file data and paste it into a LaTeX compiler to create a pdf of the Number Sense Test.

Editing the Program
-------------------

In order to add another trick, write a method in the "Trick Definitions" area that takes no parameters and returns a two-membered array of strings, the first one being the question and the second one being the answer. Both support LaTeX formatting. Once you have done this, increase the number of tricks in the "Important Constant Definitions" area. Finally, add another <code>elif</code> in the "Question Iterator." For example, if your new trick is called "approximation," and it is the 9th trick in the list, then create a method <code>approximation()</code>, let <code>numTricks = 9</code>, and add the conditional <code>elif (k == 8)</code> to the Iterator. For the body of the conditional, just mimic what is in the rest of the conditionals. 

While this is optional, it is highly recommended that you add the trick you created to the README.

Current Tricks
--------------

1. FOIL
2. Addition
3. Polygonal Numbers
4. Whole Number Times Fraction
5. Number of Divisors