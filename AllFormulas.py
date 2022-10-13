#!/usr/bin/env python3
#!/usr/bin/python

userName = input('Who is this? ')
print('Hi, ' + userName)
print("Try this calculator!")

x, y = [float(x) for x in input("Enter two values: ").split()]

#print("Enter numbers with a space between each: ")
#numberList = list(map(float, input().split()))

#addition
print("   ~~Addition~~")

additionMessageOne = "If you add "
additionMessageTwo = x
additionMessageThree = "by "
additionMessageFour = y
additionMessageFive = "the answer is: "
additionAnswer = x + y

print(additionMessageOne, additionMessageTwo, additionMessageThree, additionMessageFour, additionMessageFive, additionAnswer)

#subtraction
print("   ~~Subtraction~~")

subtractionMessageOne = "If you subtract "
subtractionMessageTwo = x
subtractionMessageThree = "by "
subtractionMessageFour = y
subtractionMessageFive = "the answer is: "
subtractionAnswer = x - y

print(subtractionMessageOne, subtractionMessageTwo, subtractionMessageThree, subtractionMessageFour, subtractionMessageFive, subtractionAnswer)

revsubtractionMessageOne = "If you subtract "
revsubtractionMessageTwo = y
revsubtractionMessageThree = "by "
revsubtractionMessageFour = x
revsubtractionMessageFive = "the answer is: "
revsubtractionAnswer = y - x

print(revsubtractionMessageOne, revsubtractionMessageTwo, revsubtractionMessageThree, revsubtractionMessageFour, revsubtractionMessageFive, revsubtractionAnswer)

#multiply
print("   ~~Multiplication~~")

multiplicationMessageOne = "If you multiply "
multiplicationMessageTwo = x
multiplicationMessageThree = "by "
multiplicationMessageFour = y
multiplicationMessageFive = "the answer is: "
multiplicationAnswer = x * y

print(multiplicationMessageOne, multiplicationMessageTwo, multiplicationMessageThree, multiplicationMessageFour, multiplicationMessageFive, multiplicationAnswer)

#division
print("   ~~Division~~")

divisionMessageOne = "If you divide "
divisionMessageTwo = x
divisionMessageThree = "by "
divisionMessageFour = y
divisionMessageFive = "the answer is: "
divisionAnswer = x/y

print(divisionMessageOne, divisionMessageTwo, divisionMessageThree, divisionMessageFour, divisionMessageFive, divisionAnswer)

#reverse division
revdivisionMessageOne = "If you divide "
revdivisionMessageTwo = y
revdivisionMessageThree = "by "
revdivisionMessageFour = x
revdivisionMessageFive = "the answer is: "
revdivisionAnswer = y/x

print(revdivisionMessageOne, revdivisionMessageTwo, revdivisionMessageThree, revdivisionMessageFour, revdivisionMessageFive, revdivisionAnswer)

print("Have a great day!")