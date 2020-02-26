# Programmer:    Branko Andrews
# Date:          Dec. 15, 2016
#
# Problem Statement: Write a GUI program that has 2 text boxes.  The first text box accepts a file to check the spelling.
# The second file is the dictionary file or words.  When you click the spell-check button the program opens both files reads
# the dictionary file into memory and then spell checks the other file.  To do the spell checking of the other file you should do a
# binary search on the list of words in the dictionary.  If the word is not in the dictionary file, print it on the
# screen as a potentially incorrect word. 
# Overall Plan:
# 1. Import Button and Graphics
# 2. Create a rectangular shaped GUI window
# 3. Set the background to yellow
# 4. Create texts for each input box
# 5. Create entries for the dictionary and text file
# 6. Create large text that will display how many words were spelled incorrectly
# 7. Create 6 ouput lines for each line of incorrect words
# 8. Create check spelling and quit buttons and activate them
# 9. Create a variable that will return where the user clicked
# 10. Create a while loop that will continue as long as the quit button is not clicked
# 11. Within a loop, create an if statement to see if the 'check spelling button has been clicked
# 12. Set all word outputs texts to an empty string
# 13. Initialize two lists, one for the dictionary, the other for the list of misspelled words
# 14. Get the file names from the input boxes
# 15. Open and read each file
# 16. Lower case and trim every word in the dictionary file and append it to the dictionary array and sort the array
# 17. Append each word in the text file that is not found in the dictionary to the misspelled word array
# 18. Use binary search to determine if the word is in the dictionary
# 19. Close both files
# 20. If the misspelled words array is empty, set the background to green
# 21. If not, set the background to red and output a max of 10 words per word output line

#Import Button and Graphic
from graphics import*
from button import Button

#Binary Search that returns a boolean
def contains(word, dictionary):
    low = 0
    high = len(dictionary) - 1
    while low <= high:
        mid = (low + high) // 2
        item = dictionary[mid]
        if word.lower() == item:
            return True
        elif word.lower() < item:
            high = mid -1
        else:
            low = mid + 1
    return False


def main():
    #Create a rectangular shaped GUI window
    win = GraphWin("Spell Check", 800, 180)
    win.setCoords(0.0, 0.0, 9, 3)
    #Set the background to yellow
    win.setBackground("yellow")

    #Create texts for each input box
    Text(Point(1,.9), "Text File").draw(win)
    Text(Point(1,2.18), "Dictionary File").draw(win)

    #Create entries for the dictionary and text file
    textInput = Entry(Point(1,1.3), 8)
    textInput.setText("")
    textInput.draw(win)

    dicInput = Entry(Point(1,2.55), 8)
    dicInput.setText("")
    dicInput.draw(win)

    #Create large text that will display how many words were spelled incorrectly
    wordCount = Text(Point(5.25,2.75), "")
    wordCount.setSize(22)
    wordCount.draw(win)

    #Create 6 ouput lines for each line of incorrect words
    wordOutput1 = Text(Point(5.25,2), "")
    wordOutput1.draw(win)

    wordOutput2 = Text(Point(5.25,1.7), "")
    wordOutput2.draw(win)

    wordOutput3 = Text(Point(5.25,1.4), "")
    wordOutput3.draw(win)

    wordOutput4 = Text(Point(5.25,1.1), "")
    wordOutput4.draw(win)

    wordOutput5 = Text(Point(5.25,.8), "")
    wordOutput5.draw(win)

    wordOutput6 = Text(Point(5.25,.5), "")
    wordOutput6.draw(win)

    #Create check spelling and quit buttons and activate them
    checkButton = Button(win, Point(1,1.8), 1.3, .3, "Check Spelling")
    checkButton.activate()

    quitButton = Button(win, Point(1,.5), .6, .3, "Quit")
    quitButton.activate()

    #Create a variable that will return where the user clicked
    pt = win.getMouse()

    #Create a while loop that will continue as long as the quit button is not clicked
    while not quitButton.clicked(pt):
        #Within a loop, create an if statement to see if the 'check spelling button has been clicked
        if checkButton.clicked(pt):
            #Set all word outputs texts to an empty string
            wordOutput1.setText("")
            wordOutput2.setText("")
            wordOutput3.setText("")
            wordOutput4.setText("")
            wordOutput5.setText("")
            wordOutput6.setText("")
            #Initialize two lists, one for the dictionary, the other for the list of misspelled words
            spelledWrong = []
            dictionary = []
            #Get the file names from the input boxes
            textFileName = textInput.getText()
            dictionaryFileName = dicInput.getText()
            #Open and read each file
            textFile = open(textFileName,'r')
            dictionaryFile = open(dictionaryFileName,'r')
            #Lower case and trim every word in the dictionary file and append it to the dictionary array
            for line in dictionaryFile:
                for word in line.split():
                    word.lower()
                    dictionary.append(word)
            dictionary.sort()
            #Append each word in the text file that is not found in the dictionary to the misspelled word array
            for line in textFile:
                for word in line.replace(',',' ').replace('.',' ').replace('?',' ').replace(';',' ').split():
                    if not contains(word, dictionary):
                        spelledWrong.append(word)
            #Close both files
            textFile.close()
            dictionaryFile.close()
            #If the misspelled words array is empty, set the background to green 
            if len(spelledWrong) == 0:
                win.setBackground("green")
                wordCount.setText("All words spelled correctly!")
            #If not, set the background to red and output a max of 10 words per word output line
            else:
                win.setBackground("red")
                wordCountString = str(len(spelledWrong)) + " words were spelled wrong"
                wordCount.setText(wordCountString)

                if len(spelledWrong) <= 10:
                    wordOutput1.setText(", ".join(spelledWrong[0:]))
                elif len(spelledWrong) <= 20:
                    wordOutput1.setText(", ".join(spelledWrong[0:9]))
                    wordOutput2.setText(", ".join(spelledWrong[10:]))
                elif len(spelledWrong) <= 30:
                    wordOutput1.setText(", ".join(spelledWrong[0:9]))
                    wordOutput2.setText(", ".join(spelledWrong[10:19]))
                    wordOutput3.setText(", ".join(spelledWrong[20:]))
                elif len(spelledWrong) <= 40:
                    wordOutput1.setText(", ".join(spelledWrong[0:9]))
                    wordOutput2.setText(", ".join(spelledWrong[10:19]))
                    wordOutput3.setText(", ".join(spelledWrong[20:29]))
                    wordOutput4.setText(", ".join(spelledWrong[30:]))
                elif len(spelledWrong) <= 50:
                    wordOutput1.setText(", ".join(spelledWrong[0:9]))
                    wordOutput2.setText(", ".join(spelledWrong[10:19]))
                    wordOutput3.setText(", ".join(spelledWrong[20:29]))
                    wordOutput4.setText(", ".join(spelledWrong[30:39]))
                    wordOutput5.setText(", ".join(spelledWrong[40:]))
                else:
                    wordOutput1.setText(", ".join(spelledWrong[0:9]))
                    wordOutput2.setText(", ".join(spelledWrong[10:19]))
                    wordOutput3.setText(", ".join(spelledWrong[20:29]))
                    wordOutput4.setText(", ".join(spelledWrong[30:39]))
                    wordOutput5.setText(", ".join(spelledWrong[40:49]))
                    wordOutput6.setText(", ".join(spelledWrong[50:]))
        
        pt = win.getMouse()

    win.close()

main()
                

        

        

        
        


    
