#This is assigning a list to the gameboard variable
gameboard = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]



#This is the main function which actually allows the board to print, sets a win counter 
#and allows the user to play
def main():
    """This function states the main components for the program to call"""
    win = 0
    printBoard()
    Player_1(gameboard, 3)
    
    
    
#This allows the elements to be set in the gameboard so the user can access them
#as indexes (i and j)
def setelement (element, position, gameboard, boardsize):
    """This function defines the layout for the elements for the gameboard"""
    for i in range (3):
        for j in range (3):            
            print(gameboard[i][j].format(gameboard[i][j]))
            if (gameboard[i][j] == position):                
######################################################################################
#This prints specific information about the lists, gameboard and elements                
                print('the position of setelement is... {}'.format(position))
                print('element is... {}'.format(element))
                print('the gameboard on entering setelement is {}'.format(gameboard))
                print('this is your current position in the board')
######################################################################################                
#This updates the new gameboard                
                gameboard[i][j] = element                
#This prints out which element the user has used and returns the updated gameboard                
    print('board in setelement is {}'.format(gameboard))
    return gameboard



#This displays the board and then allows the user to be able to input their desired position     
def Player_1 (gameboard,boardsize):
    """This function is a docstring which allows the user to input the desired position on the gameboard"""
    element = 'X'
#This allows the user to be able to input where they want their counter to go    
    position = input("player 1, which position do you choose?")
    gameboard = setelement(element, position, gameboard, boardsize)
    drawBoard(gameboard,boardsize)
#This records which win state has been input into the gameboard    
    win = checkWin(gameboard,boardsize)
#This checks player 2's win-state if the player 1 did not get a matched win-state    
    if (win==False):
        Player_2(gameboard,boardsize)
    else:
        print('Congratulations Player 1! You win!')
        
        

#This displays the board and then allows the user to be able to input their desired position        
def Player_2 (gameboard,boardsize):
    """This function is a docstring which allows the user to input the desired position on the gameboard"""
    element = 'O'
#This allows the user to be able to input where they want their counter to go    
    position = input("player 2, Which position do you choose?")
    gameboard = setelement(element, position, gameboard, boardsize)
    drawBoard(gameboard,boardsize)
#This records which win state has been input into the gameboard    
    win = checkWin(gameboard,boardsize)
#This checks player 2's win-state if the player 1 did not get a matched win-state    
    if (win==False):
        Player_1(gameboard,boardsize)
    else:
        print('Congratulations Player 2! You win!')
        
        
        
def printBoard():
    """This function sets the required values to allow the board to be printed"""
    boardsize = 3                                               
    gameboard = defineBoard(boardsize)
#This calls the board labels which have been created (x and y)    
    createBoardLabels(gameboard, boardsize)
#This calls the gameboard to be drawn with the new parts implemented    
    drawBoard(gameboard, boardsize)
    
    

def defineBoard(boardsize):
    """This function allows the gameboards range to be set"""
    gameboard = [[""] * boardsize for i in range(boardsize)]
#This returns the gameboard with the new added features and gives the correct size 
#according to what boardsize the user inputs    
    return gameboard



def inputBoardSize():
    """This function allows the user to be able to input their desired board dimensions"""
#This input statement allows the user to enter their desired board size    
    boardsize = input('enter board dimension: ')                
    return int(boardsize)



def createBoardLabels(gameboard, boardsize):
    """This function allows the indexes to be counted"""
#This assigns a number to the index counter (look at the for loop comment)    
    counter = 0
#For loop allowing the program to add up the three different index counters together     
    for i in range(boardsize):        
        for j in range(boardsize):
            counter +=1
            gameboard[i][j] = counter
#Updates the changes made to the gameboard and returns the new version            
    return (gameboard)



def print_divider (boardsize):
    """This function allows a part of the board to be made"""
    print ('|'.join(['____' for x in range(boardsize)])) 
    
    

def print_blank (boardsize):
    """This function allows a part of the board to be made"""
    print ('|'.join(['    ' for x in range(boardsize)]))   
    
    

def print_labels(counter, gameboard, boardsize):
    """This function allows a part of the board to be made"""
    row = ' | '.join(['%2s' % gameboard[counter][x] for x in range(boardsize)])
    row = ' ' + row
    print(row)
    
    
   
def drawBoard(gameboard, boardsize):
    """This function allows gameboard to be drawn"""
    for i in range(boardsize):
        print_blank(boardsize)
        print_labels(i,gameboard, boardsize)
#If statement to compare the indexes to the boardsize        
        if (i == boardsize-1):
            print_blank(boardsize)
        else:
            print_divider(boardsize)          
            
#
#
#
#
#
#
#
#
#
#
#


#This checks the first vertical column
def win1 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexs for the J column    
    j = 0
#For loop for checking the win state of the row     
    for i in range (2):
        if gameboard [i][j] != gameboard [i+1][j]:
            win = False
    return (win)



#This checks the second vertical column
def win2 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexs for the J column    
    j = 1
#For loop for checking the win state of the row    
    for i in range (2):
        if gameboard [i][j] != gameboard [i+1][j]:
            win = False
    return (win)



#This checks the third vertical column
def win3 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexs for the J column    
    j = 2
#For loop for checking the win state of the row    
    for i in range (2):
        if gameboard [i][j] != gameboard [i+1][j]:
            win = False
    return (win)




#This checks the first horizontal row
def win4 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexes for the I column    
    i = 0
#For loop checking the win state of the row    
    for j in range (2):
        if gameboard [i][j] != gameboard [i][j+1]:
            win = False
    return (win)



#This checks the second horizontal row
def win5 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexes for the I column     
    i = 1
#For loop checking the win state of the row    
    for j in range (2):
        if gameboard [i][j] != gameboard [i][j+1]:
            win = False
    return (win)



#This checks the third horizontal row
def win6 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#Setting the indexes for the I column    
    i = 2
#For loop checking the win state of the row    
    for j in range (2):
        if gameboard [i][j] != gameboard [i][j+1]:
            win = False
    return (win)



#This checks the first diagonal row
def win7 (gameboard):
    """This function defines a win-state for the game"""
    win = True
#For loop checking the win state of the diaganol row    
    for i in range (2):
        if gameboard[i][i] != gameboard[i+1][i+1]:
            win = False
       # j=j+1  
    return (win)



#This checks the second diagonal row
def win8 (gameboard):
    """This function defines a win-state for the game"""
    win = True
    j = 2
#For loop checking the win state of the diaganol row    
    for i in range (2):
        if gameboard [i][j] != gameboard [i+1][j-1]:
            win = False
        j=j-1      
    return (win)
#
#
#
#
#
#
#


#The box below shows all of the possible win states from the board. 

###########################################################################
                                                                          #
#win1 = [['x','2','3'],['x','5','6'],['x','8','9']]                       #
#win2 = [['1','x','3'],['4','x','6'],['7','x','9']]                       #
#win3 = [['1','2','x'],['4','5','x'],['7','8','x']]                       #
#win4 = [['x','x','x'],['4','5','6'],['7','8','9']]                       #
#win5 = [['1','2','3'],['x','x','x'],['7','8','9']]                       #  
#win6 = [['1','2','3'],['4','5','6'],['x','x','x']]                       #  
#win7 = [['x','2','3'],['4','x','6'],['7','8','x']]                       #
#win8 = [['1','2','x'],['4','x','6'],['x','8','9']]                       # 
                                                                          #
###########################################################################

def checkWin(gameboard,boardsize):
    """This function checks which win state the user has met and prints which one is matched"""
#If statement to say which win state is correct and then return the correct one    
    if win1(gameboard) or win2(gameboard) or win3(gameboard) or win4(gameboard) or win5(gameboard) or win6(gameboard) or win7(gameboard) or win8(gameboard):                
#Prints what the checkwin is in the .format style        
        print('checkWin is {}'.format(checkWin))
        return True
    else:        
        return False
        
        
       

    
       
            
#Calls checkwin with the updated game board, the main function body, and also the size of the board.     
checkWin(gameboard,3)
main()
