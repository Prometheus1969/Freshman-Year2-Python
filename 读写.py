
with open("abc.txt", "r") as f :
    print(f.read())
    
f.close()

print()

f = open("abc.txt", "r")

for lines in f:
    print(lines)
f.close()
