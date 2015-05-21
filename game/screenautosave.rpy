###########################################  
# screen autosave -> save values to player each 0.5 second
screen autosave:
        if pid == 1:
            timer 0.5 repeat True action [SetVariable("hp1", (hp))]
            timer 0.5 repeat True action [SetVariable("mp1", (mp))]
            timer 0.5 repeat True action [SetVariable("xp1", (xp))]
            timer 0.5 repeat True action [SetVariable("cash1", (cash))]
            timer 0.5 repeat True action [SetVariable("items1", (items))]
        if pid == 2:
            timer 0.5 repeat True action [SetVariable("hp2", (hp))]
            timer 0.5 repeat True action [SetVariable("mp2", (mp))]
            timer 0.5 repeat True action [SetVariable("xp2", (xp))]
            timer 0.5 repeat True action [SetVariable("cash2", (cash))]
            timer 0.5 repeat True action [SetVariable("items2", (items))]
        if pid == 3:
            timer 0.5 repeat True action [SetVariable("hp3", (hp))]
            timer 0.5 repeat True action [SetVariable("mp3", (mp))]
            timer 0.5 repeat True action [SetVariable("xp3", (xp))]
            timer 0.5 repeat True action [SetVariable("cash3", (cash))]
            timer 0.5 repeat True action [SetVariable("items3", (items))]
        if pid == 4:
            timer 0.5 repeat True action [SetVariable("hp4", (hp))]
            timer 0.5 repeat True action [SetVariable("mp4", (mp))]
            timer 0.5 repeat True action [SetVariable("xp4", (xp))]
            timer 0.5 repeat True action [SetVariable("cash4", (cash))]
            timer 0.5 repeat True action [SetVariable("items4", (items))]


