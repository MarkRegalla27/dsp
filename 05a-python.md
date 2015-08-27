# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both hold large amounts of data as a single variable.  Lists are different from tuples in that lists are mutable, meaning the contents of the list can be changed (one datum swapped with another).  Tuples are immutable, which means that in order to change any datum, a new tuple must be made.

Tuples can be used as keys in dictionaries, as the key in a dictionary is also immutable.  You would not want to be able to change the key of a dictionary after it has been made and lose track of the value that it corresponded to.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets must have unique values, lists can have repeated values.  Sets are unordered, lists retain their order.  Finding values in a list references an index, values in a set must be hashable to be searched.

Lists can hold data generated from any application even if there are repeated values.  Sets could be used when there is a set and known amount of data to be collected and cannot have repeated values, such as the cards in a deck.

As the values of a set must be hashable, items can be found faster.  The hash function is faster than standard indexing.  Thus, searching a set is faster than searching a list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda is a function that is not bound to a name.  It can be written in 1 line for compactness yet perform an operation on a large amount of data (looping over it without for or while).  Also, a return statement is not needed as lambda always returns a value.

An example of the use of a lambda function:
```
x = ['1%', '2%', '3%', '4%', '5%']
x = map(lambda x: int(x.rstrip("%")), x)
x = [1, 2, 3, 4, 5]
#stips the '%' sign from each entry and converts the data to an integer data type
```
Lambda functions can be used in Python's sorted function as the key.  The key argument takes a function which acts on all elements of the list.  Here is an example that sorts mult-tiered data:

emp_tuples = [
        ('John', 'Sales', 45000),
        ('Jane', 'HR', 62000),
        ('Dave', 'Exec', 90000),
]
>>> sorted(emp_tuples, key=lambda employee: employee[2])   # sort by salary
[('Dave', 'Exec', 90000), ('Jane', 'HR', 62000), ('John', 'Sales', 45000)]

(https://wiki.python.org/moin/HowTo/Sorting)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A list comprehension is enclosed in brackets [] and generates a list of data using the function inside.  This helps cut down on the tedious task of typing in every number you need.  For instance, to generate a list of a few numbers counting by two, the list comprehension can be written:

theList = [2*x for x in range(10)]
print theList
>>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





