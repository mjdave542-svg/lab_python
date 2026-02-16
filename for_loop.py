#1.Print Numbers from 1 to 5
for i in range(1, 6):
    print(i)    

#2.Print a message 3 times
for i in range(3):
    print("Hello, World!")

#3.Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


#4.Print even numbers from 1 to 20
for i in range(1, 21):  
    if i % 2 == 0:  
        print(i)


#5.print odd numbers from 1 to 20
for i in range(1, 21):  
    if i % 2 != 0:  
        print(i)


#6.Print Table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


#7.Print characters of a string
name= "Hello"
for letter in name:
    print(letter)


#8.Sum of numbers from 1 to 5
total = 0
for i in range(1, 6):
    total += i
print("Sum of numbers from 1 to 5:", total)

#9.Print List Elements

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)