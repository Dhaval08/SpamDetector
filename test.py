newDict = {}

with open('/Users/shahdhaval/Downloads/Spam or Ham/NBOutput.txt') as f:
    for line in f:
        splitLine = line.split()
        print(splitLine)
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]

print(newDict.get('Umang')[0])