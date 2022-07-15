name=input("Enter your name:")
want_play=input("Do you want to play the number guess game? (yes=y ,no=n)")
if(want_play=="y"):
    choose=int(input("choose one number between 1 - 10"))
    if(choose==4):
        print(" congragulation you won")
    else:
        print("you lost better luck next time")
else:
    print("ok")