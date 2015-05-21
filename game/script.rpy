# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bgwhite = "#ffffff"
image bgblack = "#000000"
image bgskin = "#e5f1e5"
image txtcolor = "#cbe86b"
image framecolor = "#1c140d"
image bgcolor2 = "#707070"
image logo = "logo.png"



init:
# button style
    style m_button is button:
        xminimum 133
        xmaximum 133
        yminimum 60
        ymaximum 60
        
    style p_button is button:
        xminimum 200
        xmaximum 200
        yminimum 60
        ymaximum 60
        
    style w_button is button:
        xminimum 400
        xmaximum 400
        yminimum 60
        ymaximum 60
    
    style c_button is button:
        xminimum 60
        xmaximum 60
        yminimum 60
        ymaximum 60
        
#transition    
    $ flash = Fade(.05,0,.75,color="fff")
    $ flash2 = Fade(0,0,.75,color="fff")
        
#variables
    $ additem = ""
    $ maxp = 0
    $ maxpoints = 16
    $ gmode = 0 # 0 = play, 1 = create
    

# playervar
    $ pid = 0
    $ pname = ""
    $ hp = 1
    $ mp = 1
    $ xp = 1
    $ cash = 1
    $ items = []
    
    
# player1
    $ pid1 = 1
    $ pname1 = "1"
    $ hp1 = 1
    $ mp1 = 1
    $ xp1 = 1
    $ cash1 = 1
    $ items1 = []
    
# player2
    $ pid2 = 1
    $ pname2 = "2"
    $ hp2 = 1
    $ mp2 = 1
    $ xp2 = 1
    $ cash2 = 1
    $ items2 = []
    
# player3
    $ pid3 = 3
    $ pname3 = "3"
    $ hp3 = 1
    $ mp3 = 1
    $ xp3 = 1
    $ cash3 = 1
    $ items3 = []
    
# player4
    $ pid4 = 4
    $ pname4 = "4"
    $ hp4 = 1
    $ mp4 = 1
    $ xp4 = 1
    $ cash4 = 1
    $ items4 = []
    
            
#dice
    $ adddice = ""
    $ dicethrow = 0
    $ dice1 = ["1", "2", "3", "4", "5", "6"]
    $ dice2 = ["1", "2", "3", "4", "5", "6"]
    $ dicesetname = "Dice"
    
    #$ dice1 = ["1","2"]
    #$ dice2 = []
    
    
    
# dice slots
    
    $ slot1n = "Normal Set"
    $ slot1d1 = ["1", "2", "3", "4", "5", "6"]
    $ slot1d2 = ["1", "2", "3", "4", "5", "6"]
    
    $ slot2n = "Yes/No Set"
    $ slot2d1 = ["yes", "no"]
    $ slot2d2 = []
    
    $ slot3n = "Elements Set"
    $ slot3d1 = ["fire", "water", "earth", "air"]
    $ slot3d2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    
    $ slot4n = "Noise and Velocity Set"
    $ slot4d1 = ["booooom!", "clac!", "vrrrrr", "tshhhh", "toc toc", "ding dong", "pssss.."]
    $ slot4d2 = ["very slow","slow","normal","fast","very fast"]



    
#####################################

# The game starts here.
label start:
    show bgcolor2
    
    hide screen playergrid
    hide screen autosave
    hide screen playerchoice
    hide screen playergridsave
    hide screen playersave
    hide text
    
    show logo:
        xalign 0.5
        yalign 0.2
        
    #show text "{size=16}v. 0.1{/size}" at center
    
    
    menu:
        "Play":
            jump player1load
        "Create Players":
            #jump createplayer
            #jump player1save
            jump firstcreate
        "Dice Manager":
            jump dicemanager
        "":
            pass
            
        "Save / Load":
            jump save
            
        "About":
            jump about
        
        "Quit Game":
            return

        
#########################################
# PLAY

label game:

    hide logo
    hide text
    hide text2

    show screen playergrid
    show screen playerchoice
    show screen autosave
    
    $ gmode = 0 # set game mode to play
    
    
    #menu items
    menu:
        
        "Throw [dicesetname]":
            jump dice
        
        "Change Dice":
            jump changedice

        "Exit Game":
            jump start
            
                
    
    
####################################    
# CREATE PLAYER 

label firstcreate:
    hide logo
    hide text
    hide text2

    show screen playersave
    show text "{size=30}Choose a Player{/size}" at truecenter
    
    menu:
        "Exit":
            jump start
    
    jump player1save
     
     
label createplayer:
    show screen playergridsave
    show screen autosave
    show screen playersave
    
    hide text
    hide logo
    
    $ gmode = 1 # set game mode to create player
    
    
    #menu items
    menu:
        "Save all and Exit":
            hide text
            
            jump start
 




############################################
# ADD AND REMOVE ITEMS            
            
            
label additem:
            python:
                additem = renpy.input("Add an Item:",exclude='{äöüß§€°}')
                additem = additem.strip()
                if not additem:
                    additem = ""
            
            $ items.append(str(additem))
            
            if gmode == 0:
                jump game
            if gmode == 1:
                jump createplayer
            


label removeitem:
            python:
                additem = renpy.input("Remove an Item:",exclude='{äöüß§€°}')
                additem = additem.strip()
                if not additem:
                    additem = ""
            
            if additem in items:
                $ items.remove(str(additem))
            
            if gmode == 0:
                jump game
            if gmode == 1:
                jump createplayer
            

 
            
            
############
#save

label save:
    show screen save
    pause 200
    
    hide screen save
    jump start
    
    
    
    
    

###############
# About

label about:
    show bgcolor2
    hide logo
    show text "About:\nRenRPG is a small tool for RPG Game Masters.\n\nWith RenRPG you can create up 4 characters with health points (hp), magic points (mp), experience (xp), cash and items.\nYou can create as well up to 4 totally configurable dice sets.\nWith those tools send your players into incredibles adventures! \n\nCredits:\nCreated by Vincent Rateau\nat Sonejo Studios\nwww.sonejo.net\n\nLicense:\nThis software is licensed\nunder the GPL v3.\n\nRenRPG was made with the RenPy script language.":
        xalign 0.5
        yalign 0.2

    menu:
        "Exit":
            hide text
            jump start
            


    
    
