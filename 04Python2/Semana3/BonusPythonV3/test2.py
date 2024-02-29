newFile = open('data.txt', 'r')
for line in newFile.readlines():
    print(line.strip())