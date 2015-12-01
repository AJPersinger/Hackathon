#import textract
import time
import wikipedia

headers = {"User-Agent" : "MRS Hackathon MaterialsScience Bot v3 (am3798@drexel.edu)"}

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

# Opens the output file to see the last query and starts from there
readLines = 0
oldFile = open("output.txt").read()
oldFile = str(oldFile)
oldFile = oldFile.split()
readLines = oldFile.count("--&&--") 
print readLines

#Creates and opens outputfile
f = open("output.txt", 'a' )
exceptions = open("exceptions.txt", 'a' )
string = open('wordsReverse.txt').read()

shortList = string.splitlines()

# Cycles through X amount of words states status of process and wites to output file
for word in shortList:
    try:
        dictionary[word] = wikipedia.summary(str(word))
        print (dictionary[word] + "\n --&&-- \n")
        f.write(dictionary[word].encode('utf8') + "\n --&&-- \n")
        time.sleep(1)
        print(time.time() - t)
    except KeyError as e:
        exceptions.write(word.encode('utf8') + "\n --&&-- \n")
        print "EXCEPTION CAUGHT AT: " + word + " BECAUSE: " + e
    except:
        exceptions.write(word.encode('utf8') + "\n --&&-- \n")
        print "EXCEPTION CAUGHT AT: " + word


# Closes output file
f.close()
exceptions.close()

#toc
print(time.time() - t)
