

input_number = int(raw_input("please enter a number\n "))
isPrime = False

if input_number < 2:
    isPrime = False
else:
    for index in range (2, input_number):
        if (input_number % index) == 0:
            isPrime = False
            break
        else:
            isPrime = True

#
if isPrime:
    print("This is a prime number")
else:
    print("This is not a prime number")
