with open('TextFile.txt', 'r') as reader:   #reader is an object we can give any name instea of it
    content = reader.readlines() #hello, goodevening, how, areyou
    reversed(content)
    with open('TextFile.txt', 'w') as writer:
        for line in reversed(content): #are you, how, good evening, hello
            writer.write(line)