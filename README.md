# Python-Principles-Challenges
My attemps at the Python Principles code challenges

## Challenge 1 ##
# Capital Indexes #
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



## Challenge 2 ##
# Middle letter #
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string. For example, mid("abc") should return "b" and mid("aaaa") should return "".*

Non negotiables against! First we must
* create a function named mid
* takes a string as a parameter
* take the middle letter and return it
* return empty string if no middle

Right so thought process is as follows:
* is the string an odd or an even number? 
* if even, how can we can bypass everything and return an empty string?
That will be an entire side of the conditional already done so we will do that first.


```python
def mid(string):
    x = len(string)
    if x % 2 == 0:
        return ""
 ```
 
 The above chunk of code defines the function and passes the paramater of string. We assign the length of the string to the variable **x**. The conditional checks if there are any numbers after the decimal when divided by two. If there are no numbers beyond the decimal, we can assume the number is even. I have set the conditional branch to return "" where the condition for the length being even is true as has asked by the brief.


To get the middle number, i can use this formula:
 
 ### (x - 1) / 2 = key in array ###
 
 For example:
 
```
[0][1][2][3][4] 
5 - 1 = 4
4 / 2 = [2]
```
 
```
[0][1][2][3][4][5][6][7][8]
9 - 1 = 8
8 / 2 = [4]
```

Our second chunk of code is very simple, we will work with the same variable for brevity.

```python
    else:
        x = x - 1
        x = int(x / 2)
        return string[x]
```
This chunk of code takes the length of the string and applies the above calculations to it. it will return the key we need to access the character of the string. it then returns the value assigned to that key on return.

## Challenge 3 ##

# Online status #
*The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online. For example, consider the following dictionary:*

```python
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
```

*In this case, the number of people online is 2. Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above. Your function should return the number of people who are online.*

I will want to create a function which iterates through the dictionary adding one to an int, and then return int at the end.

```python
def online_count(statuses):
    
    countOnline = 0
    
    for key in statuses:
```

Defines the functions and assigns value from dicitionary to key while it iterates

```python
if statuses[key] == "online":
            countOnline = countOnline+1
```
Gets paired data and determines wether it is online or not, if it is online add one to our int tracking the online number


```python
    return int(countOnline)

online_count(statuses)
```
Return the int and call the function to test it with our test dictionary named statuses




## Challenge 4 ##
# Randomness #
*Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.*

*Calling the function multiple times should (usually) return different numbers.*

*For example, calling random_number() some times might first return 42, then 63, then 1.*
