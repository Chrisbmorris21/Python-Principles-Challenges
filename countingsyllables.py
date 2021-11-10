string = "met-a-phor"

def count(string):
    metaphor = 1
    for i in range(len(string)):
        if string[i] == "-":
            metaphor = metaphor + 1
    return int(metaphor)
            
    
