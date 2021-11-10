# Python-Principles-Challenges
My attemps at the Python Principles code challenges

## Challenge 1 ##
*Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters. For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].*


Firstly I take a look at the non-negotiables of what is being asked. What parameters must I pass, and what must I return?
The non-negotiables in this case is 
* The function needs to be called **capital_indexes**
* It can only take a **single parameter** and that must be a **string**.
* It should return a **list** of all **indexes** that have capital letters.

By analysing a question in such a way, a lot of the work around the structure is already done for me. It also makes it easy for me to break down anything I may need to look up in the future. I will always attempt to learn or incorporate something new in every challenge.

```python
def capital_indexes(string):
  characterArray = []
```
The above code declares my function in the way it is asking. I personally like to name my parameters the type of variable that it will be handling when there is only one, as long as it isn't a reserved word / keyword.

```python
  x = string.split()
```

This line will take the string and convert it to a single entity list that I can get the length from. In my head I knew I wanted to build in the ability later on to take an entire sentence and output the uppercases. So this seemed like a good way to introduce this so I can fork from it at a later time.

```python
for i in range(len(x)):
  y = str(x[i])
```

For every **key** that exists as **i** for the length, **x**, of our list, we will assign that keys repersentative **value** to **y**

```python
  if y[i].isupper():
```

If **y** is an uppercase letter

```python
characterArray.append(i)
```

Add to the end of our predefined array its key

```python
return(characterArray)
```
Return the characterArray so if called as a method with print, it will output our array as described

```python
print(capital_indexes("HeLlO"))
```

The Test Code
