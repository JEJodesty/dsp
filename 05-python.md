# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* Similarities: "lists" and "tuples" 
  * Both are sequences of values, that are indexed by integers, and can be any type.
* Differences: "lists" and "tuples"
  * "lists" are mutable, and "tuples" are immutable.
* Tuples will work as keys in dictionaries because tuples are immutable (can't be changed), which is necessary for the mapping of keys to values for the key-value pairs.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

* Differences: WHat lists aren't or can't do.
 * Only sets can't contain duplacates and are unordered.
 * When a single strng is a set argument, the charaters are split
 * Can perform unions, intersetions, etc. on sets
* Example: List
 * >>> a = range(1, 20)
 * >>> a
 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
* Example Set A:
 * >>> basket = ['apple', 'orange', 'kale', 'apple', 'pear', 'orange', 'lettuce', 'banana']
 * >>> fruit = set(basket)
 * >>> fruit - veg
 * >>> veg = set(['kale', 'lettuce'])
 * >>> fruit - veg
 * set(['orange', 'pear', 'apple', 'banana'])
*Example Set B:
 * >>> nums = [1, 2, 3, 4, 6, 8, 10]
 * >>> numset = set(nums)
 * >>> oddset = set([1, 3, 5, 7, 9])
 * >>> oddset = set([1, 3, 5, 7, 9])
 * >>> numset | oddset
 * set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
* Performance Compare: Sets are significantly faster when it comes to determining if an element is in the set (as in x in s), but are slower than lists when it comes to iterating over their contents. [timeit]

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

* `lambda` is shorthand to create an anonymous function (a function without a name or deffenition); the expression 'lambda arguments: expression' yields a function object. The unnamed object behaves like a function object
* Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. More specifically, it can be used when you don't really want to define a function with a name, possibly because that function will only be used one time and not numerous times.
* Example: Look familiar? :bowtie: 
 *   Returns a list sorted in increasing order by the last element in each tuple
 *   >>> sorted([(1, 7), (3, 4, 5), (2, 2), (5, 6, 10), (1, 3)], key=lambda x: x[-1])

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

* List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
* Big Eaxample (`map` & `filter`): Comparison - `map` & `filter` doesnt need loops in this example
 * >>> a = range(1, 20)
 * >>> a
 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
 * >>> b = []
 * >>> for i in a:
 * ...   b.append(i*2)
 * ...
 * >>> b
 * [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
 * >>>
 * >>> def double(x):
 * ...   return x * 2
 * ...
 * >>> map(double, a)
 * [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
 * >>>
 * >>> def is_even(x):
 * ...   return x % 2 == 0
 * ...
 * >>> is_even(2)
 * True
 * >>> is_even(3)
 * False
 * >>>
 * >>> filter(is_even, a)
 * [2, 4, 6, 8, 10, 12, 14, 16, 18]
* Example (Set Comprehention)
 * >>> x = set([2, 4, 6, 8])
 * >>> type(x)
 * <type 'set'>
 * >>> y = {n*3 for n in x}
 * >>> y
 * set([24, 18, 12, 6])
* Example: Dictionary Comprehention
 * >>> {key: value for (key, value) in enumerate('bigdata')}
 * {0: 'b', 1: 'i', 2: 'g', 3: 'd', 4: 'a', 5: 't', 6: 'a'}
 
---
---

Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
