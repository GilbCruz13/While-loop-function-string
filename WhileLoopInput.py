# Created a function that will return "?" If the startin word uses "How, When, Why" else it will return "."

def sentence (phrase):
    questions = ("how","when","why","what","whats")     
    capitalized = phrase.capitalize()
    if phrase.startswith((questions)):  
        return "{}?".format(capitalized) 
    else:
        return "{}.".format(capitalized)

#create a list "[]" to assign various items, and use that list in the While loop
result = []
while True:
    x = input("Say Something: ")
    if x == "\end":
        break
    else:
        result.append(sentence(x)) #<--------- Add(.append()) the fucntion named sentence and assing the parameter "x".

print(" ".join(result)) # <----- The output will show as a string instead of a list
 