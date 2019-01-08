'''
Homework #2 - CMP SCI 4500
Author: Allie Robbins
Due Date: September 05, 2018
Software Version: LiClipse 5.0.2 using Python 3.7.0
Goal: To traverse a pyramid using a dice game environment
Sources Used: https://www.pythonforbeginners.com/
             http://interactivepython.org/RkmcZ/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
             https://www.tutorialspoint.com/python/python_2darray.htm
             http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
             https://www.geeksforgeeks.org/print-without-newline-python/
'''
#Import needed libraries
import random

#Beginning of Program 
print("Starting program...\n")

#Open output file
outputFile = open("HW1RobbinsOutfile.txt", "w+")


#Class for dice functions
class dice:
    def roll(self) :
        return random.randint(1, 4)
    '''1 = Upper Left
       2 = Upper Right
       3 = Lower Left
       4 = Lower right '''

#List of all the nodes to access individually
#format of nodes → [Dot Count, Upper Left, Upper Right, Lower Left, Lower Right]
NodeList =[[1122],
           [0, None, None, 2, 3],
           [0, None, 1, 4, 5],
           [0, 1, None, 5, 6],
           [0, None, 2, 7, 8],
           [0, 2, 3, 8, 9],
           [0, 3, None, 9, 10],
           [0, None, 4, 11, 12],
           [0, 4, 5, 12, 13],
           [0, 5, 6, 13, 14],
           [0, 6, None, 14, 15],
           [0, None, 7, 16, 17],
           [0, 7, 8, 17, 18],
           [0, 8, 9, 18, 19],
           [0, 9, 10, 19, 20],
           [0, 10, None, 20, 21],
           [0, None, 11, None, None],
           [0, 11, 12, None, None],
           [0, 12, 13, None, None],
           [0, 13, 14, None, None],
           [0, 14, 15, None, None],
           [0, 15, None, None, None]]

#Variable to keep track of the location during the game 
currentPlace = 1

#Initialize the dice
dice = dice()

#variable to determine if End-Of-Game
GameOver = False

#Print opening explanation of the game
print("Hello! And welcome to Pyramid Run! The fast-paced game where you will\n attempt to visit every place-marker shown on the board below.\n\n                  1\n               2     3\n            4     5     6\n         7     8     9     10\n      11   12    13     14    15\n   16   17    18    19     20     21\n\nBut before we begin, allow me to explain how the game works. You will\n begin at the top of the pyramid, in the 1 position.At the beginning of each\n turn, a 4 sided dice will be rolled to determine where you move.You can\n move to the Upper Left, Upper Right, Lower Left, and Lower Right.Sometimes,\n you can’t make a possible move. For example, if you are at 1, you can’t go up.\n If you are at 19, you can’t go down. If you roll a direction you can’t move,\n you stay where you are in the pyramid, but that does count as a “move.”\n For each time you make a move, that position will gain a dot. The game is over\n once you have gone to each position at least once.\n")
print("What this simulation is going to do, starting at 1, the 4 sided dice\n will roll and that will dictate the where to move to. If there is no space\n to move to, the simulation will automatically mark the turn and roll the dice\n again. At the end of the 'turn', the simulation will look to see if every\n space has been visited. If every space has been reached, the game will end\n and print the statistics. If not, the game continues!\n")
outputFile.write("Hello! And welcome to Pyramid Run! The fast-paced game where you will\n attempt to visit every place-marker shown on the board below.\n\n                  1\n               2     3\n            4     5     6\n         7     8     9     10\n      11   12    13     14    15\n   16   17    18    19     20     21\n\nBut before we begin, allow me to explain how the game works. You will\n begin at the top of the pyramid, in the 1 position.At the beginning of each\n turn, a 4 sided dice will be rolled to determine where you move.You can\n move to the Upper Left, Upper Right, Lower Left, and Lower Right.Sometimes,\n you can’t make a possible move. For example, if you are at 1, you can’t go up.\n If you are at 19, you can’t go down. If you roll a direction you can’t move,\n you stay where you are in the pyramid, but that does count as a 'move.'\n For each time you make a move, that position will gain a dot. The game is over\n once you have gone to each position at least once.\n\n")
outputFile.write("What this simulation is going to do, starting at 1, the 4 sided dice\n will roll and that will dictate the where to move to. If there is no space\n to move to, the simulation will automatically mark the turn and roll the dice\n again. At the end of the 'turn', the simulation will look to see if every\n space has been visited. If every space has been reached, the game will end\n and print the statistics. If not, the game continues!\n\n")

#beginning statements 
print("Let's start the game!\n\n1, ", end = '')
outputFile.write("Let's start the game!\n\n1, ")

#while loop to keep the game going
#The variable GameOver will keep track of all the dot counts.
#Once all the spaces have been visited at least once, 
#the variable will be changed to signal that the game is over.
while GameOver is not True:

    #Roll the dice and move accordingly.
    nextPlace = dice.roll()
        
    if nextPlace == 1:                                  #Rolled to Upper Left
        if NodeList[currentPlace][nextPlace] == None:   #If there is no where to go:
            NodeList[currentPlace][0] += 1               #Increment the DC to indicate a move was made
        else:
            print("%s, " % NodeList[currentPlace][nextPlace], end ='')     #If there is somewhere to go:
            outputFile.write("%s, " % NodeList[currentPlace][nextPlace])    #Print placement
            currentPlace = NodeList[currentPlace][nextPlace]                #Update the current position
            NodeList[currentPlace][0] += 1                                  #Increment the DC to indicate a move was made
                
    elif nextPlace == 2:                                   #Rolled to Upper Right
        if NodeList[currentPlace][nextPlace] == None:      #If there is no where to go:
            NodeList[currentPlace][0] += 1                  #Increment the DC to indicate a move was made
        else:
            print("%s, " % NodeList[currentPlace][nextPlace], end ='')     #If there is somewhere to go:
            outputFile.write("%s, " % NodeList[currentPlace][nextPlace])    #Print placement
            currentPlace = NodeList[currentPlace][nextPlace]                #Update the current position  
            NodeList[currentPlace][0] += 1                                  #Increment the DC to indicate a move was made
                
    elif nextPlace == 3:                                    #Rolled to Lower Left
        if NodeList[currentPlace][nextPlace] == None:       #If there is no where to go:
            NodeList[currentPlace][0] += 1                   #Increment the DC to indicate a move was made
        else:
            print("%s, " % NodeList[currentPlace][nextPlace], end ='')     #If there is somewhere to go:
            outputFile.write("%s, " % NodeList[currentPlace][nextPlace])    #Print placement
            currentPlace = NodeList[currentPlace][nextPlace]                #Update the current position    
            NodeList[currentPlace][0] += 1                                  #Increment the DC to indicate a move was made
                
    elif nextPlace == 4:                                   #Rolled to Lower Right    
        if NodeList[currentPlace][nextPlace] == None:      #If there is no where to go:
            NodeList[currentPlace][0] += 1                  #Increment the DC to indicate a move was made
                                                        
        else:
            print("%s, " % NodeList[currentPlace][nextPlace], end ='')     #If there is somewhere to go:
            outputFile.write("%s, " % NodeList[currentPlace][nextPlace])    #Print placement
            currentPlace = NodeList[currentPlace][nextPlace]                #Update the current position
            NodeList[currentPlace][0] += 1                                  #Increment the DC to indicate a move was made
                    
    #Check all the DC for a 0 value. If there is a 0, the game continues, else, end the game.
    for i in range(1, 22):  
            if NodeList[i][0] == 0:
                GameOver = False
                break
            else:
                GameOver = True
             
#Game has completed
print(". \n\nGame over!!!\n")
outputFile.write(". \n\nGame over!!!\n\n")

#Variables to calculate the game statistics
total = 0
maxNum = 0

print("Final Statistics: ")
outputFile.write("Final Statistics: \n")

#Loop through the DC:
    #Add up all the values for the total
    #Locate the maximum # of dots
for i in range(1, 22):
    total += NodeList[i][0]
    if NodeList[i][0] > maxNum:
        maxNum = NodeList[i][0]

#Calculate the average 
average = total / 21

#Print final statistics
print("Total # of moves: %s" % total)
outputFile.write("Total # of moves: %s\n" % total)
print("Average # of dots: %s" % average)
outputFile.write("Average # of dots: %s\n" % average)
print("Maximum # of dots: %s" % maxNum)
outputFile.write("Maximum # of dots: %s\n" % maxNum)


#End of Program
print("\nProgram has finished - Please see HW2RobbinsOutfile.txt for data.")
outputFile.write("\nProgram has finished - Please see HW2RobbinsOutfile.txt for data.")

#close the files
outputFile.close()