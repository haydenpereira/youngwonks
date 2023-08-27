

'''empty = True
turn = 'X'
board = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
while True:
    for i in board:
        if i % 3 == 0:
            print (i,':',board[i])
            print ()
        else:
            print (i,':',board[i],end = ' ')
    number = int(input('where do you want to place your marker  '))
    if board[number] == '':  
        if turn == 'X':
            board[number] = turn
            turn = 'O'
        else:
            board[number] = turn
            turn = 'X'
    else:
        print ('this spot has already been taken try again')
    
    if board[1] == board[2] == board[3] != '':
        print (board[1],'wins')
        
        break
    elif board[4] == board[5] == board[6] != '':
        print (board[4],'wins')
        break
    elif board[7] == board[8] == board[9] != '':
        print (board[7],'wins')
        break
    elif board[1] == board[4] == board[7] != '':
        print (board[1],'wins')
       
        break
    elif board[2] == board[5] == board[8] != '':
        print (board[2],'wins')
        break
    elif board[3] == board[6] == board[9] != '':
        print (board[3],'wins')
        break
    elif board[1] == board[5] == board[9] != '':
        print (board[1],'wins')
        
        break
    elif board[3] == board[5] == board[7] != '':
        print (board[3],'wins')
        break
    for i in board:
        if board[i] == '':
            empty = True
            break
        else:
            empty = False
    if empty == False:
        print ('it is a tie')
        break
    if board[1] != board[2] != board[3] != board[4] != board[5] != board[6] != board[7] != board[8] != board[9] != '':
        print ('it is a tie')'''