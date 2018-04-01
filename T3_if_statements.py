'''If , statements allows you to examine current state of the program and respond appropriately to that current state'''

#Simple example
def sample_1():             #don't pay attention to 'def' statement at this point
    print "\nSample_1"

    cars = ['audi', 'bmw', 'subaru', 'toyota']

    for car in cars:
        if car == 'bmw':
            print car.upper()
        else:
            print car.title()


'''If the conditional test evaluates to 'True', Python executes the code following the if statement.
If the test evaluates to 'False', Python ignores the code following the if statement.'''
def sample_2():
    print "\nSample_2"

    car = 'Audi'

    if car == 'audi':
        print "This is false"
    else:
        print "Two values with different capitalisation are not considered equal (Audi != audi)"


'''To check whether two conditions are both True simultaneously, use the keyword 'and' to combine the two conditional
 tests; if each test passes, the overall expression evaluates to 'True'. If either test fails or if both tests fail, 
 the expression evaluates to False .'''

def sample_3():
    print "\nSample_3"

    month = 9
    day = 6

    if month == 9 and day == 5:
        print "T1 is true"
    if month == 9 and day == 6:
        print "T2 is true"
    if month == 9 or day == 5:  #The keyword 'or' allows you to check multiple conditions as well, but it passes when
        print "T3 is true"      # either or both of the individual tests pass. 'or' expression fails only when both
    if month == 9 or day == 6:  # individual tests fail.
      print "T4 is true"
    if month == 8 or day == 5:
        print "T5 is true"


'''Checking whether a value is in a list- Using keyword 'in' 
    Checking whether a value is not in a list - using keyword 'not in' '''

def sample_4():
    print "\nSample_4"

    cars = ['audi', 'bmw', 'subaru', 'toyota']
    if 'audi' in cars:
        print "audi is present in cars list"
    if 'maruti' not in cars:
        print "maruti is not present in cars list"


'''An 'if-else' block is similar to a simple if statement, but the else statement allows you to define an action
 or set of actions that are executed when the conditional test fails - Refer sample_1'''

# At this point don't pay attention to codes below this line
sample_1()
sample_2()
sample_3()
sample_4()
