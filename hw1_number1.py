# city_distances = [5,25, 15, 10, 15] **** THIS FILE IS FOR DEBUGGING, NOT FOR SUBMISSION ****
# fuel [1,2,1,0,3]
# mpg 10
def myhamilton(city_distances, fuel_at_gas_station, car_mpg):
    number_of_cities = len(city_distances)
    bestCity = 0  # will store index of best city to start with
    for i in range(number_of_cities):
        fuel_left_over = 0  # for each round trip, we need to reset left over fuel to zero
        # we must recognize this is beginning of the roundtrip
        print("starting city", i)
        for j in range(i, i + number_of_cities):
            if j > number_of_cities-1:  # if we are out of bounds index, then reset to numbers 0 to number_of_cities
                myindex = j % number_of_cities
            else:
                myindex = j
            # number of gallons filled at gas station
            print("******", myindex, "***")
            gallons_filled_at_gas_station = fuel_at_gas_station[myindex]
            # *print('gallons_filled_at_gas_station',gallons_filled_at_gas_station)
            # total gallons from gas station and leftover from previous trip
            total_gallons = gallons_filled_at_gas_station + fuel_left_over
            # *print('total gallonn', total_gallons)
            # gallons needed to travel distance ex. 5miles/10miles/gallon = .5 gallon
            gallons_needed_to_travel = city_distances[myindex] / car_mpg
            # *print("city distance", city_distances[myindex], "carmpg", car_mpg)
            # *print("gallons_needed_to_travel", gallons_needed_to_travel)
            ##print("gallons needed to travel distance", gallons_needed_to_travel)
            # number of gallons remaining after trip
            fuel_left_over = total_gallons - gallons_needed_to_travel
            # *print("fuel_left_over", fuel_left_over)

            # if our fuel is greater than or equal to 0 and we are at the last stop before our original city, add fuel left over to dict
            if fuel_left_over >= 0 and myindex == i:
                if i == 0 and j == 0:
                    continue
                print("we adding now to dict", "starting city",
                      i, "current city in round trip", myindex, "left over fuel", fuel_left_over)
                #my_dict[myindex] = fuel_left_over
                bestCity = myindex
            elif fuel_left_over < 0:   # if fuel is ever negative, then we couldn't do a round trip, so exit this starting city
                #print(   "a shucks we couldn't do a round trip, the fuel left over was", fuel_left_over, "at city ", myindex, "to city", myindex+1)
                break
        # if i == 1:
        #    return 0
            # fuel_left_over = 0  # reset fuel_left over for next round trip
    #a = my_dict.keys()
    print("the best city to start with is:", bestCity)
    return bestCity
    # for i in a:
    #    print(i)
    #print("printing a ", a)
    #print(my_dict.keys(), "my dict keys")
    # return (my_dict.keys())
    #print(my_dict.values(), "my dict values")


myhamilton([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)
# output: city 5  at index:  4  has left over:  15
