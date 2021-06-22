def path():
    fileName =input("enter the file name:-")
    wordCount=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        wordCount=wordCount+len(words)
    print("no.of words:-")
    print(wordCount)
path()
