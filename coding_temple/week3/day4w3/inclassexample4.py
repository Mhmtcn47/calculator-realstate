#Question: Write a function count_words that takes a string as input and returns a dictionary that maps each word in the string to the number of times it appears.
#For example, if the input string is “to be or not to be”, the function should return the dictionary {“to”: 2, “be”: 2, “or”: 1, “not”: 1}.
# Also, if the input string contains any contractions (e.g. “it’s”, “don’t”), treat them as separate words for counting purposes (e.g. “it’s” should be counted as “it” and “’s”).


import re
# input: a string with words separated by spaces
# output: a dictionary with key = unique words in input, and value = count of times
# unique words appear
# define function(inputString)
    # turn string into list with split
    # initialize empty dictionary
    # for each ele in inputString
        #if element is not in dictionary
            # add element as key to dictionary
            # set value of element to 1
        # else:
            # increment that key's value by 1
    # return dictionary
test_string = "it's to be or not to be"
def count_words(aString):
    aString = aString.lower().split()
    newString = []
    for ele in aString:
        if "'" in ele:
            tempEle1 = ele[0:ele.index("'")]
            tempEle2 = ele[ele.index("'")+1:len(ele)]
            print("ele1: ", tempEle1," ele2: ", tempEle2)
            newString.append(tempEle1)
            newString.append(tempEle2)
        else:
            newString.append(ele)
    the_answer = {}
    for ele in newString:
        if ele not in the_answer:
            the_answer[ele] = 1
        else:
            the_answer[ele] += 1
    return(the_answer)
print(count_words(test_string))



