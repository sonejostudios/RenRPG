# screens grid SAVE
screen playersave:
     vbox at top:
        null height 10
        grid 2 2 at truecenter:
            textbutton "[pname1]" action [Jump("player1save")] align (1.0 , 0.0) style "p_button"
            textbutton "[pname2]" action [Jump("player2save")] align (1.0 , 0.0) style "p_button"
            textbutton "[pname3]" action [Jump("player3save")] align (1.0 , 0.0) style "p_button"
            textbutton "[pname4]" action [Jump("player4save")] align (1.0 , 0.0) style "p_button"


screen playergridsave:   
    vbox at top:
        null height 160
        text "{size=30}Max Points: [maxp]{/size}" align (0.5 , 0.0)
        null height 20
        
        grid 3 5 at truecenter:
            
            ## HP
            if  hp >= 1:
                textbutton "-1 hp" action [SetVariable("hp", (hp-1)), SetVariable("maxp", (maxp)+1)] align (1.0 , 0.0) style "m_button"
            else:
                null
                
            text "[hp]" align (0.5 , 0.5)
            
            if  maxp >= 1:
                textbutton "+1 hp" action [SetVariable("hp", (hp+1)), SetVariable("maxp", (maxp)-1)] align (0.0 , 0.0) style "m_button"
            else:
                null
            
            ## MP
            if  mp >= 1:            
                textbutton "-1 mp" action [SetVariable("mp", (mp-1)), SetVariable("maxp", (maxp)+1)] align (1.0 , 0.0) style "m_button"
            else:
                null
                
            text "[mp]" align (0.5 , 0.5)
            
            if  maxp >= 1:
                textbutton "+1 mp" action [SetVariable("mp", (mp+1)), SetVariable("maxp", (maxp)-1)] align (0.0 , 0.0) style "m_button"
            else:
                null
    
            ## XP
            if  xp >= 1:
                textbutton "-1 xp" action [SetVariable("xp", (xp-1)), SetVariable("maxp", (maxp)+1)] align (1.0 , 0.0) style "m_button"
            else:
                null
                
            text "[xp]" align (0.5 , 0.5)
            if  maxp >= 1:
                textbutton "+1 xp" action [SetVariable("xp", (xp+1)), SetVariable("maxp", (maxp)-1)] align (0.0 , 0.0) style "m_button"
            else:
                null
             
            ## CASH
            if  cash >= 1:            
                textbutton "-1 cash" action [SetVariable("cash", (cash-1)), SetVariable("maxp", (maxp)+1)] align (1.0 , 0.0) style "m_button"
            else:
                null
            text "[cash]" align (0.5 , 0.5)
            
            if  maxp >= 1:
                textbutton "+1 cash" action [SetVariable("cash", (cash+1)), SetVariable("maxp", (maxp)-1)] align (0.0 , 0.0) style "m_button"
            else:
                null
                
            ## ITEMS
            if  items != []:            
                textbutton "- item" action [Jump("removeitem")] align (1.0 , 0.0) style "m_button"
            else:
                null
            
            text "items:" align (0.5 , 1.0)
            
            textbutton "+ item" action [Jump("additem")] align (0.0 , 0.0) style "m_button"


        
        null height 10
        text "[items]" align (0.5 , 0.0)
        
        

  

