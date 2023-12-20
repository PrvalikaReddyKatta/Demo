file = open('TextFile.txt')
#print(file.read())    #read method is used to read the file


list = file.readline()
while list!= '':
    print(list)
    list = file.readline()

file.close()