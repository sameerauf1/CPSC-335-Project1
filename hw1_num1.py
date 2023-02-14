#city_distances = [5,25, 15, 10, 15]
# fuel [1,2,1,0,3]
# mpg 10
def myhamilton(city_distances, fuel_at_gas_station, car_mpg):
    number_of_cities = len(city_distances)
    # print(number_of_cities)
    my_dict = {}  # will store city index : fuels left over
    fuel_left_over = 0
    for i in range(number_of_cities):  # for every starting city in city_distances
        # we will need to keep track of fuel_left_over for every city in a round trip
        fuel_left_over = 0
        # we will go on a round trip, starting from city i
        for j in range(i, i + number_of_cities):
            if j > number_of_cities-1:  # if we are out of bounds index, then reset to numbers 0 to number_of_cities
                myindex = j % number_of_cities
            else:
                myindex = j
            # number of miles that can be travveled from gas fill
            miles_of_gas_filled = car_mpg * fuel_at_gas_station[myindex]

            # number of miles to travel
            miles_to_travel = city_distances[myindex]
            # number of miles still left with remaining gas
            fuel_left_over = miles_of_gas_filled - miles_to_travel

            if fuel_left_over >= 0:
                my_dict[myindex] = fuel_left_over
            else:  # if fuel is ever negative, then we couldn't do a round trip, so exit this starting city
                break
    max_key = 0
    for key_value in my_dict:  # city number_INDEX: gallons, loop through gallons too see max
        if my_dict[key_value] > my_dict[max_key]:
            max_key = key_value
    print("city", max_key + 1, " at index: ", max_key,
          " has left over: ", my_dict.get(max_key))
    return max_key


myhamilton([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)
# output: city 5  at index:  4  has left over:  15
