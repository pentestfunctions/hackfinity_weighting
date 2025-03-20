# TryHackMe HackfinityBattle Scoreboard Analysis

This repository contains an analysis of the TryHackMe HackfinityBattle competition scoreboard. The data has been processed to rank players based on a weighted point system that accounts for challenge difficulty.

## Methodology

### Difficulty Weighting System
To provide a more accurate representation of skill, we applied a weighted point system based on challenge difficulty:

| Difficulty | Points | Multiplier |
|------------|--------|------------|
| Beginner   | 15     | 1.0x       |
| Easy       | 30     | 1.5x       |
| Medium     | 60     | 2.0x       |
| Hard       | 40/90  | 3.0x       |

**Weighted Score = Sum of (Task Points × Difficulty Multiplier)**

## Analysis Highlights

- **Top Performer**: Madridista777 leads with 3665.0 weighted points, demonstrating exceptional skill across all difficulty levels.
- **Difficulty Distribution**: The top performers consistently solved a high number of Hard challenges (5-7), demonstrating advanced skills.
- **Points vs. Weighted Score**: While some participants had similar raw points, their weighted scores varied significantly based on which challenges they solved.

## Complete Ranking

The following table displays all participants ranked by their weighted scores:

| Rank | Player | Raw Points | Weighted Points | Difficulty (B/E/M/H) |
|------|------------------|------------|----------------|---------------------|
| 1    | Madridista777    | 1755       | 3665.0         | 3/22/7/7            |
| 2    | cuddest          | 1605       | 3440.0         | 3/17/7/7            |
| 3    | brayanenorton    | 1665       | 3395.0         | 3/22/7/6            |
| 4    | kanakshilledar   | 1665       | 3395.0         | 3/22/7/6            |
| 5    | drkrowx          | 1665       | 3395.0         | 3/22/7/6            |
| 6    | the.flying.wolf  | 1665       | 3395.0         | 3/22/7/6            |
| 7    | whiterobber      | 1665       | 3395.0         | 3/22/7/6            |
| 8    | isl4r            | 1635       | 3350.0         | 3/21/7/6            |
| 9    | CypherWalt       | 1635       | 3350.0         | 3/21/7/6            |
| 10   | M04m1n3          | 1485       | 3245.0         | 1/16/6/7            |
| 11   | ztz              | 1455       | 3200.0         | 1/15/6/7            |
| 12   | skalvin          | 1455       | 2915.0         | 3/20/6/5            |
| 13   | AliyanKhan       | 1335       | 2850.0         | 1/17/6/5            |
| 14   | sh3nInfoSec      | 1395       | 2840.0         | 1/19/6/5            |
| 15   | ruur             | 1380       | 2780.0         | 2/20/5/5            |
| 16   | 0xl3v11          | 1275       | 2690.0         | 1/13/7/5            |
| 17   | mooder1          | 1230       | 2690.0         | 2/12/5/6            |
| 18   | amanyadav45      | 1260       | 2630.0         | 2/14/6/5            |
| 19   | mohamed.abwbakr1 | 1230       | 2555.0         | 2/15/5/5            |
| 20   | PetreRadu        | 1110       | 2510.0         | 2/8/5/6             |
| 21   | Tinonymous       | 1155       | 2465.0         | 3/10/6/5            |
| 22   | 610s             | 1140       | 2465.0         | 0/11/6/5            |
| 23   | ANUNNAKI         | 1005       | 2295.0         | 1/10/4/5            |
| 24   | Charlie00        | 1005       | 2165.0         | 1/12/3/5            |
| 25   | laughinghacker19 | 960        | 2135.0         | 0/9/4/5             |
| 26   | 8anksy           | 945        | 2130.0         | 1/7/6/4             |
| 27   | ritesh8975       | 870        | 2105.0         | 0/5/3/6             |
| 28   | bloman           | 975        | 2090.0         | 1/13/2/5            |
| 29   | HyggeHalcyon     | 960        | 2015.0         | 2/9/5/4             |
| 30   | vadapavhacker    | 1020       | 2000.0         | 2/12/6/3            |
| 31   | SirawitTH        | 960        | 1985.0         | 2/11/4/4            |
| 32   | hadsawww         | 945        | 1970.0         | 1/11/4/4            |
| 33   | NotHoudaifa      | 880        | 1935.0         | 2/13/1/5            |
| 34   | blackthorns      | 805        | 1890.0         | 1/7/3/5             |
| 35   | overllama        | 870        | 1830.0         | 0/12/4/3            |
| 36   | aelmo            | 810        | 1805.0         | 2/9/1/5             |
| 37   | MariosK1574      | 825        | 1745.0         | 3/8/3/4             |
| 38   | Erickalex        | 795        | 1740.0         | 1/7/5/3             |
| 39   | KernelKrise      | 720        | 1665.0         | 2/7/2/4             |
| 40   | xd3vnu11         | 805        | 1620.0         | 1/13/3/3            |
| 41   | Deepesh.Gautam   | 780        | 1565.0         | 0/11/3/3            |
| 42   | bhavya32         | 690        | 1410.0         | 2/8/4/2             |
| 43   | samdem           | 650        | 1385.0         | 0/9/1/3             |
| 44   | abelalmi         | 615        | 1380.0         | 1/7/2/3             |
| 45   | teebeeaf         | 675        | 1365.0         | 1/10/3/2            |
| 46   | OmarTamer0       | 615        | 1275.0         | 1/8/3/2             |
| 47   | KrzyCz           | 600        | 1275.0         | 2/5/4/2             |
| 48   | HARISH4n6        | 540        | 1275.0         | 0/5/2/3             |
| 49   | MoU              | 675        | 1265.0         | 1/10/3/2            |
| 50   | hamoshwani       | 525        | 1220.0         | 1/5/0/4             |
| 51   | NikhilCP         | 550        | 1215.0         | 0/7/2/3             |
| 52   | lostmyoldacc     | 535        | 1215.0         | 1/4/3/3             |
| 53   | iqlip            | 615        | 1170.0         | 1/9/4/1             |
| 54   | jojomojo1337     | 555        | 1160.0         | 1/7/1/3             |
| 55   | blast101         | 585        | 1155.0         | 1/6/5/1             |
| 56   | RJCyber          | 525        | 1050.0         | 1/11/0/2            |
| 57   | dxlerYT          | 525        | 1040.0         | 1/5/3/2             |
| 58   | Rxxxf            | 450        | 1010.0         | 0/4/1/3             |
| 59   | moe1n1           | 540        | 1005.0         | 0/11/2/1            |
| 60   | purusinghvi      | 450        | 1005.0         | 0/5/2/2             |
| 61   | Ankur.Gautam     | 465        | 975.0          | 3/6/1/2             |
| 62   | Haalloobim       | 450        | 945.0          | 0/9/0/2             |
| 63   | sky404           | 510        | 930.0          | 0/12/1/1            |
| 64   | cfalas           | 450        | 930.0          | 0/4/4/1             |
| 65   | 0Wl              | 375        | 885.0          | 1/2/2/2             |
| 66   | R4Y4N3           | 510        | 870.0          | 2/8/4/0             |
| 67   | hackerreal935    | 450        | 870.0          | 0/8/2/1             |
| 68   | P.S.Y            | 390        | 870.0          | 2/4/1/2             |
| 69   | Raoufard         | 450        | 855.0          | 2/7/2/1             |
| 70   | dawnhacker       | 420        | 855.0          | 0/5/3/1             |
| 71   | law.masud        | 435        | 840.0          | 1/7/2/1             |
| 72   | TomSteer         | 450        | 830.0          | 2/8/0/2             |
| 73   | worachat.smn     | 420        | 825.0          | 0/7/2/1             |
| 74   | NaZer0           | 345        | 810.0          | 1/3/1/2             |
| 75   | koyphshi         | 455        | 770.0          | 1/5/4/0             |
| 76   | KabylieBoys09    | 315        | 765.0          | 1/2/1/2             |
| 77   | AlphaBey         | 390        | 750.0          | 0/8/1/1             |
| 78   | Amqdou           | 360        | 705.0          | 0/7/1/1             |
| 79   | NEELPATEL        | 360        | 705.0          | 0/7/1/1             |
| 80   | Achrafness       | 250        | 705.0          | 0/1/0/3             |
| 81   | JustinApplegate  | 300        | 680.0          | 0/0/2/2             |
| 82   | izoubizou        | 240        | 660.0          | 0/0/1/2             |
| 83   | Revvv            | 300        | 645.0          | 0/3/2/1             |
| 84   | Henry6621        | 360        | 635.0          | 0/5/2/1             |
| 85   | ANONDGr          | 405        | 630.0          | 1/11/1/0            |
| 86   | Souvlakia        | 330        | 630.0          | 0/8/0/1             |
| 87   | itskarudo        | 300        | 615.0          | 0/5/1/1             |
| 88   | Seli             | 300        | 615.0          | 0/5/1/1             |
| 89   | AlinaPosea       | 360        | 600.0          | 0/8/2/0             |
| 90   | JackJack261      | 300        | 600.0          | 2/4/1/1             |
| 91   | sk00l            | 225        | 600.0          | 1/1/0/2             |
| 92   | ISHAYU           | 300        | 585.0          | 0/7/0/1             |
| 93   | 0xbnd            | 285        | 585.0          | 1/4/1/1             |
| 94   | Jackychan        | 285        | 585.0          | 1/4/1/1             |
| 95   | 0xd0lv3          | 345        | 575.0          | 1/6/1/1             |
| 96   | crashOverflow    | 300        | 570.0          | 0/2/4/0             |
| 97   | h00dy            | 290        | 545.0          | 0/5/0/1             |
| 98   | 4L4WN3.H4CK      | 275        | 545.0          | 1/2/1/1             |
| 99   | rbahloul         | 300        | 540.0          | 0/4/3/0             |
| 100  | CodeBreaker44    | 300        | 540.0          | 0/4/3/0             |
| 101  | ver3e            | 270        | 540.0          | 0/6/0/1             |
| 102  | R3v34lKro        | 270        | 540.0          | 0/6/0/1             |
| 103  | V0ight           | 315        | 525.0          | 1/6/2/0             |
| 104  | 4ymen            | 240        | 525.0          | 0/3/1/1             |
| 105  | wantet           | 240        | 525.0          | 0/3/1/1             |
| 106  | 0M4R             | 285        | 510.0          | 1/3/3/0             |
| 107  | mark.agudo       | 240        | 510.0          | 2/2/1/1             |
| 108  | jmsbaihi         | 285        | 480.0          | 1/5/2/0             |
| 109  | 0xA5h            | 210        | 480.0          | 0/2/1/1             |
| 110  | 0xkakash1        | 210        | 480.0          | 0/2/1/1             |
| 111  | n1tesh0x00       | 225        | 465.0          | 1/4/0/1             |
| 112  | Barszczyk        | 210        | 450.0          | 0/4/0/1             |
| 113  | ap425q           | 270        | 435.0          | 0/7/1/0             |
| 114  | Cyber.AI         | 270        | 435.0          | 0/7/1/0             |
| 115  | smmedislam       | 180        | 435.0          | 0/1/1/1             |
| 116  | Altelus          | 180        | 435.0          | 0/1/1/1             |
| 117  | Whotf.bunny      | 275        | 425.0          | 3/2/2/0             |
| 118  | Sutoroga         | 240        | 420.0          | 0/4/2/0             |
| 119  | nicl4ssic        | 255        | 405.0          | 1/6/1/0             |
| 120  | pawelsolowiej    | 180        | 405.0          | 0/3/0/1             |
| 121  | VeN0M            | 210        | 375.0          | 0/3/2/0             |
| 122  | Evangelospro     | 150        | 360.0          | 0/2/0/1             |
| 123  | momrulhasan      | 150        | 360.0          | 0/2/0/1             |
| 124  | n999             | 210        | 345.0          | 0/5/1/0             |
| 125  | 0utc4st          | 210        | 330.0          | 2/4/1/0             |
| 126  | Charlie01        | 210        | 330.0          | 2/4/1/0             |
| 127  | Lmog             | 195        | 315.0          | 1/4/1/0             |
| 128  | roshan.saw.1312  | 180        | 300.0          | 0/4/1/0             |
| 129  | youppi           | 90         | 270.0          | 0/0/0/1             |
| 130  | MohammadKYaseen  | 150        | 255.0          | 0/3/1/0             |
| 131  | deltabluejay     | 165        | 240.0          | 1/5/0/0             |
| 132  | vaty             | 150        | 225.0          | 0/5/0/0             |
| 133  | denzelsimatupang | 135        | 225.0          | 1/2/1/0             |
| 134  | WannaCry8        | 135        | 225.0          | 1/2/1/0             |
| 135  | YCF.xfg          | 100        | 210.0          | 0/2/0/1             |
| 136  | AndreiChiper     | 135        | 195.0          | 1/4/0/0             |
| 137  | ER0m1            | 140        | 185.0          | 0/3/0/0             |
| 138  | massco99         | 105        | 185.0          | 1/0/0/1             |
| 139  | loufa0           | 135        | 180.0          | 3/3/0/0             |
| 140  | mkara            | 120        | 180.0          | 0/4/0/0             |
| 141  | p4wnd4           | 105        | 180.0          | 1/1/1/0             |
| 142  | vjz3r            | 105        | 180.0          | 1/1/1/0             |
| 143  | Gratigo          | 90         | 170.0          | 0/0/0/1             |
| 144  | z3r0X0r          | 120        | 165.0          | 2/3/0/0             |
| 145  | anasnedjmeddine  | 90         | 165.0          | 0/1/1/0             |
| 146  | Qu1ck5h0t        | 90         | 165.0          | 0/1/1/0             |
| 147  | karmeen          | 90         | 165.0          | 0/1/1/0             |
| 148  | damoReduc        | 90         | 165.0          | 0/1/1/0             |
| 149  | sudoRooted       | 90         | 165.0          | 0/1/1/0             |
| 150  | PlatypusJovial   | 110        | 140.0          | 0/2/0/0             |
| 151  | Ironstone        | 90         | 135.0          | 0/3/0/0             |
| 152  | Rainyyy          | 90         | 135.0          | 0/3/0/0             |
| 153  | biplobrahman488  | 90         | 135.0          | 0/3/0/0             |
| 154  | dip.raj          | 75         | 135.0          | 1/0/1/0             |
| 155  | iklak            | 60         | 120.0          | 0/0/1/0             |
| 156  | 0xDuB            | 60         | 120.0          | 0/0/1/0             |
| 157  | VTXsideswipe     | 75         | 105.0          | 1/2/0/0             |
| 158  | bent0x           | 60         | 90.0           | 0/2/0/0             |
| 159  | Sh0z3n           | 60         | 90.0           | 0/2/0/0             |
| 160  | AvAl4nch         | 60         | 90.0           | 0/2/0/0             |
| 161  | RaphaelDJefe     | 60         | 90.0           | 0/2/0/0             |
| 162  | trustie.rity     | 60         | 90.0           | 0/2/0/0             |
| 163  | GinericaAlex     | 60         | 90.0           | 0/2/0/0             |
| 164  | anarchistx       | 45         | 60.0           | 1/1/0/0             |
| 165  | ziru             | 45         | 60.0           | 1/1/0/0             |
| 166  | AthenaGodess     | 45         | 60.0           | 1/1/0/0             |
| 167  | R4d14n7          | 45         | 45.0           | 3/0/0/0             |
| 168  | patriotviii      | 30         | 45.0           | 0/1/0/0             |
| 169  | dede13210        | 30         | 45.0           | 0/1/0/0             |
| 170  | pgglsjulil       | 30         | 45.0           | 0/1/0/0             |
| 171  | llatreche        | 30         | 45.0           | 0/1/0/0             |
| 172  | shayes20         | 30         | 45.0           | 0/1/0/0             |
| 173  | seishirah        | 30         | 45.0           | 0/1/0/0             |
| 174  | BL4CKD3VIL       | 30         | 45.0           | 0/1/0/0             |
| 175  | nadnine          | 30         | 45.0           | 0/1/0/0             |
| 176  | bl4ckwood        | 30         | 45.0           | 0/1/0/0             |
| 177  | Xyrax            | 30         | 45.0           | 0/1/0/0             |
| 178  | awakeningunquest | 30         | 45.0           | 0/1/0/0             |
| 179  | Hackertistic     | 30         | 45.0           | 0/1/0/0             |
| 180  | iftx             | 30         | 45.0           | 0/1/0/0             |
| 181  | Starman1         | 30         | 30.0           | 2/0/0/0             |
| 182  | S3c              | 15         | 15.0           | 1/0/0/0             |
| 183  | pkaba            | 15         | 15.0           | 1/0/0/0             |
| 184  | broodashah       | 15         | 15.0           | 1/0/0/0             |
| 185  | 6235a015f6432b004f230906 | 0  | 0.0            | 0/0/0/0             |
| 186  | 64070ecf531d88004f590193 | 0  | 0.0            | 0/0/0/0             |
| 187  | 662fef83009659aea696c883 | 0  | 0.0            | 0/0/0/0             |
| 188  | KaalBhairav1O8   | 0          | 0.0            | 0/0/0/0             |
| 189  | 61e8a27ddd3f3b00496505d9 | 0  | 0.0            | 0/0/0/0             |
| 190  | 65aa7304faebf698223aea57 | 0  | 0.0            | 0/0/0/0             |
| 191  | technoterror30   | 0          | 0.0            | 0/0/0/0             |
| 192  | 613c72a1cd28a80048e1dac3 | 0  | 0.0            | 0/0/0/0             |
| 193  | 640cd13326067c0056eb3509 | 0  | 0.0            | 0/0/0/0             |
| 194  | 67054c267e88c0eaa43aa725 | 0  | 0.0            | 0/0/0/0             |
| 195  | 643aa4a1d9452c0062052f4c | 0  | 0.0            | 0/0/0/0             |

## Understanding the Data

The B/E/M/H column represents the number of challenges solved at each difficulty level:
- B: Beginner (15 points)
- E: Easy (30 points)
- M: Medium (60 points)
- H: Hard (40/90 points)

## Script Information

This analysis was generated using a Python script that fetches data from the TryHackMe API, processes the scoreboard data, and calculates weighted scores based on challenge difficulty.

```python
# Sample of the key functionality
def get_difficulty_multiplier(score):
    if score == 15:  # Beginner
        return 1.0
    elif score == 30:  # Easy
        return 1.5
    elif score == 60:  # Medium
        return 2.0
    elif score in [40, 90]:  # Hard
        return 3.0
    else:
        return 1.0
```

---

*Last updated: March 21, 2025*






My personal TEAM RANKINGS

| Task # | Assignee | Points | Difficulty | Category |
|--------|----------|--------|------------|----------|
| 6.2 | n1tesh0x00 | 15 | Beginner | OSINT |
| 7 | h00dy | 30 | Easy | OSINT |
| 8 | iqlip | 60 | Medium | OSINT |
| 9 | iqlip | 15 | Beginner | Web |
| 10 | iqlip | 30 | Easy | Web |
| 11 | iqlip | 60 | Medium | Web |
| 12 | iqlip | 30 | Easy | Crypto |
| 13 | h00dy | 30 | Easy | Crypto |
| 14 | lostmyoldacc | 15 | Beginner | Red Teaming |
| 15 | iqlip | 30 | Easy | Red Teaming |
| 16 | iqlip | 30 | Easy | Red Teaming |
| 17 | iqlip | 30 | Easy | Blockchain |
| 18 | iqlip | 60 | Medium | Blockchain |
| 19 | lostmyoldacc | 30 | Easy | Game Hacking |
| 20 | lostmyoldacc | 30 | Easy | Game Hacking |
| 21.2 | n1tesh0x00 | 30 | Easy | LLM |
| 22 | n1tesh0x00 | 30 | Easy | LLM |
| 23 | n1tesh0x00 | 90 | Hard | IoT |
| 24 | n1tesh0x00 | 30 | Easy | Forensics |
| 25 | h00dy | 30 | Easy | Forensics |
| 26 | n1tesh0x00 | 30 | Easy | Forensics |
| 27 | h00dy | 30 | Easy | Forensics |
| 28 | lostmyoldacc | 90 | Hard | Forensics |
| 29 | h00dy | 90 | Hard | Forensics |
| 30 | iqlip | 30 | Easy | Crypto |
| 31 | iqlip | 30 | Easy | Crypto |
| 32 | lostmyoldacc | 30 | Easy | Binary Exploitation |
| 33 | iqlip | 30 | Easy | Binary Exploitation |
| 34 | iqlip | 30 | Easy | Cloud |
| 35 | h00dy | 30 | Easy | Cloud |
| 36 | lostmyoldacc | 60 | Medium | Cloud |
| 37.1 | h00dy | 50 | Hard | Red Teaming |
| 37.2 | lostmyoldacc | 40 | Hard | Red Teaming |
| 38 | lostmyoldacc | 30 | Easy | Reverse Engineering |
| 39 | iqlip | 90 | Hard | Reverse Engineering |
| 40 | iqlip | 60 | Medium | PWN |
| 42.1 | lostmyoldacc | 60 | Hard | Cloud |
| 42.2 | lostmyoldacc | 90 | Hard | Cloud |
| 42.3 | lostmyoldacc | 60 | Hard | Cloud |

## Task Distribution by Assignee
- **iqlip**: 14 tasks
- **lostmyoldacc**: 10 tasks
- **n1tesh0x00**: 6 tasks
- **h00dy**: 7 tasks

## Task Distribution by Difficulty
- **Beginner**: 4 tasks
- **Easy**: 20 tasks
- **Medium**: 5 tasks
- **Hard**: 8 tasks

## Task Distribution by Category
- **OSINT**: 3 tasks
- **Web**: 3 tasks
- **Crypto**: 4 tasks
- **Red Teaming**: 4 tasks
- **Blockchain**: 2 tasks
- **Game Hacking**: 2 tasks
- **LLM**: 2 tasks
- **IoT**: 1 task
- **Forensics**: 6 tasks
- **Binary Exploitation**: 2 tasks
- **Cloud**: 5 tasks
- **Reverse Engineering**: 2 tasks
- **PWN**: 1 task

## Workload Analysis by Points and Difficulty

### Points Calculation Method
To analyze the workload more accurately, I'll assign difficulty multipliers:
- Beginner: 1x multiplier
- Easy: 1.5x multiplier
- Medium: 2x multiplier
- Hard: 3x multiplier

### Assignee Workload Analysis

| Assignee | Raw Points | Weighted Points | Task Count | Avg Points/Task | Avg Weighted/Task |
|----------|------------|----------------|------------|-----------------|-------------------|
| iqlip | 510 | 855 | 14 | 36.4 | 61.1 |
| lostmyoldacc | 485 | 1027.5 | 10 | 48.5 | 102.8 |
| n1tesh0x00 | 225 | 382.5 | 6 | 37.5 | 63.8 |
| h00dy | 290 | 555 | 7 | 41.4 | 79.3 |

### Workload Percentage Distribution

#### Raw Points
```
iqlip: 33.9%
lostmyoldacc: 32.2%
n1tesh0x00: 15.0%
h00dy: 19.3%
```

Weighted Point System: I applied difficulty multipliers (Beginner: 1x, Easy: 1.5x, Medium: 2x, Hard: 3x) to calculate weighted contribution.
Weighted Points = Sum of (Task Points × Difficulty Multiplier)

#### Weighted Points (Accounting for Difficulty)
```
lostmyoldacc: 36.5%
iqlip: 30.3%
h00dy: 19.7%
n1tesh0x00: 13.6%
```

### Difficulty Breakdown by Assignee

| Assignee | Beginner | Easy | Medium | Hard |
|----------|----------|------|--------|------|
| iqlip | 2 | 8 | 3 | 1 |
| lostmyoldacc | 1 | 4 | 1 | 4 |
| n1tesh0x00 | 1 | 4 | 0 | 1 |
| h00dy | 0 | 4 | 0 | 3 |

### Key Observations
1. **lostmyoldacc** has the highest weighted contribution at 36.5% of total weighted points, despite having fewer tasks than iqlip
2. **iqlip** handles the most tasks (14) but with a lower average difficulty
3. **h00dy** has the second-highest average weighted points per task (79.3)
4. **n1tesh0x00** contributes the least in both raw and weighted measures, but maintains a solid average per task
