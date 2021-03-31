# bounce.py
#
# Exercise 1.5
height = 100 #initial height of the drop in meters
bounce = 3/5 #rebound bounce height of each drop
#What is the height of the bounce for the first 10 bounces?

bounce_num = 1
while bounce_num < 11:
    print(bounce_num, " ",round((height * bounce), 4))
    height=height*bounce
    bounce_num += 1