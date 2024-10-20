def mysplit(s):
    print(s)
    tail = s.lstrip('0123456789')
    head = s[:(len(s)-len(tail))]
    return head, tail

def find_characters(matrix):

    dicNumbers={}

    for numbers in matrix:
        dicNumbers[(numbers)]= matrix.count(numbers)
    
    dicNumbers.pop("\n")
    result = [mysplit(s) for s in [''.join(sorted(''.join(str(key) for min_value in (min(dicNumbers.values()),) for key in dicNumbers if dicNumbers[key]==min_value)))]]

    return result[0][1]+""+result[0][0]