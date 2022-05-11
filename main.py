
# name = input("Enter the name:")
# print(type(name))



# a = int(input("Enter the value of A:"))
# b = int(input("Enter the value of B:"))

# c= a+b

# print(c)

# name1,name2,name3 = input("enter 3 names").split()

# print("Name1:",name1)
# print("Name2:",name2)
# print("Name3:",name3)


# para =["25","40","33"]
# print('#'.join(para))

inputParagraph =[]

print("Enter a para:")

while True:
    line = input()
    if line:
        inputParagraph.append(line)
    else:
        break
print(inputParagraph)
output='\n'.join(inputParagraph)
print(output)
