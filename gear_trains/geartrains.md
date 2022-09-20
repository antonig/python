# GearTrains 
selects gears for gear trains giving the required gear rate 
gears are selected  from a reduced set described in a text file. I made the app  with Meccano in mind but 
gears.txt can be edited with the gears available in other contexts.
Gears text is a list of number of teeths available min to max, separed by \n

The programa allows the input of gear rates in floating point, in fractions or as a Python formula (=math.sqrt(2)) to be evaluated
It gives first a continuous fraction developement for the rate, then tries to combine all gears avaiable in 1, 2, 3 and 4 stages and returns only the results giving the lesser error.

The distance between axles is a main constraint in Meccano, but the program does'nt consider it. 
Tricks as using a differential to get an average between two rates are not considered