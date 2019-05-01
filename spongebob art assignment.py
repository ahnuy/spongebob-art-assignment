from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=900, height=800, background="turquoise")
screen.pack()
##SKY
y = 0
y2 = 30
skyOptions = ["#CCFF99","#C2FC9E","#B8FAA3","#ADF7A8","#A3F5AD","#99F2B2",\
              "#8FF0B8","#85EDBD","#7AEBC2","#70E8C7","#66E6CC","#5CE3D1",\
              "#52E0D6","#47DEDB","#3DDBE0","#33D9E6","#29D6EB","#1FD4F0",\
              "#14D1F5","#0ACFFA","#00CCFF"]
for sky in range (1,21):
    skyColour = (skyOptions[sky%21]) 
    screen.create_rectangle (0,y,905,y2, fill = skyColour, outline = skyColour)
    y = y + 30
    y2 = y2 + 30
##CLOUDS
for cloud in range (1,26):
    x = randint (75,200)
    y = randint (200,250)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#2DD2E1", outline = "#2DD2E1")
    y2 = randint (250,275)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#2EBCC9", outline = "#2EBCC9")
for cloud in range (1,31):
    x = randint (400,550)
    y = randint (100,150)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#3DD493", outline = "#3DD493")
    y2 = randint (150,175)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#36BB81", outline = "#36BB81")
for cloud in range (1,36):
    x = randint (650,800)
    y = randint (290,350)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#987ECA", outline = "#987ECA")
    y2 = randint (350,375)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#876DB7", outline = "#876DB7")
##PATRICK'S HOME
screen.create_polygon (-120,650,110,400,225,650, fill = "#463939", outline = "#3E342A", smooth = "true") #354A83
#SAND
screen.create_rectangle (0,600,905,805, fill = "blanchedalmond", outline = "blanchedalmond")
sandOptions = ["burlywood","saddlebrown","cornsilk"]
for sand in range (1,1750):
    sandColour = choice (sandOptions)
    x = randint (0,900)
    y = randint (600,800)
    s = randint (1,3)
    screen.create_oval (x,y,x+s,y+s,fill = sandColour, outline = sandColour)
##BUBBLES
for bubbles in range (1,75):
    x = randint (-5,905)
    y = randint (-5,580)
    s = randint (17,33)
    screen.create_oval (x,y,x+s,y+s, outline = "white")
    if s <23:
        screen.create_oval (x+3,y+3,x+6,y+6, fill = "white", outline = "white")
    else:
        screen.create_oval (x+5,y+5,x+10,y+10, fill = "white", outline = "white")
##PATRICK
##body
screen.create_polygon (259,156,239,170,176,404,144,433,80,487,40,586,53,616,82,603,139,526,131,558,131,580,200,640,354,633,427,595,415,456,351,411,331,365,291,197, fill = "#F7ABAD", outline = "#F25A43", width = 3, smooth = "true")
##left foot
screen.create_polygon (145,690,171,747,196,761,215,749,227,723,230,685, fill = "#F7ABAD", outline = "#F25A43", width = 3, smooth = "true")
##right foot
screen.create_polygon (277,679,306,740,327,755,349,746,365,715,377,677, fill = "#F7ABAD", outline = "#F25A43", width = 3, smooth = "true")
##eyes
screen.create_oval (203,313,257,396, fill = "#FFFFFF", outline = "#000002", width = 3)
screen.create_oval (257,313,315,396, fill = "#FFFFFF", outline = "#000002", width = 3)
##pupils
screen.create_oval (234,347,251,370, fill = "#000002")
screen.create_oval (267,347,282,368, fill = "#000002")
##eyebrows
screen.create_polygon (246,281,245,286,250,290,240,300,225,305,225,298,222,299,231,287, fill = "#000002", smooth = "true")
screen.create_polygon (268,276,283,279,295,290,290,292,292,297,278,292,268,283,272,282, fill = "#000002", smooth = "true")
##smile
screen.create_line (206,398,197,402,194,412, fill = "#000002", smooth = "true", width = 3)
screen.create_line (315,390,320,397,328,404, fill = "#000002", smooth = "true", width = 3)
screen.create_line (197,402,217,418,245,427,260,428,278,425,304,416,315,410,322,399, fill = "#000002", smooth = "true", width = 3)
##belly button
screen.create_line (258,582,265,585,271,580, fill = "#000002", smooth = "true", width = 3)
screen.create_line (254,591,264,595,276,588, fill = "#000002", smooth = "true", width = 3)
##pants
screen.create_polygon (130,585,127,603,129,631,137,659,138,698,173,709,204,710,237,701,240,685,285,683,285,697,313,705,346,703,383,692,388,640,392,575,263,615, fill = "#D6DF22",outline = "#000002", width = 3, smooth = "true")
screen.create_polygon (131,581,265,615,383,579,382,588,263,620,130,593, fill = "#D6DF22", outline = "#000002", width = 3, smooth = "true")
screen.create_line (225,680,261,689,297,677, fill = "#000002", smooth = "true", width = 3)
##pattern on pants
screen.create_polygon (132,631,142,635,146,647,137,656, fill = "#B292C4", outline = "#737EBC", width = 2, smooth = "true")
screen.create_polygon (141,677,158,669,171,682,166,705,141,700, fill = "#B292C4", outline = "#737EBC", width = 2, smooth = "true")
screen.create_polygon (206,610,213,642,234,634,241,642,231,659,254,671,279,659,271,645,276,638,299,648,306,610,257,617, fill = "#B292C4", outline = "#737EBC", width = 2, smooth = "true")
screen.create_polygon (387,652,372,662,362,655,347,675,355,699,381,691, fill = "#B292C4", outline = "#737EBC", width = 2, smooth = "true")
##randomly places freckles on patrick
for freckleBelly in range (1,8):
    x = randint (155,370)
    y = randint (445,575)
    s = randint (5,8)
    screen.create_oval (x,y,x+s,y+s, fill = "#F25A43", outline = "#F25A43")
for freckleArm in range (1,3):
    x = randint (60,95)
    y = randint (540, 575)
    s = randint (5,7)
    screen.create_oval (x,y,x+s,y+s, fill = "#F25A43", outline = "#F25A43")
for freckleHead in range (1,4):
    x = randint (235,280)
    y = randint (200,270)
    s = randint (4,6)
    screen.create_oval (x,y,x+s,y+s, fill = "#F25A43", outline = "#F25A43")
for freckleLeg in range (1,2):
    x = randint (180,210)
    y = randint (720,740)
    randint (2,5)
    screen.create_oval (x,y,x+s,y+s, fill = "#F25A43", outline = "#F25A43")

##SPONGEBOB
##arm
screen.create_polygon (593,583,591,639,595,646,600,657,600,670,596,682,585,687,579,689,575,685,570,683,576,664,570,651,575,640,575,590, fill = "#FEF46E", outline = "#000002", width = 2, smooth = "true")
screen.create_line (585,687,582,680,587,672,588,664, fill = "#000002", width = 2, smooth = "true")
screen.create_line (575,685,577,679,580,672,580,666, fill = "#000002", width = 2, smooth = "true")
screen.create_line (583,650,588,667,595,661,590,648, fill = "#000002", width = 2, smooth = "true")
##sleeve
screen.create_polygon (584,548,595,559,599,569,601,578,602,592,575,592, fill = "#FFFFFF", outline = "#000002", width = 3)
##shirt
screen.create_rectangle (382,568,579,604, fill = "#FFFFFF", outline = "#000002", width = 4)
screen.create_line (427,575,462,602,481,573, fill = "#000002", width = 2)
screen.create_line (490,578,505,600,540,572, fill = "#000002", width = 2)
##legs
screen.create_polygon (424,663,427,688,433,691,438,688,439,663, fill = "#FEF46E", outline = "#000002", width = 2)
screen.create_polygon (518,663,518,685,524,688,529,685,529,662, fill = "#FEF46E", outline = "#000002", width = 2)
##socks
screen.create_polygon (427,688,433,691,438,688,439,729,426,729, fill = "#FFFFFF", outline = "#000002", width = 2)
screen.create_polygon (518,685,524,688,529,685,529,728,518,730, fill = "#FFFFFF", outline = "#000002", width = 2)
##stripes on socks
screen.create_line (427,698,433,701,438,698, fill = "#5389C7", width = 2)
screen.create_line (427,706,433,709,438,706, fill = "#EF1D26", width = 2)
screen.create_line (518,695,524,698,529,695, fill = "#5389C7", width = 2)
screen.create_line (518,703,524,706,529,703, fill = "#EF1D26", width = 2)
##shoes
screen.create_oval (395,728,431,765, fill = "#000002")
screen.create_polygon (419,730,422,725,427,724,430,729,436,728,439,725,439,720,448,727,450,736,449,742,450,751,432,756,431,746, fill = "#000002", smooth = "true")
screen.create_polygon (431,749,433,755,429,754, fill = "#8C979D", outline = "#000002")
screen.create_oval (405,737,416,745, fill = "#FFFFFF")
screen.create_oval (532,728,561,762, fill = "#000002")
screen.create_polygon (543,762,534,757,528,745,522,753,507,748,514,740,508,732,516,722,522,728,527,726,531,724,536,726,542,734, fill = "#000002", smooth = "true")
screen.create_polygon (530,751,528,745,522,751, fill = "#8C979D", outline = "#000002")
screen.create_oval (542,734,553,741, fill = "#FFFFFF")
##pants
screen.create_polygon (412,644,409,660,420,664,431,666,444,664,453,660,448,644, fill = "#BA7731", outline = "#000002", width = 3)
screen.create_polygon (509,644,504,656,513,664,525,666,536,664,549,660,547,644, fill = "#BA7731", outline = "#000002", width = 3)
screen.create_rectangle (382,604,579,645, fill = "#BA7731", width = 4)
##black rectangles on pants
x = 390
x2 = 420
for rectangle in range (1,5):
    screen.create_rectangle (x,615,x2,625, fill = "#000002")
    x = x + 50
    x2 = x2 + 50
##tie
screen.create_polygon (483,593,468,623,482,636,496,623, fill = "#EE1C25", outline = "#000002", width = 2)
screen.create_oval (474,565,493,600, fill = "#EE1C25", outline = "#000002", width = 2)
##body
screen.create_polygon (354,351,359,394,354,412,363,434,361,457,369,483,365,503,374,524,370,539,374,\
                       555,371,575,394,577,415,583,436,578,460,583,480,579,499,582,521,577,542,580,\
                       557,577,584,580,584,553,594,532,590,489,606,452,612,441,607,416,614,395,608,\
                       376,613,349,586,353,559,346,529,353,503,346,481,353,457,347,431,354,405,347,\
                       384,354, fill = "#FFF56F", outline = "#899030", width = 4, smooth = "true")
##sponge holes
screen.create_oval (376,364,403,407, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (373,420,388,442, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (388,525,397,536, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (392,542,408,567, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (575,375,590,400, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (565,525,580,550, fill = "#BABD18", outline = "#BABD18")
screen.create_oval (548,550,555,561, fill = "#BABD18", outline = "#BABD18")
##eyes
screen.create_oval (475,395,559,478, fill = "#FFFFFF", outline = "#000002", width = 3)
screen.create_oval (398,398,482,482, fill = "#FFFFFF", outline = "#000002", width = 3)
##pupils
screen.create_oval (439,426,468,454, fill = "#44C7F5", outline = "#000002", width = 2)
screen.create_oval (497,426,525,454, fill = "#44C7F5", outline = "#000002", width = 2)
screen.create_oval (446,432,461,447, fill = "#000002")
screen.create_oval (502,432,518,447, fill = "#000002")
##nose
screen.create_polygon (476,478,470,460,482,450,494,458,495,474,490,481, fill = "#FFF56F", width = 2, smooth = "true")
screen.create_line (476,478,470,460,482,450,494,458,495,474,490,481, fill = "#000002", width = 3, smooth = "true")
##eyelashes
screen.create_line (422,400,418,392, fill = "#000002", width = 3)
screen.create_line (441,397,442,384, fill = "#000002", width = 3)
screen.create_line (460,402,465,390, fill = "#000002", width = 3)
screen.create_line (504,398,499,386, fill = "#000002", width = 3)
screen.create_line (525,395,526,382, fill = "#000002", width = 3)
screen.create_line (544,404,548,391, fill = "#000002", width = 3)
##mouth
screen.create_polygon (392,483,484,510,575,481,545,537,480,556,419,536, fill = "#743236", outline = "#000002", width = 3, smooth = "true")
##tongue
screen.create_polygon (443,546,462,533,480,543,501,535,517,546,492,555,465,553, fill = "#F8ACAE", outline = "#000002", width = 3, smooth = "true")
##teeth
screen.create_polygon (455,501,476,503,476,525,451,521, fill = "#FFFFFF", outline = "#000002", width = 3)
screen.create_polygon (488,503,508,502,511,523,488,523, fill = "#FFFFFF", outline = "#000002", width = 3)
##chin line
screen.create_line (448,560,480,568,510,562, fill = "#F8AAA6", smooth = "true", width = 3)
##randomly places freckles on spongebob
for leftFreckles in range (1,4):
    x = randint (380,395)
    y = randint (460,475)
    screen.create_oval (x,y,x+5,y+5, fill = "#DD5C3D", outline = "#DD5C3D")
for rightFreckles in range (1,4):
    x = randint (560,575)
    y = randint (460,475)
    screen.create_oval (x,y,x+5,y+5, fill = "#DD5C3D", outline = "#DD5C3D")
##PATRICK AGAIN
screen.create_polygon (611,432,575,500,600,525,625,500, fill = "#F7ABAD", outline = "#F25A43", width = 3, smooth = "true")

screen.update()
