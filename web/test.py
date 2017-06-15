# -*- encoding: utf-8 -*-
import random

a=1
b=10
number = random.randint(1, 10)
counter = 0

if __name__ == '__main__':
    print "Guess the Secret Number Game (between {} and {} You have 3 tries!)".format(a,b)
    print "*" * 40
    print
    while counter < 3:

        print "Current Try: {}".format(counter)
        print "-" * 20
        try:
            variable = raw_input()
            variable = float(variable)
        except:
            print "Error. Not a correct number. Try again"
            continue

        if variable == number:
            print "\n You did it. Congratulations!\n"
            quit()

        elif variable > number:
            print "Your Guess is higher than the number\n"
            counter += 1

        else:
            print "Your Guess is lower than the number\n"
            counter += 1

        # if too many tries, final loop:
        if counter == 3:
            print "You lost. Thank you for playing"
