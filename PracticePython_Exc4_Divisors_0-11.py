number = int(raw_input("Enter a number between 0 and 11 to find its list of divisors: "))
x = []
for divisor in range (1, 11):
    if number % divisor == 0:
        answer = int(divisor)
        x.append(answer)
print x


#finding list of divisors up to 10.
