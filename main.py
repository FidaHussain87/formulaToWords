operators = {
  "+": "plus",
  "-": "minus",
  "*": "multiply by",
  "/": "divided by",
  "=": "equals to"
}
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
  0: 'Zero'
}


def convertNumber2Word(n):
  n = int(n)
  try:
    return ""+numbers[n]
  except KeyError:
    try:
      return ""+numbers[n - n % 10] + numbers[n % 10].lower()
    except KeyError:
      print('Number out of range')


def solveProblem():
  result = ''
  formula=input("Please enter your math formula to solve?")
  answer=eval(formula)
  for i in formula:
    if i.isdigit() and i is not None:
      result=result+convertNumber2Word(i)+" "
    elif i == "(":
      result=result+"("+" "
    elif i==")":
      result=result+")"+ " "
    else:
      result = result + operators[i]+" "
  print(result+" "+operators["="]+" "+str(convertNumber2Word(answer)))
  

solveProblem()



