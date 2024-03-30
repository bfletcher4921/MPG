mpg= float(input("Enter the MPG of the vehicle:"))
cost = float(input("Enter the fuel cost per gallon:"))
distance_1 = float(input("Enter distance one:"))
distance_2 = float(input("Enter distance two:"))
distance_3 = float(input("Enter distance three:"))
short_trip = (distance_1/mpg)*cost
med_trip = (distance_2/mpg)*cost
long_trip = (distance_3/mpg)*cost

print(f'The cost of distance one cost: ${short_trip:.2f}. The cost of distance two cost:${med_trip:.2f}, The cost of distance three cost:${long_trip:.2f}')
