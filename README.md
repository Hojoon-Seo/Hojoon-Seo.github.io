# Hojoon Seo

# Welcome to my blog

## 2020/06/29

n = 30
number = n
for i in range(1,31):
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

This is my Fizz Buzz program. When a number is a multiple of 3, the program prints Fizz. When a number is a multiple of 5, the program prints Buzz. When a number is both a multiple of 3 and 5, the program prints Fizz Buzz. However, when a number is nor a multiple of 3 and 5, the program print the number. 