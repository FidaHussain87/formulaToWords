#### this dictionary has operators as key and their translation into words as value pair
operators = {
    "+": "plus",
    "-": "minus",
    "*": "multiply by",
    "/": "divided by",
    "=": "equals to"
}

##### this numbers array has digits as key and translation into words a value pair
numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety',
    100:"Hundred",
    0: 'Zero'
}


#### this function is used to convert any number between 0-90 into words,

def convertNumber2Word(n):
    n = int(n)
    #### try block inorder to catch an error if number doesn't exist in numbers dictionary.
    try:
        return ""+numbers[n]
    
    #### except block incase if we are catching the error in above try block as a KeyError, let say if we insert the number other than integer, i.e a,b,c....z
    #in that case we don't want to break the code but to catch that error and return just false, if we have any number which is not in numbers array like 100,101,
    # then it will return false in except block having Error type as KeyError
    except KeyError:
        try:
            return ""+numbers[n - n % 10] + numbers[n % 10].lower()
        except KeyError:
            return False


# In this method we are supposed to take an input math formula based on numbers as a string from user between
# 0-9, and operators as given in operators dictionary above, and then we are looping over the string formula,
# and checking if it's digit operator or small brackets, based on each condition we are saving result into output variable,
#while parsing numbers into  above function convertNumber2Word to get translation, 
# and getting repsective operators with index

def main():
  output = ''
  result = ""
  number=''

  try:
    ### getting input from user i.e 2+3*(2+4)-4/2 as a string
    formula = input("Please enter your math formula to solve?")
    #### using eval built-in method to take math formula as a string and give an output as a final result
    answer = eval(formula)
    #while loop inorder to ask the user to input formula if the result exceeds 100
    while answer>100:
      formula = input("Please enter your math formula to solve?")
      answer = eval(formula)
    ### converting the answer number into words
    result = convertNumber2Word(answer)
    ### using loop to iterate over each number into string formula
    for i in formula:
        if i == "(":
            output = output+"("+" "
        elif i == ")":
            output=output+convertNumber2Word(number)+" "
            number=""
            output = output+")" + " "
        elif i in operators:
            if number !='':
              output=output+convertNumber2Word(number)+" "

            output = output + operators[i]+" "
            number=''
        else:
          number=number+i
    if not result:
        print('Number out of range')
    else:
        output = output + convertNumber2Word(number)
        print(output+" "+operators["="]+" "+str(result))
  except Exception as e:
    print(e)


#### calling the main method ############
main()





