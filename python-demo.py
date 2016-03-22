print("Hello World!")


# print()

# for i in range(0,10):
#   if (i % 2 == 1):
#     print("Found an odd. Skipping.")
#     continue
#   else:
#     print(i)


# print()
# print("Begin Strings")

# string = "Hello World!"
# print(string)
# print(string[1])
# print(string[1:])
# print(string[:-2])


# print()
# print("Begin File Input")

# inFile = open("inputFile.txt", "r")

# for line in inFile:
#   print(line.rstrip("\n"))

# inFile.close()

# print()
# print("Begin File Output")

# outFile = open("outputFile.txt", "w")
# outFile.write("Hello World!\n")
# outFile.close()

# outFile = open("outputFile.txt", "w")
# outFile.write("Hello World 2!\n")
# outFile.close()


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