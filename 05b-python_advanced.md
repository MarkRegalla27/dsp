## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  

Use regular expressions to:

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
```
There are 1 personnel with the degree "MD".
There are 1 personnel with the degree "MA".
There are 6 personnel with the degree "ScD".
There are 1 personnel with the degree "BSEd".
There are 31 personnel with the degree "PhD".
There are 1 personnel with the degree "0".
There are 2 personnel with the degree "MPH".
There are 2 personnel with the degree "MS".
There are 1 personnel with the degree "JD".
```

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor
```
There are 11 personnel with the title "Assistant Professor of Biostatistics".
There are 13 personnel with the title "Professor of Biostatistics".
There are 1 personnel with the title "Assistant Professor is Biostatistics".
There are 12 personnel with the title "Associate Professor of Biostatistics".
```

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
```
['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']
```

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
```
There are 12 personnel with the email domain "@upenn.edu".
There are 1 personnel with the email domain "@email.chop.edu".
There are 1 personnel with the email domain "@cceb.med.upenn.edu".
There are 23 personnel with the email domain "@mail.med.upenn.edu".
```
Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:
```
[(['Bellamy'], [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']), (['Bilker'], ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']), (['Bryan'], [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'])]
```

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:
```
[(['Matthew', 'W', 'Bryan'], [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']), (['Scarlett', 'L.', 'Bellamy'], [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']), (['Warren', 'B.', 'Bilker'], ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'])]
```
####Q8.  It looks like the current dictionary is sorted by first name.  Sort by last name and print the first 3 key and value pairs.  
```
[(['Scarlett', 'L.', 'Bellamy'], [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']), (['Warren', 'B.', 'Bilker'], ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']), (['Matthew', 'W', 'Bryan'], [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'])]
```
Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

