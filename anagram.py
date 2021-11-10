def is_anagram(string1, string2):

    string1 = sorted(string1)
    string1 = "".join(string1)

    string2 = sorted(string2)
    string2 = "".join(string2)

    if string1 == string2:
        #print("True")
        return True

    else:
        #print("False")
        return False

is_anagram("Hello", "Hello")
    
