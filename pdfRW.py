#import textract
import time
import wikipedia
t = time.time()

#plainFile = textract.process("source.pdf")

#textList = plainFile.split()
definitionList = []

#outputFile = open("outputFile.txt", "wb")
outputList = []
totalWords = 0
string = open('words.txt').read()
for word in string.split():
    totalWords += 1

dict0 = {}
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
dictionary = {}
finalDefList = [dict0, dict1, dict2, dict3, dict4]
k = 0
i = 0
#while i < len(finalDefList):
#    for dictionary in finalDefList:
#        i += 1
#        string = open(str(k)+'.txt').read()
#        for word in string.split():
#            dictionary[word] = wikipedia.summary(word, sentences=2)
#        k += 1
string = open('words.txt').read()
while i < 100:
    for word in string.split():
        dictionary[word] = wikipedia.summary(word, sentences=2)
        i += 1

f = open(output, 'w' )
f.write(dictionary)
f.close()


print(time.time() - t)


# Close opend file
#outputFile.write( "Python is a great language.\nYeah its great!!\n");

#outputFile.close()
