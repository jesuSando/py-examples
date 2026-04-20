import os
import time

frames =[
"""
            _.,,,._
       .,uS$$$$$$$SSI;,_
     ,d$$S$$$$S$$$SS$SIi:.
    J$S$$S7iIS$$S$$$S$SIi::
  .d$$$7iIIS$$$$$$SS$$SIIi:.
  $$$7:iIIS$S$$$SIS$$$$SIi::
  j ?k:iIISIS$S7IS$$$SSIIi::
.d? j$b:iIj$$S7IIS$$S7IIi::·
`$$u$$7·:j$$SiiIS$$$SIIIi::·
 biS$S$p,._?%u,`?S$SSIIi::·
dS$?Ii?°?$S?°"`^"4ISIii::·
°?$Sk.           ·?7I::·
^:?i:"`         .-'¨
""",
"""
           _.,,._
       ,p$$$$$$SSIi:·.
     :i$$$$$$S$$$SSSSi:.
   ,$$$$SSSS$$$$$7I$$$Ii:·
  j$$$$SS$$$$$$7IId$$$SIi:·
 ."I7¨`"°$$iI$7iIS$$$$SIi:·
 `·jI    `?L:iIIS$$$$SII::·
 ,°$$·    j$b:iIS$$S?iIi:·
 ? i$L,_.d$d$:ijSSSIiSi::·
 i.j$S?S$$$$S%u,°?iISi::·
.d$SIIi?°?$S?°`   ¨`¨.:'
:SIISIi:·          .-¨
·?i:·i?·^
""",
"""
         _.,,._
      ,d$$$$$SSIi:.
    ,$$$SSZS$$$SSIi:.
   j$$$$SZSS$$$$SSIIi:·
  j$$$$SS$$$$$SS7iiiII:·
 j°`^4SSI7°"°?$?:iiISIi:
 ?    $i?     ?$:iIS$Si:
jL _,$?iL    j7k:iIS$Si:
?$i$7  ?$b,_,d$$$.:Ii?:·
i$$?   :S$?i?$$$Siu,?•'
 ¨?I./,$?I:·'°?S?°' '
  IS$IS$SbI:·  ¨  .-
  :i?i:i?·i·
    ¨  ` `^
""",
"""
       _.,,.._
    ,d$$$$$SSIi:·
  ,$$$S$SS$$SSSIi:.
 j$$$$$$SS$$$SSSIi:.
 S$$$$SS$$$$$SSSIi:·
j?°`¨`?S$SI7°"°4SL::
?:     $$S?     `?i·
:L    j$?$k.     I7:
d$$b%d$:  `$b,.,dS:·
?SSIiSi·   S$?I?$Si
 ¨`?IS$L_,d$SIi:`°'
    ?$$$SS$SIi'
    i:?i:i?.•:
      ¨` `^
"""


]

for i in range(len(frames)):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frames[i])
    time.sleep(1)