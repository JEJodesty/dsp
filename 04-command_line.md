*# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

---CHEAT SHEET---

* pwd - print working directory 
* hostname - my computer's network name
* mkdir - make directory 
  * 'mkdir -p <dir path>' (*)
  * mkdir "I Have Fun" (*)
* rmdir - remove directory
* cd - change directory 
  * 'cd ~' - takes you to your home directory (*)
* ls - list directory 
  * 'ls -1R' takes tou to a "leaf" directory (*)
  ls <dir/> - lists items in referenced dir (*)
* pushd - push directory (*)
  *In Linux/Unix 'pushd', if you run it by itself with no arguments, will switch between your current directory and the last    one you pushed. 
  *It's an easy way to switch between two directories.
* popd - pop directory (*)
* cp - copy a file or directory - 'cp iamcool.txt neat.txt' (*)
  * cp awesome.txt something/ - copy file into directory (*)
  * cp -r - to copy more directories with files in them. (*)
    * 'cp -r something newplace' - make a new directory and copy a file into that directory
* mv - move a file or directory OR rename a file (*)
* less - page through a file
* cat - print the whole file - 'cat <file.txt> <file2.txt>' concatinates texts of both files
* xargs - execute arguments [build and execute command lines from standard input] (*) (See below)
* find - find files
* grep - find things inside files
* man - read a manual page
* apropos - find what man page is appropriate
* env - look at your environment
* echo - print some argumentss
* export - export/set a new environment variable
* exit - exit the shell
* sudo - DANGER! become super user root DANGER! (*)
* touch - make an empty file '$ touch iamcool.txt' (*)
* rm - remove (delete) a file - 'rm <file>' or 'rm something/awesome.txt' 
  * 'rm -rf newplace' - rm directory with files in it


---Notes---
* Put a / (slash) at the end of a directory to make sure the file is really a directory, 
* so if the directory doesn't exist you'll get an error.
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

* 'ls' lists out the contents of the directory you are currently in
* 'ls -a' - reveals "hidden" current ('.') or parent ('..') directories 
* 'ls -1h' - displays contents of directory in long list format
* 'la -1h -a' in meaningfull because it lists directories in long list format 
  * and includes "hidden" current ('.') or parent ('..') directories 

---


---

What does `xargs` do? Give an example of how to use it.

* xargs - build and execute command lines from standard input  
---Example 1--- 
* I can use it to compress multiple files of paticular types into a .tgz file

Joshua@joshej07 ~/xargsExample
$ ls 
* file1.jpg
 file1.pdf
 file1.txt
 file2.jpg
 file2.pdf
 file2.txt
 file3.jpg
 file3.pdf
 file3.txt
 file4.jpg
 file4.pdf
 file4.txt
 file5.jpg
 file5.pdf
 file5.txt

Joshua@joshej07 ~/xargsExample
$ find . -maxdepth 1 -name "*.jpg" | xargs tar -czvf jpeg.tgz
./file1.jpg
./file2.jpg
./file3.jpg
./file4.jpg
./file5.jpg

Joshua@joshej07 ~/xargsExample
$ tar -tzf jpeg.tgz
./file1.jpg
./file2.jpg
./file3.jpg
./file4.jpg
./file5.jpg

Joshua@joshej07 ~/xargsExample
$ ls
file1.jpg  file1.txt  file2.pdf  file3.jpg  file3.txt  file4.pdf  file5.jpg  file5.txt
file1.pdf  file2.jpg  file2.txt  file3.pdf  file4.jpg  file4.txt  file5.pdf  jpeg.tgz

>---Example 2---

Joshua@joshej07 ~/xargsExample
$ echo {1..15}
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

Joshua@joshej07 ~/xargsExample
$ echo {1..15} | xargs -n5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15


---
