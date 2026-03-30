#Write()

#ex.1
f=open("one.txt", "w")
f.write("Hello, World!\n")
f.write("Welcome to Python programming.\n")
f.close()

#ex.2
f=open("one.txt", "w")
f.write("This is a new line.\n")
f.close()

#ex.3
f=open("one.txt", "a")
lines=[
    "Hello,World!\n",
    "Welcome to Python programming.\n",
    "This is a new line.\n"
]
f.writelines(lines)
f.close()