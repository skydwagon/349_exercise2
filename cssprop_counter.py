#File Made by Retro

file1 = open('stylessheet.css', 'r')
lines = file1.readlines()
setA = set()
for line in lines:
    if ";" in line:
        setA.add((line.split(':')[0]).strip())
print(setA)
print(len(setA))