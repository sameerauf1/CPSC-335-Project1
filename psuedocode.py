#city_distances = [5,25, 15, 10, 15]
# fuel [1,2,1,0,3]
# mpg 10
# initialize empty dictionary
# intialize fuel_left_over = 0
# loop through each starting city
#  nest another loop for a round trip each starting city
#  calculate number of miles travelable, miles_of_gas_filled = miles_per_gallon * gallons_at_gas_station
#  grab miles to travel from that city in city_distances lists
#  calculate fuel left over by subtracting miles_of_gas_filled - miles_to_travel
# if fuel left over is ever negative, break out of nested loop
# if fuel is greater than or equal to 0, add starting city and fuels_left_over
# loop through dictioanry and find max miles left and return key value
