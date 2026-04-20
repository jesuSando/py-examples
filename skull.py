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
""",
"""
         _.,,._
     _,d$$$$$$$$io,
   ,d$S$$$$S$$$$$SIi.
  dSS$SIS$$$$$$$$$$Si:
 jIS$$?I?$$$$$$$$SSS$Si:
 SI$$III::d$$S?iI$$$S7°?.
:iS$II:·jS°¨    ?$S7   i
:iSSI::·$I      j$$L   :
·:?i:.,d$$k,_.,d$$7¨?p;$
 ·iI:`°?$$$S?I?$$7   $$?
   ?:.  ?S$?SII$$L.,J$"`
    `.   ¨  :IS$S$IISk
            ·:i?i:?:·?
                 "' '
""",
"""
        _.,,,._
    ,.oi$$$$$$Sio,
  ,i$$S$$$$$$$$SSSIk:
 dISS$$$$$$$SZ$$$$SSIk
jIS$$$$$$$$$SII?$$$SSIi
SSS$$$$SS$$SSI:i$$7°°?S.
?SS$$$$$$SS?I:·d$'    ?'
:SS$$$$$S?Ii:·J$S    ,$L
 ?IS$$SIIi:·.,?$$$up%?$'
  ?ISIb,¨`°"?S$$°°¨,d$:
   `°?$?'    '?°k.:iIS$k
      ¨'        `?.:iI$?
                 "·"° ^
"""


]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.2)