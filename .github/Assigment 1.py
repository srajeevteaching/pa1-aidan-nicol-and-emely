# Team Members: [Nicol Gutierrez]
# Course: CS151, Dr.Rajeev
# Date: [Sep 22/2021]
# Programming Assignment: 1
# Program Inputs: [lenght, height, weight]
# Program Outputs: [area, paints, primer]

width=float(input("please give width in feet"))
lenght=float(input("please give lenght in feet"))
height=float(input("please give height in feet"))
area=width*height*2+lenght*height*2+lenght*height
primer=area/200
paint=area/350
print("the total area in square feet is " +str(area ))
print ( "the amount of paint needed is %.2f gallons"%paint)
print ( "the amount of primer needed is %.2f gallons"%primer)





