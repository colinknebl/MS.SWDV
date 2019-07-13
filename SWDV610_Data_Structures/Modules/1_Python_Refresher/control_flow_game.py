import random
 
Ammo = 5
breakOut = 0
 
Shoot = input("Type '1' to shoot or '2' to quit: ")
             
while breakOut == 0:
    if Shoot == '1':
        HitOrMiss = random.randrange(1, 3)
        if HitOrMiss == 1:
            print("You missed!\n")
            Ammo = Ammo - 1
            if Ammo < 1:
                breakOut = breakOut + 1
                print("You're out of Ammo.")
            else:
                Shoot = input("Type '1' to shoot or '2' to quit: ")
                         
        if HitOrMiss == 2:
            print("You hit the target!\n")
            Ammo = Ammo - 1
            if Ammo < 1:
                breakOut = breakOut + 1
                print("You're out of Ammo.")
            else:
                Shoot = input("Type '1' to shoot or '2' to quit: ")
                 
    elif Shoot == '2':
        breakOut = breakOut + 1
        print("You stopped the game.")
         
         
    else:
        print("You may only type '1' or '2'.\n")
        Shoot = input("Type '1' to shoot or '2' to quit: ")  