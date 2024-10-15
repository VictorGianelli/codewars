def spin_words(sentence):
    # Vars
    words= []
    finalSentence = ''
    
    # Splitng words
    words = sentence.split(" ")
    for i in words:
        # Return reverse word if length in up to 5 letters 
        if len(i) >= 5:
            i = i[::-1]
            
        # Building the answer    
        finalSentence = finalSentence + " " + i    

    return finalSentence.lstrip() # <- Remove space from begin