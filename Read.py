#1.Read()

f=open("one.txt", "r") 
data=f.read()
print("First Data",data)
f.close()

#2.Readline()

f=open("one.txt","r")

line1=f.readline()
line2=f.readline()
line3=f.readline()

print("Line 1:",line1)
print("Line 2:",line2)
print("Line 3:",line3)

f.close()


#3.Readlines

f=open("one.txt","r")

lines=f.readlines()
print("list of lines:",lines)
print("Numbers of lines:",len(lines))
f.close()


#4.strip

f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()

#5.char()
f=open("one.txt","r")
char=f.read(5)
print("First 5 characters:",char)
f.close()