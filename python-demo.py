print("Hello World!")


print()
print("Begin Variables")
x = 1
y = 2
print("x=", x)
print("y=", y)


print()
print("Begin Operators")

print(x+y)
z = x + y
print("z=", z)
print(z < y)
print(z != y)


print()
print("Begin User Input")

nameStr = input("Name: ")
age = eval(input("Age: "))
print ("Your name is", nameStr, "and you are", age)

print()
print("Begin Functions")

def seven():
  return 7

def addNums(num1, num2):
  return num1+num2

print(addNums(7,8))
print(seven())

print()
print("Begin Loops")

for i in range(0,10):
  print(i)


print("Begin Loops")

for i in range(0,10):
  if (i % 2 == 1):
    print("Found an odd. Breaking")
    break
  else:
    print(i)


for i in range(0,10):
  if (i % 2 == 1):
    print("Found an odd. Skipping.")
    continue
  else:
    print(i)


print()
print("Begin Strings")

string = "Hello World!"
print(string)
print(string[1])
print(string[1:])
print(string[:-2])


print()
print("Begin File Input")

inFile = open("inputFile.txt", "r")

for line in inFile:
  print(line.rstrip("\n"))

inFile.close()

print()
print("Begin File Output")

outFile = open("outputFile.txt", "w")
outFile.write("Hello World!\n")
outFile.close()

outFile = open("outputFile.txt", "w")
outFile.write("Hello World 2!\n")
outFile.close()


print()
print("Begin List")

l = ["a", "b", "c", 2, 3, 4]
for i in range(len(l)):
  print(l[i])

for e in l:
  print(e)

print()
print("Begin Dictionary")

phoneNums = {}
phoneNums['Eric'] = '512-555-0123'
phoneNums['Daniel'] = '512-555-0124'
phoneNums['Eric'] = '512-555-0000'
print(phoneNums['Eric'])