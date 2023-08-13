n = int(input("Enter the height:"))


#Left angle triangle
print("Left-angle triangle:\n\n")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

print("\n\n")

#Left angle triangle upside-down
print("Left-angle triangle upside-down:\n\n")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")

    for j in range(i,n):
        print("*",end="")
    
    print()

print("\n\n")


#Right angle triangle
print("Right-angle triangle:\n\n")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

print("\n\n")

#Right-angle triangle upside-down
print("Right-angle triangle upside-down:\n\n")
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    print()

print("\n\n")

#Hill-bridge star pattern
print("Hill Bridge pattern:\n\n")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("  ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

print("\n\n")

#Hill pattern
print("Hill pattern:\n\n")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(i):
        print("*",end="")

    for j in range(i+1):
        print("*",end="")
    print()

print("\n\n")

#Hill star pattern upside-down
print("Hill pattern upside-down:\n\n")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")

    for j in range(i,n):
        print("*",end="")

    for j in range(i,n-1):
        print("*",end="")
    print()


print("\n\n")

#sand-glass pattern
print("Sand glass pattern:\n\n")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(i):
        print("*",end="")

    for j in range(i+1):
        print("*",end="")
    print()

print("\n\n")

#Diamond pattern
print("Diamond pattern:\n\n")
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")

    for k in range(i+1):
        print("*",end="")

    for j in range(i):
        print("*",end="")

    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(i,n-1):
        print("*",end="")
    
    for j in range(i,n):
        print("*",end="")
    print()
        

