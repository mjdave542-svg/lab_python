#1.Square of no.

def square(num,ex=2):
    return num**ex

print(square(5))
print(square(5,3))
print(square(2,4))

#2.
def greet(name="Guest"):
    print("Hello",name)

greet("Alice")
greet()

#3.
def add(a,b=5):
    print("Sum:",a+b)

add(10,20)
add(10)