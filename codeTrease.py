print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
navigate=   (input("Where you want to Go, Type 'Left' or 'Right'\n")).lower()

lake=0
color= 0

if navigate=='left':
    lake =   (input(print("You have Arrived a Lake Choose We will wait for Boat or Swim\n Type 'Boat' or 'Swim'"))).lower()
    if lake=='boat':
        color =    (input(print("Choose Color 'Yellow', 'Blue' or 'Red'\n "))).lower()
    if color== 'yellow':
            print('''                                  ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"''')
        
    else:
        print("You got Killed\nGame Over")
