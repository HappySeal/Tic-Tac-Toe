turn=0
test=["a","_","_","_","_","_","_","_","_","_"]
print("",test[1:4],"\n",test[4:7],"\n",test[7:10])
while turn <= 5:
    print("Choose your move (1-9) ")
    move=int(input())
    while test[move] != "_":
        print("Choose another one")
        move=int(input())
    test[move]="X"
    print("",test[1:4],"\n",test[4:7],"\n",test[7:10],)
    turn=turn+1
    updown1=[test[1],test[4],test[7]]
    updown2=[test[2],test[5],test[8]]
    updown3=[test[3],test[6],test[9]]
    cross1=[test[1],test[5],test[9]]
    cross2=[test[3],test[5],test[7]]
    if test[1:4]==["X","X","X"] or test[4:7]==["X","X","X"] or test[7:10]==["X","X","X"] or updown1==["X","X","X"] or updown2==["X","X","X"] or updown3==["X","X","X"] or cross2==["X","X","X"] or cross1==["X","X","X"]:
        print("Player1 won!!")
        break
    if turn == 5:
        print("Draw!")
        break
    from random import randint
    movecpu=randint(1,9)
    while test[movecpu] != "_":
        movecpu=randint(1,9)
    test[movecpu]="O"
    movecpu=""
    move=""
    print("--------------------")
    print("",test[1:4],"\n",test[4:7],"\n",test[7:10])
    updown1=[test[1],test[4],test[7]]
    updown2=[test[2],test[5],test[8]]
    updown3=[test[3],test[6],test[9]]
    cross1=[test[1],test[5],test[9]]
    cross2=[test[3],test[5],test[7]]
    if test[1:4]==["O","O","O"] or test[4:7]==["O","O","O"] or test[7:10]==["O","O","O"] or updown1==["O","O","O"] or updown2==["O","O","O"] or updown3==["O","O","O"] or cross2==["O","O","0"] or cross2==["O","O","O"]:
        print("Computer won!!")
        break
print("Press any key to continue")
exit=input()