import glob, os
import re
'''
for root, subdirs, files in os.walk("/Users/shahdhaval/Downloads/Spam or Ham"):
        print('--\nroot = ' + root)

        if(os.path.basename(os.path.normpath(root)) == "spam"):
            print("true")
'''
spam_files = 0
ham_files = 0
total_files = 0

spam_words = {}
ham_words = {}
spam_prob = {}
ham_prob = {}
distinct_words = []

for root, subdirs, files in os.walk("/Users/shahdhaval/Downloads/Spam or Ham/Demo"):
    if(os.path.basename(os.path.normpath(root)) == "spam1"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            total_files = total_files+1
            spam_files = spam_files+1
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    line = ''.join(line.splitlines())
                    for word in line.split():

                        if word not in distinct_words:
                            distinct_words.append(word)

                        if word in spam_words:
                            spam_words[word] = spam_words.get(word) + 1
                        else:
                            spam_words[word] = 2

    elif(os.path.basename(os.path.normpath(root)) == "ham1"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            total_files = total_files+1
            ham_files = ham_files+1
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    line = ''.join(line.splitlines())
                    for word in line.split():

                        if word not in distinct_words:
                            distinct_words.append(word)

                        if word in ham_words:
                            ham_words[word] = ham_words.get(word) + 1
                        else:
                            ham_words[word] = 2

for i in range (0, len(distinct_words)):
    if distinct_words[i] not in spam_words:
        spam_words[distinct_words[i]] = 1
    if distinct_words[i] not in ham_words:
        ham_words[distinct_words[i]] = 1

probabilitySpam = spam_files/total_files
probabilityHam = ham_files/total_files

print(probabilityHam, probabilitySpam)

print(spam_words)
print(ham_words)
print(distinct_words)

spam_wordCount = 0
ham_wordCount = 0

for i in spam_words:
    spam_wordCount = spam_wordCount + spam_words.get(i)

for i in ham_words:
    ham_wordCount = ham_wordCount + ham_words.get(i)

print(spam_wordCount)
print(ham_wordCount)

for i in spam_words:
    spam_prob[i] = spam_words.get(i)/spam_wordCount

for i in ham_words:
    ham_prob[i] = ham_words.get(i)/ham_wordCount

print(spam_prob)
print(ham_prob)

file = open("/Users/shahdhaval/PycharmProjects/CSCI 544 - Naive Bayes/nbmodel.txt", "w")
file.write(str(probabilitySpam))
file.write('\n')

file.write(str(probabilityHam))
file.write('\n')

for i in distinct_words:

    print_line = i+" "+str(spam_prob.get(i))+" "+str(ham_prob.get(i))
    file.write(print_line)
    file.write('\n')
