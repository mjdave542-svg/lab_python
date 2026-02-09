#1.vote
age=int(input("enter your age:"))
if age>=18:
    print("yes,you are eligible for vote...!!")
else:
    print("no,you are not eligible for vote...!!")
    
#2.mark
marks=int(input("ebter your marks:"))
if marks>=90:
    print("you get A grade.")
elif marks>=70:
    print("you get B grade")
else:
    print("you get C grade")
    
#3.odd/even
number=int(input("enter the number:"))
if number % 2==0:
    print("the number is even")
else:
    print("the number is odd")
    
#4.positive or negative
number=int(input("enter the number:"))
if number > 0:
    print("the number is positive")
else:
    print("the number is negative")
    
#5.license eligible
num=int(input("enter the number:"))
if num >=18:
    print("yes,you are eligible for driving licence..!!")
else:
    print("sorry,you are not eligible for driving licence")