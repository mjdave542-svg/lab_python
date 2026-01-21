#Q-1
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)


#Q-2
for i in range(1, 6):
    print(i)
 
    
#Q-3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Maximum =", a)
else:
    print("Maximum =", b)


#Q-4
s = input("Enter a string: ")
print("Length of string =", len(s))


#Q-5
print("Welcome to Python Programming")


#Q-6
s = input("Enter a string: ")
print("First character =", s[0])


#Q-7
s = input("Enter a string: ")
print("Last character =", s[-1])


#Q-8
n = int(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")


#Q-9
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum =", a + b + c)


#Q-10
n = int(input("Enter a number: "))
print("Square =", n * n)

