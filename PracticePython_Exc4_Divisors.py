number = float(raw_input("Enter a number to find its list of divisors: "))
divisor = 0
while number > 0:
    divisor = divisor + 1
    if number % divisor == 0:
        answer = divisor
        print answer

#finding list of all divisors no matter the user input quantity
