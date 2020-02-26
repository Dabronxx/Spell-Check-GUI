def binarySearch(x, words):
    low = 0
    high = len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        item = words[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid -1
        else:
            low = mid + 1
    return -1

def main():
    spelledWrong = []
    dictionary = []

    textFileName = "text.txt"
    dictionaryFileName = "english.txt"

    textFile = open(textFileName, 'r')
    dictionaryFile = open(dictionaryFileName, 'r')

    for line in dictionaryFile:
        dictionary.append(line)

    for line in textFile:
        for word in line.split():
            if binarySearch(word, dictionary) != -1:
                spelledWrong.append(word)
    textFile.close()
    dictionaryFile.close()
    spelledWrongString = " ".join(spelledWrong[1:])
    print("be" == "be")

    print("A" in dictionary)

main()
