print("Hahah Hola")

print(1,2,3,4)

print("shell", "unix", "scala", 10)


name = "python programming"

print(name)

print("I love",name)


# Slicing - extracting string

print(name[0])
print(name[1])
print(name[2])

print(name[0:3])
print(name[1:4])
print(name[2:9])
print(name[4:10])


print(name[2:15:1])
print(name[::])  # Prints Everything
print(name[::2]) # Prints at every 2 steps

print(name[1:9:5])
print(name[:])

print(name[-1])
print(name[-2])
print(name[-3])

print(name[::-1]) # pRints everything in reverse
print(name[::-2])
print(name[:2])
print(name[:2:-1])
print(name[:3:-4])
print(name[3::-2]) # python programming
print(name[-1:-8:-1]) # Go in reverse direction
print(name[18:2:-1])
print(name[len(name)-1:3:-1])

name = "python programming"

print(name.isupper())
print(name.islower())
print(name.upper()) # Display in UPPER case
print(name.lower())


print(name.replace('python', 'new'))

print(name)

print(name.startswith('p'))
print(name.startswith('q'))
print(name.endswith('g'))
print(name.find("gra")) # if subset exist it returns starting index number
print(name.find('q')) # if subset does not exist it returns -1/


aname = "   python   "

print(aname.strip()) # Strip space on both sides
print(aname.lstrip())
print(aname.rsplit())


print(name.capitalize()) # First character in Capital letter


# Skeleton or Template - a pre-defined structure that can be changed dynamically

string = "I love {} and {}" # This act like skeleton / template

print(string.format('apple','banana'))

print(string.format('java',"Scala"))

string1 = "I owe {} some {}."

print(string1.format(name,aname))

