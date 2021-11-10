#CHALLENGE
#Take a string, return it as an array with the keys of each uppercase letter.
#e.g. HeLlO should return 0,2,4
#e.g. ChiCKeN should return 0,3,4,6

#Thought process
#Get length of string
#Create empty array to store keys
#Split string, iterate throguh each character, check if its upper or lower
#If capital, append value to empty array
#Return completed array
#test function

def capital_indexes(string):
    
    characterArray = []
    x = string.split()
 
    for i in range(len(x)):
        y = str(x[i])
        for i in range(len(y)):
            if y[i].isupper():
                characterArray.append(i)
                
        return(characterArray)

print(capital_indexes("HeLlO"))
