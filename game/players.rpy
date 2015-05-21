#######################################

# PLAYER 1
#SAVE P1
label player1load:

    $ pid = 1
    $ pname = pname1
    
    $ hp = hp1
    $ mp = mp1
    $ xp = xp1
    $ cash = cash1
    $ items = items1
    
    jump game
    
#LOAD P1    
label player1save:
    $ pname1 = "1"
    $ maxp = maxpoints
    
    $ pid = 1
    $ pname = ""
    
    $ hp = 1
    $ mp = 1
    $ xp = 1
    $ cash = 1
    $ items = []
    
    hide screen playergridsave
    
    python:
        pname1 = renpy.input("Name Player 1:", length= 16, exclude='{äöüß§€°}')
        pname1 = pname1.strip()
        if not pname1:
            pname1 = "P1"


    jump createplayer


# PLAYER 2 
#SAVE P2
label player2load:

    $ pid = 2
    $ pname = pname2
    
    $ hp = hp2
    $ mp = mp2
    $ xp = xp2
    $ cash = cash2
    $ items = items2
    
    jump game
    
#LOAD P2
label player2save:
    $ pname2 = "2"
    $ maxp = maxpoints
    
    $ pid = 2
    $ pname = ""
    
    $ hp = 1
    $ mp = 1
    $ xp = 1
    $ cash = 1
    $ items = []
    
    hide screen playergridsave
    
    python:
        pname2 = renpy.input("Name Player 2:", length= 16, exclude='{äöüß§€°}')
        pname2 = pname2.strip()
        if not pname2:
            pname2 = "P2"

    jump createplayer
    


# PLAYER 3
#LOAD P3
label player3load:

    $ pid = 3
    $ pname = pname3
    
    $ hp = hp3
    $ mp = mp3
    $ xp = xp3
    $ cash = cash3
    $ items = items3
    
    jump game
    
#SAVE P3
label player3save:
    $ pname3 = "3"
    $ maxp = maxpoints
    
    $ pid = 3
    $ pname = ""
    
    $ hp = 1
    $ mp = 1
    $ xp = 1
    $ cash = 1
    $ items = []
    
    hide screen playergridsave
    
    python:
        pname3 = renpy.input("Name Player 3:", length= 16, exclude='{äöüß§€°}')
        pname3 = pname3.strip()
        if not pname3:
            pname3 = "P3"

    jump createplayer 
    


# PLAYER 4
#LOAD P4
label player4load:

    $ pid = 4
    $ pname = pname4
    
    $ hp = hp4
    $ mp = mp4
    $ xp = xp4
    $ cash = cash4
    $ items = items4
    
    jump game
#SAVE P4    
label player4save:
    $ pname4 = "4"
    
    $ maxp = maxpoints
    
    $ pid = 4
    $ pname = ""
    
    $ hp = 1
    $ mp = 1
    $ xp = 1
    $ cash = 1
    $ items = []
    
    hide screen playergridsave
    
    python:
        pname4 = renpy.input("Name Player 4:", length= 16, exclude='{äöüß§€°}')
        pname4 = pname4.strip()
        if not pname4:
            pname4 = "P4"

    jump createplayer
    
