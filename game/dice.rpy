###################################
# dice

#PLAY DICE
label dice:
    hide screen playergrid
    hide screen autosave
    hide screen playerchoice
    hide screen playergridsave
    hide screen playersave
    
    call diceanim from _call_diceanim
    
    jump dicemenu


label dicemenu:
    with flash
    menu:
        "Throw Dice A" if dice1 != []:
            call dice1anim from _call_dice1anim
        
        "Throw Dice B" if dice2 != []:
            call dice2anim from _call_dice2anim
        
        "Throw Dice A & B" if dice1 != [] and dice2 != []:
            call diceanim from _call_diceanim_1

        "Exit":
            jump game
    
    jump dicemenu
    
    
#CREATE DICE
label createdice:
    hide screen playergrid
    hide screen autosave
    hide screen playerchoice
    hide screen playergridsave
    hide screen playersave
    
    hide logo

    show text "A\n[dice1]\n\nB\n[dice2]":
        xalign 0.5
        yalign 0.05
    
    menu:
        "+ Side on A":
            python:
                adddice = renpy.input("Add Dice Side:",exclude='{äöüß§€°}')
                adddice = adddice.strip()
                if not adddice:
                    adddice = ""
            
            $ dice1.append(str(adddice))
            
            jump createdice
            
            
        "- Side on A" if dice1 != []:
            python:
                adddice = renpy.input("Remove Dice Side:",exclude='{äöüß§€°}')
                adddice = adddice.strip()
                if not adddice:
                    adddice = ""
            
            if adddice in dice1:
                $ dice1.remove(str(adddice))
            
            jump createdice
            
        "Delete A" if dice1 != []:
            $ dice1 = []
            jump createdice
            
            
        "":
            pass
            
        "+ Side on B":
            python:
                adddice = renpy.input("Add Side on B:",exclude='{äöüß§€°}')
                adddice = adddice.strip()
                if not adddice:
                    adddice = ""
            
            $ dice2.append(str(adddice))
            
            jump createdice
            
            
        "- Side on B" if dice2 != []:
            python:
                adddice = renpy.input("Remove Side on B:",exclude='{äöüß§€°}')
                adddice = adddice.strip()
                if not adddice:
                    adddice = ""
            
            if adddice in dice2:
                $ dice2.remove(str(adddice))
            
            jump createdice
            
        
            
        "Delete B" if dice2 != []:
            $ dice2 = []
            jump createdice
            
        
        "":
            pass
        
        
        "Store Dice Set":
            jump dicepresets
            
        
        "Exit":
            jump dicemanager
            
            
            
            
# DICE ANIM
label diceanim:

    if dice1 == [] and dice2 == []:
        centered "No Dice to Play!"
        jump game
    
    if dice1 == []:
        jump dice2anim
    if dice2 == []:
        jump dice1anim
        
    
    pause 0.1

    $ random1 = renpy.random.choice(dice1)
    show text "{size=40}[random1]{/size}" at Position(xalign=0.5, yalign=0.2)
    
    $ random2 = renpy.random.choice(dice2) 
    show text "{size=40}[random2]{/size}" at Position(xalign=0.5, yalign=0.4) as text2
    
    $ dicethrow += 1
        

    if dicethrow <= 5:
        jump diceanim

    else:
        $ dicethrow = 0
        return
    
    
label dice1anim:


    pause 0.1

    $ random1 = renpy.random.choice(dice1)   
    show text "{size=40}[random1]{/size}" at Position(xalign=0.5, yalign=0.2)
    
    $ dicethrow += 1

    

    if dicethrow <= 5:
        jump dice1anim

    else:
        $ dicethrow = 0
        return
        

label dice2anim:

        
    pause 0.1


    $ random2 = renpy.random.choice(dice2)    
    show text "{size=40}[random2]{/size}" at Position(xalign=0.5, yalign=0.4) as text2
    
    $ dicethrow += 1
    

    if dicethrow <= 5:
        jump dice2anim

    else:
        $ dicethrow = 0
        return
        


        
########
# dice manager

label dicemanager:
    
    hide logo

    show text "A\n[dice1]\n\nB\n[dice2]":
        xalign 0.5
        yalign 0.05
    
    menu:
    
        "Create New":
            $ dice1 = []
            $ dice2 = []
            jump createdice
            
        "Edit Set":
            jump createdice


        "":
            pass
        
        "Load Slot 1 - [slot1n]":
            $ dice1 = slot1d1
            $ dice2 = slot1d2
            $ dicesetname = slot1n
            jump dicemanager
            
        "Load Slot 2 - [slot2n]":
            $ dice1 = slot2d1
            $ dice2 = slot2d2
            $ dicesetname = slot2n
            jump dicemanager
            
        "Load Slot 3 - [slot3n]":
            $ dice1 = slot3d1
            $ dice2 = slot3d2
            $ dicesetname = slot3n
            jump dicemanager
        
        "Load Slot 4 - [slot4n]":
            $ dice1 = slot4d1
            $ dice2 = slot4d2
            $ dicesetname = slot4n
            jump dicemanager
            
        "":
            pass


        "Reset":
            $ dice1 = ["1", "2", "3", "4", "5", "6"]
            $ dice2 = ["1", "2", "3", "4", "5", "6"]
            $ dicesetname = "Default Set"
            jump dicemanager
        
        
        "Exit":
            hide text
            jump start



###################

# store dice set

label dicepresets:
    
    show text "A\n[dice1]\n\nB\n[dice2]":
        xalign 0.5
        yalign 0.05

    menu:

        "Store to Slot 1 - [slot1n]":
            $ slot1d1 = []
            $ slot1d2 = []
            
            $ slot1d1 = dice1
            $ slot1d2 = dice2
            
            python:
                slot1n = renpy.input("Name Slot 1:",exclude='{äöüß§€°}')
                slot1n = slot1n.strip()
                if not slot1n:
                    slot1n = "Dice Set 1"
            
            $ dicesetname = slot1n
            hide text
            show text "[slot1n] stored to Slot 1 !" at truecenter
            pause 1
            jump dicemanager
            
        
        "Store to Slot 2 - [slot2n]":
            $ slot2d1 = []
            $ slot2d2 = []
            
            $ slot2d1 = dice1
            $ slot2d2 = dice2
            
            python:
                slot2n = renpy.input("Name Slot 2:",exclude='{äöüß§€°}')
                slot2n = slot2n.strip()
                if not slot2n:
                    slot2n = "Dice Set 2"
            
            $ dicesetname = slot2n
            hide text
            show text "[slot2n] stored to Slot 2 !" at truecenter
            pause 1
            jump dicemanager
            
        
        "Store to Slot 3 - [slot3n]":
            $ slot3d1 = []
            $ slot3d2 = []
            
            $ slot3d1 = dice1
            $ slot3d2 = dice2
            
            python:
                slot3n = renpy.input("Name Slot 3:",exclude='{äöüß§€°}')
                slot3n = slot3n.strip()
                if not slot3n:
                    slot3n = "Dice Set 3"
            
            $ dicesetname = slot3n
            hide text
            show text "[slot3n] stored to Slot 3 !" at truecenter
            pause 1
            jump dicemanager
            
        "Store to Slot 4 - [slot4n]":
            $ slot4d1 = []
            $ slot4d2 = []
            
            $ slot4d1 = dice1
            $ slot4d2 = dice2
            
            python:
                slot4n = renpy.input("Name Slot 4:",exclude='{äöüß§€°}')
                slot4n = slot4n.strip()
                if not slot4n:
                    slot4n = "Dice Set 4"
            
            $ dicesetname = slot4n
            hide text
            show text "[slot4n] stored to Slot 4 !" at truecenter
            pause 1
            jump dicemanager
            
        "":
            pass

        
        "Exit": 
            jump createdice
            
            
##########
# change dice in game

label changedice:
    hide text
    hide screen playerchoice
    hide screen playergrid
    
    show text "A\n[dice1]\n\nB\n[dice2]":
        xalign 0.5
        yalign 0.2
    

    menu:
        "[slot1n]":
            $ dice1 = slot1d1
            $ dice2 = slot1d2
            $ dicesetname = slot1n
            jump changedice
            
        "[slot2n]":
            $ dice1 = slot2d1
            $ dice2 = slot2d2
            $ dicesetname = slot2n
            jump changedice
            
        "[slot3n]":
            $ dice1 = slot3d1
            $ dice2 = slot3d2
            $ dicesetname = slot3n
            jump changedice
        
        "[slot4n]":
            $ dice1 = slot4d1
            $ dice2 = slot4d2
            $ dicesetname = slot4n
            jump changedice
        
        "":
            pass
            
        "Exit":
            jump game
