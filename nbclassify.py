#@author Dhaval Shah


import glob, os
import math

newDict = {}
correctlyClassifiedSpam = 0
correctlyClassifiedHam = 0
totalFiles = 0
spamClassified = 0
hamClassified= 0
spamFiles = 0
hamFiles = 0

with open("/Users/shahdhaval/PycharmProjects/CSCI 544 - Naive Bayes/nbmodel.txt","r", encoding="latin1") as f:
    spam_probability = f.readline()
    ham_probability = f.readline()

    for line in f:
        splitLine = line.split()
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]

print(spam_probability)
print(ham_probability)

outputFile = open("/Users/shahdhaval/PycharmProjects/CSCI 544 - Naive Bayes/nboutput.txt", "w")

for root, subdirs, files in os.walk("/Users/shahdhaval/Desktop/CSCI544/SpamHam/dev"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            if(os.path.basename(os.path.normpath(root)) == "spam"):
                spamFiles = spamFiles + 1
            if(os.path.basename(os.path.normpath(root)) == "ham"):
                hamFiles = hamFiles + 1
            totalFiles = totalFiles + 1

            spam = 0
            ham = 0
            sum_spam = 0
            sum_ham = 0
            new_words = []
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    line = ''.join(line.splitlines())
                    for word in line.split():
                        new_words.append(word)
            for i in new_words:
                if i in newDict:
                    sum_spam = sum_spam + math.log(float(newDict.get(i)[0]))
                    sum_ham = sum_ham + math.log(float(newDict.get(i)[1]))

            spam = sum_spam + math.log(float(spam_probability))
            ham = sum_ham + math.log(float(ham_probability))

            if(spam>ham):
                spamClassified = spamClassified + 1
                if(os.path.basename(os.path.normpath(root)) == "spam"):
                    correctlyClassifiedSpam = correctlyClassifiedSpam + 1

                outputFile.write("Spam"+" "+root+"/"+file+"\n")

            else:
                hamClassified = hamClassified + 1
                if(os.path.basename(os.path.normpath(root)) == "ham"):
                    correctlyClassifiedHam = correctlyClassifiedHam + 1
                outputFile.write("Ham"+" "+root+"/"+file+"\n")



print(correctlyClassifiedSpam)
print(correctlyClassifiedHam)

print(spamClassified)
print(hamClassified)

spamPrecision = (correctlyClassifiedSpam/spamClassified)
hamPrecision = (correctlyClassifiedHam/hamClassified)

spamRecall = (correctlyClassifiedSpam/spamFiles)
hamRecall = (correctlyClassifiedHam/hamFiles)

spamF1 = (2*spamPrecision*spamRecall)/(spamPrecision+spamRecall)
hamF1 = (2*hamPrecision*hamRecall)/(hamPrecision+hamRecall)

print(spamF1)
print(hamF1)