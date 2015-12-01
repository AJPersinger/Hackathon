#import textract
import time
import wikipedia

headers = {"User-Agent" : "MRS Hackathon MaterialsScience Bot v2 (am3798@drexel.edu)"}

#tic
t = time.time()

#plainFile = textract.process("source.pdf")

#textList = plainFile.split()

# Create hierarchy for dictionary words (not yet implemented)
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

#Creates and opens outputfile
f = open("output.txt", 'w' )
exceptions = open("exceptions.txt", 'w' )
string = open('words.txt').read()

# Cycles through X amount of words states status of process and wites to output file
for word in string.splitlines():
    try:
        dictionary[word] = wikipedia.summary(str(word))
        print dictionary[word]
        f.write(dictionary[word].encode('utf8') + "--&&-- \n")
        time.sleep(1)
    except:
        exception.write(dictionary[word].encode('utf8') + "--&&-- \n")
# Closes output file
f.close()
exceptions.close()

#toc
print(time.time() - t)
