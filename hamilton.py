# Project 1, Algorithm 1:
# Names: Samee Rauf, Victoria Parry
# CSUF-supplied email address: srauf@csu.fullerton.edu,

# Input data for algorithm:
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
car_mpg = 10


def myhamilton(city_distances, fuel_at_gas_station, car_mpg):
    number_of_cities = len(city_distances)
    # will store index of best city to start trip with, initializing with city 0
    bestCity = 0
    # looping through each starting city
    for i in range(number_of_cities):
        # for each round trip, we need to reset left over fuel to zero
        fuel_left_over = 0
        # looping through every city in a round trip from each starting city
        for j in range(i, i + number_of_cities):
            # if we are out of bounds index, then reset index to numbers from 0 to number_of_cities
            if j > number_of_cities-1:
                myindex = j % number_of_cities
            else:
                myindex = j
            # number of gallons filled at gas station
            gallons_filled_at_gas_station = fuel_at_gas_station[myindex]
            # total gallons from gas station and leftover from previous trip
            total_gallons = gallons_filled_at_gas_station + fuel_left_over
            # gallons needed to travel distance, (Miles)/(Miles/Gallons) = gallons
            gallons_needed_to_travel = city_distances[myindex] / car_mpg
            # number of gallons remaining after trip
            fuel_left_over = total_gallons - gallons_needed_to_travel
            # if our fuel is greater than or equal to 0 and we are at the last stop before our original city record city index
            if fuel_left_over >= 0 and myindex == i:
                if i == 0 and j == 0:  # edge case of first starting city and first trip in round trip, must ignore
                    continue
                # record index of bestCity with fuel>0
                bestCity = myindex
            # if fuel is ever negative, then we couldn't do a round trip, so move onto next starting city
            elif fuel_left_over < 0:
                break
    # finally return index of bestCity
    # print(bestCity)
    return bestCity


myhamilton(city_distances, fuel, car_mpg)
