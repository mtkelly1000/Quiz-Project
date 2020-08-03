
answercombo = {
  'AAA':'Maddy',
  'ABA':'Trevor',
  'AAB':'Matte',
  'ABB':'Eli'
}


j = input('hello! What is your name?')
print ('nice to meet you, ' + j)

quit= 'y'
while quit == 'y':
  Q1 = input ('What is your favorite color? \nA) blue \nB) red')
  Q2 = input ('What is your favorite dessert? \nA) cake \nB) ice cream ')
  Q3 = input ('what is your favorite animal: \nA) cat  \nB) dog')
  code = Q1+Q2+Q3
  if code in answercombo:
    print ('you are '+ answercombo.get(code))

  quit = input ('do you want to continue? (y/n)')
