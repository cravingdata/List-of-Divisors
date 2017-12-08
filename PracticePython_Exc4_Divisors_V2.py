number = int(raw_input("Enter a number to find its list of divisors: "))
x = []
for divisor in range (1, (number +1)):
    if number % divisor == 0:
        answer = int(divisor)
        x.append(answer)
print x

#version 3 for finding list of all divisors for user input.
