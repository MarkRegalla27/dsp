# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. pipe |: Sits between two commands.  The output from the first command gets channelled into the command of the second command.
2. touch: Creates new file.  Give it the extension of your choosing.
3. less: view contents of file. w and spacebar scrolls through file
>>: Append command.  Appends the command to the left of the sign to the command or file to the right of the sign.
5. man [command]:  Gives help about the command following 'man' 
6. apropos: (Very worth remembering) Suggests relevant commands if you forget the name but know what it does
7. cat: Stream contents of a file in the current directory as output on the command line
8. open '/file': This command is not listed in the command line crash course.  I found it by trying it.  And it works.  It opens the file.  Pretty self-explanatory.
9. grep: Searches for specified contents in chosen file
10. pushd:  Saves the current directory that you are in and changes to a new one temporarily
11. -i: ignores case of letter when searching within files using grep command
12. seq (number): Prints a sequence starting from 1 up to the number entered

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls: Lists the files and folders in a directory.
ls -a: Lists all files and folders in given directory, even hidden ones
ls -l: Lists the contents of a directory along with information regarding whether it is a directory or file, the date and time the file or directory was created, and the size of the file or directory.
ls -lh: Lists the same details as ls -l but in human readable form (adds units to the size of files/folders)

---


---

What does `xargs` do? Give an example of how to use it.

xargs allows for performing multiple commands in a single statement and loop over multiple objects in the directory.  It takes the output of the first command as an argument which it passes to the second command (placed after xargs, called the utility command).  (Note: the default command if none is specified after xargs is echo.)

An example of a usage of xargs:
```
The command "seq 5 | xargs -n1 echo "Banana Count:"" prints the words "Banana Count" over the number of times the sequence command prints.  Here is the output:
Banana Count: 1
Banana Count: 2
Banana Count: 3
Banana Count: 4
Banana Count: 5
```
This is just a rough example that falls short of demonstrating the full power of xargs.  I still need to get more practice with it.

---

