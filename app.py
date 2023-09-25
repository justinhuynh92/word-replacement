#create function to replace word
def replace_word():
    #assign str variable to the sentence we're going to work off of
    str = "hi guys, i'm justin and it's a good day today."
    #create variables for the word we want to replace
    word_to_replace = input("enter the word to replace: ")
    #create the word that's going to replace the original word
    word_replacement = input("enter the word replacement: ")
    #print the word you want to replace with replace method
    print(str.replace(word_to_replace, word_replacement))
#call the function
replace_word()
