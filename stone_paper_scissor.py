player1 = (input(" For player 1 choose one from stone,paper,scissor:"))
player2 = (input("For player 2 choose one from stone paper scissor:"))
if(player1 == "stone" and player2 == "paper"):
    print("player2 won")
elif(player1 == "stone" and player2 == "scissor"):
    print("player1 won")
elif(player1 == "stone" and player2 == "stone"):
    print("draw")
elif(player1 == "paper" and player2 == "stone"):
    print("player1 won")
elif(player1 == "paper" and player2 == "paper"):
    print("Draw")
elif(player1 == "paper" and player2 == "scissor"):
    print("player2 won")
elif(player1 == "scissor" and player2 == "stone"):
    print("player2 won")
elif(player1 == "scissor" and player2 == "paper"):
    print("player1 won")
elif(player1 == "scissor" and player2 == "scissor"):
    print("Draw")
