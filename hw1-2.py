#city_distances = [5,25, 15, 10, 15]
# fuel [1,2,1,0,3]
# mpg 10
#from collections import defaultdict


def myhamilton(city_distances, fuel_at_gas_station, car_mpg):
    number_of_cities = len(city_distances)
    # print(number_of_cities)
   # my_dict = defaultdict(int)
    my_dict = {}
    fuel_remaining = 0
    for i in range(number_of_cities):  # for every starting city in city_distances
        #starting_fuel = fuel_at_gas_station[i]
        #print(" **** We are looking at city ******* ", i, )
        fuel_left_over = 0
        for j in range(i, i + number_of_cities):  # we will go on a round trip
            if j > number_of_cities-1:  # if we are out of bounds, then reset
                spot = j % number_of_cities
                #print("j is greater, the new index is ", spot)
            else:
                spot = j
            miles_of_gas_filled = car_mpg * fuel_at_gas_station[spot]
            miles_to_travel = city_distances[spot]
            fuel_left_over = miles_of_gas_filled - miles_to_travel
            #print(" now looking at from city,", spot, " to city ", spot + 1)
            if fuel_left_over >= 0:
                my_dict[spot] = fuel_left_over
            else:
                #print("ah we coudn't make it!! we were down", fuel_left_over)
                my_dict[spot] = fuel_left_over
                break
    max_key = 0
    for key_value in my_dict:  # city number_INDEX: gallons
        #print(key_value, my_dict[key_value])
        #print(key_value, my_dict.get(key_value))
        if my_dict[key_value] > my_dict[max_key]:
            max_key = key_value
    print("city", max_key + 1, " at index: ", max_key,
          " has left over: ", my_dict.get(max_key))
    return max_key
    #


myhamilton([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)
# output: city 5  at index:  4  has left over:  15
