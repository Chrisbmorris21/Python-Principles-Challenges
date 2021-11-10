#Middle letter
#Write a function named mid that takes a string as its parameter.
#Your function should extract and return the middle letter.
#If there is no middle letter, your function should return the empty string.
#For example, mid("abc") should return "b" and mid("aaaa") should return "".


string = "chickenss"

def mid(string):
    x = len(string)
    if x % 2 == 0:
        return ""
    else:
        x = x - 1
        x = int(x / 2)
        return string[x]
    
print(mid(string))

