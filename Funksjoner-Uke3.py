
def multiply():
    print "Multiplication"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) * int(y)
    print sum
    return


def pluss():   
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) + int(y)
    print sum
    return


def subtract(): 
    print "subtract"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) - int(y)
    print sum
    return

def divide():   
    print "divide"
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = int(x) / int(y)
    print sum
    return

divide()



calc = raw_input('What operator do you want to use? ')

if calc == 'multiplication':
    multiply()
elif calc == 'subtraction':
    subtract()
elif calc == 'addition':
        pluss()  
elif calc == 'divide':
    divide()

