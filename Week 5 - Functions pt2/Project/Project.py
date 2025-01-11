###########################################################
# Computer Project #5
# function to open file:
#     Opens file and prepare file name for reading 
# function to make float:
#     Converts the string to a float
# function to get density:
#     Takes mass and radius of a spherical object in terms of Earth units and returns the
#     density
# function to get temp in range:
#     This function returns True if we estimate that the planet’s temp 
# function to get distance range:
#     Prompt for a distance. If the distance is less than zero or cannot be converted to
#     a float, print an error message and re-prompt
# function for the main program:
#     display opening message
#     open file by calling it
#     light year set to called get dist range function
#     variables set to their given values        
#     variables set to values to be compared to and edited
#     readline of file
#     loop to go through each file line:
#         variables set indexes after calling make_float 
#         condition to check if distance is usuable:
#             continue if conditions met
#         variables set indexes after calling make_float
#         conditions to add to number of stars and planets if true
#         condition to check if planet mass is greater than 0:
#             if true add to total mass and mass count:
#             condition calling temp_range to check if true:
#                if true habitable count increases by 1:
#                    conditions for determing rocky or gaseasous planet
#                    if rocky:
#                        change variables
#                else:
#                    if gaseas:
#                        change variables
#           calcualtion for average mass
#           close file
#           print statements with their formats
#           Condition if rocky distance is values:
#               if true print statement:
#           else:
#               print statement
#           Condition if gaseous distance is values:
#               if true print statement:
#           else:
#               print statement        
###########################################################





import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262


def open_file():
    ''' Opens file and prepare file name for reading '''
    prompt = input("Input data to open: ")
    while True:
        
        try:
            
            file1 = (prompt+".csv")
            file2 = open(file1, "r")
            return file2
        except FileNotFoundError:
            print("\nError: file not found.  Please try again.")
            prompt = input("Enter a file name: ") 

    return file2  

def make_float(s):
    ''' Converts the string to a float'''
    try:
        s = float(s)
    except ValueError:
        s = -1
    return s

def get_density(mass, radius):
    '''Takes mass and radius of a spherical object in terms of Earth units and returns the
        density'''
    if mass <= 0 or radius <= 0:
        return -1
    mass = EARTH_MASS * mass
    radius = EARTH_RADIUS * radius
    Volume = (4/3) * math.pi * (radius ** 3)
    Density = float(mass/Volume)
    return Density


def  temp_in_range(axis, star_temp, star_radius, albedo, lower_bound, upper_bound):
    '''This function returns True if we estimate that the planet’s temp'''
    if axis <= 0 or star_temp <= 0 or star_radius <= 0:
        return -1
    star_radius = star_radius * SOLAR_RADIUS
    axis = AU * axis
    planet_temp = star_temp * ((star_radius/(2 * axis))**(0.5)) * ((1-albedo)** 0.25)
    if lower_bound <= planet_temp <= upper_bound:
        return True
    elif planet_temp < 0:
        return False
    return False

def get_dist_range():
    '''Prompt for a distance. If the distance is less than zero or cannot be converted to
        a float, print an error message and re-prompt'''
    Prompt = input("\nEnter maximum distance from Earth (light years): ")
    while True:
        try:
           Prompt = float(Prompt)
           if Prompt < 0:
                print("\nError: Distance needs to be greater than 0.")
                Prompt = input("\nEnter maximum distance from Earth (light years): ")
                
           else:
                return Prompt
        except ValueError:
               print("\nError: Distance needs to be a float.")
               Prompt = input("\nEnter maximum distance from Earth (light years): ")
    return Prompt

def main():
         
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
    files = open_file()
    light_year = get_dist_range() 
    light_year /= PARSEC_LY
    lower_bound = 200
    upper_bound = 350
    albedo = 0.5

    max_value_planets = 0
    max_value_stars = 0
    rocky_distance = 10000000
    gaseous_distance = 100000000
    habitable_count = 0
    total_mass = 0
    mass_count = 0
    op = (files.readline())
    for line in files:
        
        distance_at_orbit = make_float(line[66:77])
        distance = make_float(line[114:])

        if distance < 0 or distance > light_year:
            continue
        light_year > distance_at_orbit
        planet_name = line[:25]
        num_of_stars = int(line[50:57])
        num_planets = int(line[58:65])
        planet_radius = make_float(line[78:85])
        planet_mass = make_float(line[86:96])
        star_temp = make_float(line[97:105])
        star_radius = make_float(line[106:113] )

        if num_planets > max_value_planets:
            max_value_planets = num_planets
        if num_of_stars > max_value_stars:
            max_value_stars = num_of_stars
        
        if planet_mass > 0:
            total_mass += planet_mass
            mass_count += 1
        if temp_in_range(distance_at_orbit, star_temp, star_radius, albedo, lower_bound, upper_bound) == True:
            habitable_count += 1
            if 0 < planet_mass < 10 or 0 < planet_radius < 1.5 or get_density(planet_mass, planet_radius) > 2000:
                if distance < rocky_distance:
                    rocky_distance = distance
                    rocky_name = planet_name.lstrip(" ")
            else:
                if distance < gaseous_distance:
                    gaseous_distance = distance
                    gaseous_name = planet_name.lstrip(" ")
    Average_mass = total_mass/mass_count

    files.close()
    print("\nNumber of stars in systems with the most stars: {:d}.".format(max_value_stars))
    print("Number of planets in systems with the most planets: {:d}.".format(max_value_planets))
    print("Average mass of the planets: {:.2f} Earth masses.".format(Average_mass))
    print("Number of planets in circumstellar habitable zone: {:d}.".format(habitable_count))
    if rocky_distance == 10000000:
        print("No rocky planet in circumstellar habitable zone.")
    else:
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(rocky_name, rocky_distance * PARSEC_LY))
    if gaseous_distance == 100000000:
        print("No gaseous planet in circumstellar habitable zone.")
    else:
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(gaseous_name, gaseous_distance * PARSEC_LY))
    

if __name__ == "__main__":
    main()
