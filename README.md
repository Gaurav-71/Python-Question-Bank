# Python-Question-Bank
Solutions for fourth semester python lab internals

# Questions :-
1.		Write a Python function named numVowels that is passed a string containing letters, each of which may be in either uppercase or lowercase, and returns a tuple containing the number of vowels and the number of consonants the string contains.
2.		Write a python function stats() that takes name of text file as an argument. The function should print the number of lines, words, and characters in the file. For example,
>>>stats('example.txt')
Line count: 3
Word count: 20
Character count: 98
3.		Write function geometric() that takes a list of integers as input and returns True if
the integers in the list form a geometric sequence. A sequence a0, a1, a2, a3, a4, . . . ,an is a geometric sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3, . . . , an-1/anare all equal.
>>>geometric([2, 4, 8, 16, 32, 64, 128, 256])
True
>>>geometric([2, 4, 6, 8])
False
4.		Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long. For example, generate_n_chars(5,"x") should return the string "xxxxx“ using keyword only parameters.
5.		Write an interactive python program having a function called Initials() that takes input  representing a full name and returns the initials of the name in all capital letters. For example If Input: Robert B. Qwerty   then Output : RBQ
6.		Write a python function vowelCount() that takes a string as input and counts number of occurrences of each vowels in the string. For. Eg.
>>>vowelCount('Le Tour de France')
a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times
7.		Write a python program to read lines of input from the user, without giving a prompt. When the input line is quit, stop accepting input. As output, print the input lines in reverse order, one on each output line. The line quit should not be included in the output. Do not use the Python list reverse method.
Sample input and outputs are
Input :   hello world cse 326 32.545 ostrich quit 
Output: ostrich 32.545 326 cse hello world
8.		Write a python program to calculate the area of the circle and catch appropriate user defined exception.(Hint: check for invalid radius)
9.		Write function exclamation() that takes as input a string and returns it with this
modification: Every vowel is replaced by four consecutive copies of itself and an exclamationmark (!) is added at the end.
>>> exclamation('argh')
'aaaargh!'
>>> exclamation('hello')
'heeeelloooo!'
10.		Write a python function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?

11.		Write a python program to compute the area of geometrical objects and display the computed area.

12.		Create a dictionary program that initializes a set of items and prices for it. Add methods to 1) get the price of an item.    2) display all the items in sorted order
13.		Create a dictionary for words and their meanings. Write functions to add a new entry (word:meaning) ,search for a particular word and retrieve meaning, given meaning find words with same meaning , remove an entry, display all words sorted alphabetically. [Program must be menu driven]

14.		Write a function subsetSum() that takes as input a list of positive numbers and a positive number target. Your function should return True if there are three numbers in the list that add up to target. 
For example, if the input list is [5, 4, 10, 20, 15, 19] and target is 38, then True should be returned since 4+15+19 = 38. However, if the input list is the same but the target value is 10, then the returned value should be False because 10 is not the sum of any three numbers in the given list.
15.		Implement function partition() that splits a list of soccer players into two groups. More precisely, it takes a list of first names (strings) as input and prints the names of those soccer players whose first name starts with a letter between and including A and M.
>>>partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
Eleanor
Evelyn
Gavin
>>> partition(['Xena', 'Sammy', 'Owen'])
16.		Let list1 and list2 be two lists of integers.We say that list1 is a sublist of list2
if the elements in list1 appear in list2 in the same order as they appear in list1, but not necessarily consecutively.
>>>sublist([15, 1, 100], [20, 15, 30, 50, 1, 100])
True
>>>sublist([15, 50, 20], [20, 15, 30, 50, 1, 100])
False
17.		Initialize a list with odd numbers and even numbers. 
Write a function to count how many odd numbers is in a list and return the count.
18.		Implement function names() that takes no input and repeatedly asks the user to enter the first name of a student in a class. When the user enters the empty string, the function should print for every name the number of students with that name.
>>>names()
Enter next name: Valerie
Enter next name: Bob
Enter next name: Valerie
Enter next name: Amelia
Enter next name: Bob
Enter next name:
There is 1 student named Amelia
There are 2 students named Bob
There are 2 students named Valerie
19.		Given a list of integers, combine all integers to form a single integer.
Eg:  [1,25,32,4,5] ==> 1253245

20.		Write a for loop that iterates over a list of numbers lst and prints the numbers in the list whose square is divisible by 8. For example, if lst is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 4 and 8 should be printed.
