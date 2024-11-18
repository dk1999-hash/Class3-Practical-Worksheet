#
#COMP8270
#Programming for Artificial Intelligence
#Class 3
#The aim of this class is to continue practising data structures and loops in Python. To
#start, create a new Jupyter Notebook – you could name it ‘Class 3’. Each task provides a
#sample input values, but your solution must work with any input values.

#QUESTIONS:

#1. Write a Python code that, given a list of names, creates a dictionary where each name
#is grouped by the first letter. Your code should work for any list of names – e.g.:
#names = ["Jim", "Hetty", "Kirsten", "Theo", "Henry", "Paul"]
#grouped = {}
#"""
#dictionary grouping names based on the first letter
#"H" à "Henry", "Hetty"
#"J" à "Jim"
#"K" à "Kirsten"
#"P" à "Paul"
#"T" à "Theo"
#"""
#print(grouped)

#2. Given a dictionary, write a Python code that create a new dictionary where the keys are
#used as values and the values are used as keys – e.g.: "computer" à "apple" becomes
#"apple" à "computer" in the new dictionary. Your solution must work with any
#dictionary.
#my_dict = {"computer" : "apple", "model" : "macbook pro", "processor" : "M1
#Pro", "year" : 2021}
#inverted_dict = {}
# write logic here
#print(inverted_dict)

#3. * A simple way to implement a Dictionary like type is to use a list of lists: the first level
#determines the position of the element based on the “key”; the second level stores the
#value”. In order to determine the index of a particular “key” value, we can use the
#hash() function and apply the modulo operator to limit the value within the range of the
#list:
#key = "alan"
# assuming that our inner list has 10 positions
#index = hash(key) % 10
#Since there is a limited number of elements on the list, some of the “key” values will
#have a similar index. This is why each element of the list is another list: after
#determining the index where the value should be added, the value is added to the list
#at that index. The diagram below illustrates the process of adding the pair {"alan" :
#"7943" }:
#Using this approach, write a Python code that creates a list of lists that mimics a
#Dictionary. #Question1 
#names = ["Jim", "Hetty", "Kirsten", "Theo", "Henry", "Paul"]
#grouped = {}

#ANSWERS:
#Question1
for name in names:
    if name[0] not in grouped: #name[0] is the first element WITHIN the string
        grouped[name[0]]=[]
    grouped[name[0]].append(name)
    
    
print(grouped)

#Question2 swapping dictionaries from key value to value key
my_dict = {"computer" : "apple", "model" : "macbook pro", "processor" 
           : "M1 Pro", "year" : "2021"}
inverted_dict = {}
for key, value in my_dict.items():
    inverted_dict[value]=key
    
print(inverted_dict)

#Question 3 assessed
 
table = [[] for _ in range(10)]
index=hash("Deniz Korkmaz")%len(table)
table[index]=[]
table[index].append(["Deniz Korkmaz",99])
print(table)
