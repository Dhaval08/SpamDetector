import glob, os
import math

newDict = {}

with open('/Users/shahdhaval/PycharmProjects/CSCI 544 - Naive Bayes/nbmodel.txt') as f:
    spam_probability = f.readline()
    ham_probability = f.readline()

    for line in f:
        splitLine = line.split()
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]


print(spam_probability)
print(ham_probability)
print(newDict)


for root, subdirs, files in os.walk("/Users/shahdhaval/Downloads/Spam or Ham/Demo/Samples"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
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

            spam = sum_spam*float(spam_probability)
            ham = sum_ham*float(ham_probability)

            if(spam>ham):
                print(spam)
                print("spam")
            else:
                print(ham)
                print("ham")