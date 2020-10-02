#User enters a number between 1 and 100
#FizzBuzz program starts to count to that number (it prints them in the Terminal). In case the number is divisible with 3, it prints "fizz" instead of the number. If the number is divisible with 5, it prints "buzz". If it's divisible with both 3 and 5, it prints "fizzbuzz".

print("Hi, this is FizzBuzz game.")

end = int(input("Please choose a number between 1 and 100. "))

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)