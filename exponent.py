# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 15: Write a function called exponent (base, exp) that  returns an int value of base raises to the power of exp.

base = int(input("Enter a base number: "))
exponent = int (input("Enter an exponent number: "))

def power (base, exponent):
    answer = 1

    for _ in range (exponent):
        answer *= base
    
    return answer

answer = power (base, exponent)

print ("Base:", base, "and Exponent:", exponent)
print ("The answer is: ", answer)

