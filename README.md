pbaCape
=======

BeagleBone Cape for pba ("Platz-Beregnungs-Anlage")

For software see https://github.com/fknittel/pba

## TestBoard
For testing the basic circuit a test layout was developed. It was soldered together and used with one original relay (same as used for the "real" thing).

## Prototype RC1
The RC1 schematics were send of for PCB manufacturing. The bare board was soldered manually. The prototype is still used for the "real" thing. But:
- Some resistor values were choosen borderline. Only 4 out of 6 outputs worked as advertised. (Values corrected in V05.sch)
  Wrong relay behaviour can be seen here: https://www.youtube.com/watch?v=9P7xhbd6JEQ 
  Correctly it should be: https://www.youtube.com/watch?v=5yiceOrfvFM 
- Some GPIOs (P8_39, 41, 43, 45) that were chosen first interfered with "boot"-pins of the BeagelBone. Thus, the board would not boot properly.
  These were manually corrected via wire bridges to be P8_17, 18, 28 and 30 respectively. (Also corrected in V05.sch)
- There is no internet connection (currently). Thus, no time information is available. A real time clock (RTC) was needed. It was manually soldered. 
  (Not yet corrected in schematics.)

## Code
The code here is only for simple testing purposes. It uses PyBBIO (https://github.com/alexanderhiam/PyBBIO/wiki).