#The game() function in a program lets a user play a game and returns the score as an 
# integer. You need to read a file “Hiscore.txt” which is either blank or contains
#  the previous Hi-score.
#  You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
#   creating a file named hiscore.txt
with open("hiscore.txt",'w') as f:
    pass
def game():
    return 4
score=game()    
with open("hiscore.txt") as f:
    hiscore=int(f.read())

if hiscore<score:
    with open("hiscore.txt",'w') as f:
        f.write(str(score))
