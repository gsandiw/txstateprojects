# Trichords

# Prime Form: (forte name, distinct forms, [normal name])
forms = {\
  #Intervals / Dyads
  (0,1) : ("Undefined", 24, "Minor Second"),
  (0,2) : ("Undefined", 24, "Major Second"),
  (0,3) : ("Undefined", 24, "Minor Third"),
  (0,4) : ("Undefined", 24, "Major Third"),
  (0,5) : ("Undefined", 24, "Fourth"),
  (0,6) : ("Undefined", 24, "Tritone"),  
  #Trichords
  (0,1,2) : ("3-1",  12),
  (0,1,3) : ("3-2",  24),
  (0,1,4) : ("3-3",  24),
  (0,1,5) : ("3-4",  24),
  (0,1,6) : ("3-5",  24),
  (0,2,4) : ("3-6",  12),
  (0,2,5) : ("3-7",  24),
  (0,2,6) : ("3-8",  24),
  (0,2,7) : ("3-9",  12),
  (0,3,6) : ("3-10", 12),
  (0,3,7) : ("3-11", 24),
  (0,4,8) : ("3-12",  4),
  #Tetrachords
  (0,1,2,3) : ("4-1",   12),
  (0,1,2,4) : ("4-2",   24),
  (0,1,3,4) : ("4-3",   12),
  (0,1,2,5) : ("4-4",   24),
  (0,1,2,6) : ("4-5",   24),
  (0,1,2,7) : ("4-6",   12),
  (0,1,4,5) : ("4-7",   12),
  (0,1,5,6) : ("4-8",   12),
  (0,1,6,7) : ("4-9",    6),
  (0,2,3,5) : ("4-10",  12),
  (0,1,3,5) : ("4-11",  24),
  (0,2,3,6) : ("4-12",  24),
  (0,1,3,6) : ("4-13",  24),
  (0,2,3,7) : ("4-14",  24),
  (0,1,4,6) : ("4-Z15", 24),
  (0,1,5,7) : ("4-16",  24),
  (0,3,4,7) : ("4-17",  12),
  (0,1,4,7) : ("4-18",  24),
  (0,1,4,8) : ("4-19",  24),
  (0,1,5,8) : ("4-20",  12),
  (0,2,4,6) : ("4-21",  12),
  (0,2,4,7) : ("4-22",  24),
  (0,2,5,7) : ("4-23",  12),
  (0,2,4,8) : ("4-24",  12),
  (0,2,6,8) : ("4-25",   6),
  (0,3,5,8) : ("4-26",  12),
  (0,2,5,8) : ("4-27",  24),
  (0,3,6,9) : ("4-28",   3),
  (0,1,3,7) : ("4-Z29", 12),
  #Pentachords
  (0,1,2,3,4) : ("5-1",   12),
  (0,1,2,3,5) : ("5-2",   24),
  (0,1,2,4,5) : ("5-3",   24),
  (0,1,2,3,6) : ("5-4",   24),
  (0,1,2,3,7) : ("5-5",   24),
  (0,1,2,5,6) : ("5-6",   24),
  (0,1,2,6,7) : ("5-7",   24),
  (0,2,3,4,6) : ("5-8",   12),  
  (0,1,2,4,6) : ("5-9",   24),  
  (0,1,3,4,6) : ("5-10",  24),  
  (0,2,3,4,7) : ("5-11",  24),  
  (0,1,3,5,6) : ("5-Z12", 12),  
  (0,1,2,4,8) : ("5-13",  24),  
  (0,1,2,5,7) : ("5-14",  24),  
  (0,1,2,6,8) : ("5-15",  12),  
  (0,1,3,4,7) : ("5-16",  24),  
  (0,1,3,4,8) : ("5-Z17", 12),  
  (0,1,4,5,7) : ("5-Z18", 24),  
  (0,1,3,6,7) : ("5-19",  24),  
  (0,1,5,6,8) : ("5-20",  24),  
  (0,1,4,5,8) : ("5-21",  24),  
  (0,1,4,7,8) : ("5-22",  12),
  (0,2,3,5,7) : ("5-23",  24),
  (0,1,3,5,7) : ("5-24",  24),
  (0,2,3,5,8) : ("5-25",  24),
  (0,2,4,5,8) : ("5-26",  24),
  (0,1,3,5,8) : ("5-27",  24),
  (0,2,3,6,8) : ("5-28",  24),
  (0,1,3,6,8) : ("5-29",  24),
  (0,1,4,6,8) : ("5-30",  24),
  (0,1,3,6,9) : ("5-31",  24),
  (0,1,4,6,9) : ("5-32",  24),
  (0,2,4,6,8) : ("5-33",  12),
  (0,2,4,6,9) : ("5-34",  12),
  (0,2,4,7,9) : ("5-35",  12),
  (0,1,2,4,7) : ("5-Z36", 24),
  (0,3,4,5,8) : ("5-Z37", 12),
  (0,1,2,5,8) : ("5-Z38", 24),
  #Hexachords
  (0,1,2,3,4,5)  : ("6-1",   12),
  (0,1,2,3,4,6)  : ("6-2",   24),
  (0,1,2,3,5,6)  : ("6-Z3",  24),
  (0,1,2,4,5,6)  : ("6-Z4",  12),
  (0,1,2,3,6,7)  : ("6-5",   24),
  (0,1,2,5,6,7)  : ("6-Z6",  12),
  (0,1,2,6,7,8)  : ("6-7",    6),
  (0,2,3,4,5,7)  : ("6-8",   12),
  (0,1,2,3,5,7)  : ("6-9",   24),
  (0,1,3,4,5,7)  : ("6-Z10", 24),
  (0,1,2,4,5,7)  : ("6-Z11", 24),
  (0,1,2,4,6,7)  : ("6-Z12", 24),
  (0,1,3,4,6,7)  : ("6-Z13", 12),
  (0,1,3,4,5,8)  : ("6-14",  24),
  (0,1,2,4,5,8)  : ("6-15",  24),
  (0,1,4,5,6,8)  : ("6-16",  24),
  (0,1,2,4,7,8)  : ("6-Z17", 24),
  (0,1,2,5,7,8)  : ("6-18",  24),
  (0,1,3,4,7,8)  : ("6-Z19", 24),
  (0,1,4,5,8,9)  : ("6-20",   4),
  (0,2,3,4,6,8)  : ("6-21",  24),
  (0,1,2,4,6,8)  : ("6-22",  24),
  (0,2,3,5,6,8)  : ("6-Z23", 12),
  (0,1,3,4,6,8)  : ("6-Z24", 24),
  (0,1,3,5,6,8)  : ("6-Z25", 24),
  (0,1,3,5,7,8)  : ("6-Z26", 12),
  (0,1,3,4,6,9)  : ("6-27",  24),
  (0,1,3,5,6,9)  : ("6-Z28", 12),
  (0,2,3,6,7,9)  : ("6-Z29", 12),
  (0,1,3,6,7,9)  : ("6-30",  12),
  (0,1,4,5,7,9)  : ("6-31",  24),
  (0,2,4,5,7,9)  : ("6-32",  12),
  (0,2,3,5,7,9)  : ("6-33",  24),
  (0,1,3,5,7,9)  : ("6-34",  24),
  (0,2,4,6,8,10) : ("6-35",   2),
  (0,1,2,3,4,7)  : ("6-Z36", 24),
  (0,1,2,3,4,8)  : ("6-Z37", 12),
  (0,1,2,3,7,8)  : ("6-Z38", 12),
  (0,2,3,4,5,8)  : ("6-Z39", 24),
  (0,1,2,3,5,8)  : ("6-Z40", 24),
  (0,1,2,3,6,8)  : ("6-Z41", 24),
  (0,1,2,3,6,9)  : ("6-Z42", 12),
  (0,1,2,5,6,8)  : ("6-Z43", 24),
  (0,1,2,5,6,9)  : ("6-Z44", 24),
  (0,2,3,4,6,9)  : ("6-Z45", 12),
  (0,1,2,4,6,9)  : ("6-Z46", 24),
  (0,1,2,4,7,9)  : ("6-Z47", 24),
  (0,1,2,5,7,9)  : ("6-Z48", 12),
  (0,1,3,4,7,9)  : ("6-Z49", 12),
  (0,1,4,6,7,9)  : ("6-Z50", 12),
  #Septachords
  (0,1,2,3,4,5,6)  : ("7-1",   12),
  (0,1,2,3,4,5,7)  : ("7-2",   24),
  (0,1,2,3,4,5,8)  : ("7-3",   24),
  (0,1,2,3,4,6,7)  : ("7-4",   24),
  (0,1,2,3,5,6,7)  : ("7-5",   24),
  (0,1,2,3,4,7,8)  : ("7-6",   24),
  (0,1,2,3,6,7,8)  : ("7-7",   24),
  (0,2,3,4,5,6,8)  : ("7-8",   12),
  (0,1,2,3,4,6,8)  : ("7-9",   24),
  (0,1,2,3,4,6,9)  : ("7-10",  24),
  (0,1,3,4,5,6,8)  : ("7-11",  24),
  (0,1,2,3,4,7,9)  : ("7-Z12", 12),
  (0,1,2,4,5,6,8)  : ("7-13",  24),
  (0,1,2,3,5,7,8)  : ("7-14",  24),
  (0,1,2,4,6,7,8)  : ("7-15",  12),
  (0,1,2,3,5,6,9)  : ("7-16",  24),
  (0,1,2,4,5,6,9)  : ("7-Z17", 12),
  (0,1,4,5,6,7,9)  : ("7-Z18", 24),
  (0,1,2,3,6,7,9)  : ("7-19",  24),
  (0,1,2,5,6,7,9)  : ("7-20",  24),
  (0,1,2,4,5,8,9)  : ("7-21",  24),
  (0,1,2,5,6,8,9)  : ("7-22",  12),
  (0,2,3,4,5,7,9)  : ("7-23",  24),
  (0,1,2,3,5,7,9)  : ("7-24",  24),
  (0,2,3,4,6,7,9)  : ("7-25",  24),
  (0,1,3,4,5,7,9)  : ("7-26",  24),
  (0,1,2,4,5,7,9)  : ("7-27",  24),
  (0,1,3,5,6,7,9)  : ("7-28",  24),
  (0,1,2,4,6,7,9)  : ("7-29",  24),
  (0,1,2,4,6,8,9)  : ("7-30",  24),
  (0,1,3,4,6,7,9)  : ("7-31",  24),
  (0,1,3,4,6,8,9)  : ("7-32",  24),
  (0,1,2,4,6,8,10) : ("7-33",  12),
  (0,1,3,4,6,8,10) : ("7-34",  12),
  (0,1,3,5,6,8,10) : ("7-35",  12),
  (0,1,2,3,5,6,8)  : ("7-Z36", 24),
  (0,1,3,4,5,7,8)  : ("7-Z37", 12),
  (0,1,2,4,5,7,8)  : ("7-Z38", 24),
  #Octachords
  (0,1,2,3,4,5,6,7)  : ("8-1",   12),
  (0,1,2,3,4,5,6,8)  : ("8-2",   24),
  (0,1,2,3,4,5,6,9)  : ("8-3",   12),
  (0,1,2,3,4,5,7,8)  : ("8-4",   24),
  (0,1,2,3,4,6,7,8)  : ("8-5",   24),
  (0,1,2,3,5,6,7,8)  : ("8-6",   12),
  (0,1,2,3,4,5,8,9)  : ("8-7",   12),
  (0,1,2,3,4,7,8,9)  : ("8-8",   12),
  (0,1,2,3,6,7,8,9)  : ("8-9",    6),
  (0,2,3,4,5,6,7,9)  : ("8-10",  12),
  (0,1,2,3,4,5,7,9)  : ("8-11",  24),
  (0,1,3,4,5,6,7,9)  : ("8-12",  24),
  (0,1,2,3,4,6,7,9)  : ("8-13",  24),
  (0,1,2,4,5,6,7,9)  : ("8-14",  24),
  (0,1,2,3,4,6,8,9)  : ("8-Z15", 24),
  (0,1,2,3,5,7,8,9)  : ("8-16",  24),
  (0,1,3,4,5,6,8,9)  : ("8-17",  12),
  (0,1,2,3,5,6,8,9)  : ("8-18",  24),
  (0,1,2,4,5,6,8,9)  : ("8-19",  24),
  (0,1,2,4,5,7,8,9)  : ("8-20",  12),
  (0,1,2,3,4,6,8,10) : ("8-21",  12),
  (0,1,2,3,5,6,8,10) : ("8-22",  24),
  (0,1,2,3,5,7,8,10) : ("8-23",  12),
  (0,1,2,4,5,6,8,10) : ("8-24",  12),
  (0,1,2,4,6,7,8,10) : ("8-25",   6),
  (0,1,3,4,5,7,8,10) : ("8-26",  12),
  (0,1,2,4,5,7,8,10) : ("8-27",  24),
  (0,1,3,4,6,7,9,10) : ("8-28",   3),
  (0,1,2,3,5,6,7,9)  : ("8-Z29", 24),
  #Nonachords
  (0,1,2,3,4,5,6,7,8)  : ("9-1",   12),
  (0,1,2,3,4,5,6,7,9)  : ("9-2",   24),
  (0,1,2,3,4,5,6,8,9)  : ("9-3",   24),
  (0,1,2,3,4,5,7,8,9)  : ("9-4",   24),
  (0,1,2,3,4,6,7,8,9)  : ("9-5",   24),
  (0,1,2,3,4,5,6,8,10) : ("9-6",   12),
  (0,1,2,3,4,5,7,8,10) : ("9-7",   24),
  (0,1,2,3,4,6,7,8,10) : ("9-8",   24),
  (0,1,2,3,5,6,7,8,10) : ("9-9",   12),
  (0,1,2,3,4,6,7,9,10) : ("9-10",  12),
  (0,1,2,3,5,6,7,9,10) : ("9-11",  24),
  (0,1,2,4,5,6,8,9,10) : ("9-12",   4),
  #Decachords (?)
  (0,1,2,3,4,6,7,8,9,10) : ("Undefined", 24),
  (0,1,2,3,4,5,7,8,9,10) : ("Undefined", 24),
  (0,1,2,3,4,5,6,8,9,10) : ("Undefined", 24),
  (0,1,2,3,4,5,6,7,9,10) : ("Undefined", 24),
  (0,1,2,3,4,5,6,7,8,10) : ("Undefined", 24),
  (0,1,2,3,4,5,6,7,8,9 ) : ("Undefined", 24),
  #Undecachords (?)
  (0,1,2,3,4,5,6,7,8,9,10)    : ("Undefined", 24),
  #Didecachords (?)
  (0,1,2,3,4,5,6,7,8,9,10,11) : ("Undefined", 24)
}