# X O Game Begin !

d =["start"," "," "," "," "," "," "," "," "," ","end"]

row1 = "| {} | {} | {} |".format(d[1],d[2],d[3])
row2 = "| {} | {} | {} |".format(d[4],d[5],d[6])
row3 = "| {} | {} | {} |".format(d[7],d[8],d[9])

name1 = input("Enter Player 1 Name(x,o) : ")
name2 = input("Enter Player 2 Name(x,o) : ")

def game():
    row1 = "| {} | {} | {} |".format(d[1],d[2],d[3])
    row2 = "| {} | {} | {} |".format(d[4],d[5],d[6])
    row3 = "| {} | {} | {} |".format(d[7],d[8],d[9])
    print(" --- --- ---")
    print(row1)
    print(" --- --- ---")
    print(row2)
    print(" --- --- ---")
    print(row3)
    print(" --- --- ---")     

# x is even and o is odd
values = [2,4]
hori= [1,2,3]
verti = [1,4,7]

endgame = True
count = 1

while endgame:
    game()
    
    count = count + 1
    k = count%2

    if k == 0:
        user = int(input("Enter postion Player "+name1+": "))
        d[user] = "X"
    elif k != 0 :
        user = int(input("Enter postion Player "+name2+": "))
        d[user] = "O"
    print()

    for i in values:
        if d[5] == d[5+i] and d[5] == d[5-i] and d[5] != " ":
            endgame = False

    for i in hori:
        if d[i] == d[i+3] and d[i] == d[i+6] and d[i] != " ":
            endgame = False

    for i in verti:
        if d[i] == d[i+1] and d[i] == d[i+2] and d[i] != " ":
            endgame = False
       
game()

if k == 0:
    print("X - Wins !")
elif k != 0:
    print("O - Wins !")


input("Press Enter To exit! ")
    
            
    
