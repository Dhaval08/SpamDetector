#@author Dhaval Shah

import glob, os, sys

outputFile = open("nbmodel.txt", "w", encoding="latin1")

filename = ' '.join(sys.argv[1:])

spam_files = 0
ham_files = 0
total_files = 0

spam_words = {}
ham_words = {}
spam_prob = {}
ham_prob = {}
distinct_words = []

spam_wordCount = 0
ham_wordCount = 0

for root, subdirs, files in os.walk(filename):
    if(os.path.basename(os.path.normpath(root)) == "spam"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            total_files = total_files+1
            spam_files = spam_files+1
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():

                        spam_wordCount = spam_wordCount+1

                        if word in spam_words:
                            spam_words[word] = spam_words.get(word) + 1
                        else:
                            spam_words[word] = 2

    elif(os.path.basename(os.path.normpath(root)) == "ham"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            total_files = total_files+1
            ham_files = ham_files+1
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():

                        ham_wordCount = ham_wordCount+1

                        if word in ham_words:
                            ham_words[word] = ham_words.get(word) + 1
                        else:
                            ham_words[word] = 2

for i in spam_words:
    if i not in ham_words:
        ham_words[i] = 1
        ham_wordCount = ham_wordCount+1
for i in ham_words:
    if i not in spam_words:
        spam_wordCount = spam_wordCount+1
        spam_words[i] = 1

'''
for i in range (0, len(distinct_words)):
    if distinct_words[i] not in spam_words:
        spam_words[distinct_words[i]] = 1
    if distinct_words[i] not in ham_words:
        ham_words[distinct_words[i]] = 1
'''

probabilitySpam = spam_files/total_files
probabilityHam = ham_files/total_files

for i in spam_words:
    spam_prob[i] = spam_words.get(i)/spam_wordCount

for i in ham_words:
    ham_prob[i] = ham_words.get(i)/ham_wordCount

'''
print(spam_prob)
print(ham_prob)
'''

outputFile.write(str(probabilitySpam))
outputFile.write('\n')

outputFile.write(str(probabilityHam))
outputFile.write('\n')

print(spam_wordCount)
print(ham_wordCount)

for i in spam_words:

    print_line = i+" "+str(spam_prob.get(i))+" "+str(ham_prob.get(i))+" "+str(spam_words.get(i))+" "+str(ham_words.get(i))
    outputFile.write(print_line)
    outputFile.write('\n')
'''
print("Spam Words"+str(spam_wordCount))

print("Ham Words"+str(ham_wordCount))
'''

outputFile.close()