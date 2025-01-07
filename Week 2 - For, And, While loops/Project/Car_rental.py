###########################################################
#  Project 2 will be able to compute and display information for a 
# company which rents vehicles to its customers/players in the game.  For a specified 
# customer/player, the program will compute and display the amount of money charged for that 
# customer/player’s vehicle rental.
###########################################################


BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"  

import math

print(BANNER)

PROMPT = input('''\nWould you like to continue (A/B)? ''')

while PROMPT == 'A':
   if PROMPT == 'A':
        print("")
   classification_code = input("\nCustomer code (BD, D, W): \n")
   while (classification_code != "BD") and (classification_code !='D') and (classification_code !='W'):
        print("\n\t*** Invalid customer code. Try again. ***")
        classification_code = input("\nCustomer code (BD, D, W): \n")
   if (classification_code == "BD") or (classification_code =='D') or (classification_code =='W'):
        rental_days = int( input("\nNumber of days: \n"))
        start_vo_reading = int( input("Odometer reading at the start: \n")) # start of vehivcle odometer reading
        end_vo_reading = int( input("Odometer reading at the end:   \n")) # end of vehicle odometer reading
        ## Variables for Calculation ##
        number_of_miles_driven = (end_vo_reading - start_vo_reading)
        mileage = float(number_of_miles_driven/10)
            ## Average mileage and excgess charge calculation for code D ##
        average_mileageD = float(mileage/rental_days) # average mileage variable to be used for code D
        chargeable_mileageD = (average_mileageD - 100) # extra mileage that will be charged $0.25 per mile
        rent_week = math.ceil(rental_days/7)
        average_mileage_week = float(mileage/rent_week)
        print("\nCustomer summary:", )
        print("\tclassification code:",classification_code)
        print("\trental period (days):",rental_days )
        print("\todometer reading at start:",start_vo_reading )
        print("\todometer reading at end:  ",end_vo_reading )
        
        if end_vo_reading < start_vo_reading:
            end_vo_reading = (end_vo_reading + 1000000)
            number_of_miles_driven = (end_vo_reading - start_vo_reading)
            mileage = float(number_of_miles_driven/10)
            print("\tnumber of miles driven: ",mileage )
        elif end_vo_reading > start_vo_reading:
            end_vo_reading = end_vo_reading
            print("\tnumber of miles driven: ",mileage )
            
        if classification_code == 'BD':
            base_charge = float(40 * rental_days)
            mileage_charge = float(0.25 * mileage)
            amount_due = mileage_charge + base_charge
            print("\tamount due: $", amount_due,)
            
        elif classification_code == "D":
            base_charge = float(60 * rental_days)
            if average_mileageD <= 100:
                mileage_charge = base_charge
                print("\tamount due: $", mileage_charge)
            elif average_mileageD >= 100:
                mileage_charge = float(0.25 * chargeable_mileageD * rental_days) + base_charge
                print("\tamount due: $", mileage_charge)
                
        elif classification_code == "W":
            base_charge = float(190 * rent_week)
            if average_mileage_week <= 900:
                mileage_charge = base_charge
                print("\tamount due: $", mileage_charge)
            elif 900 < average_mileage_week <= 1500:
                mileage_charge = ((100 * rent_week) +base_charge)
                print("\tamount due: $", mileage_charge)
            elif average_mileage_week > 1500:
                difference = mileage - (1500 * rent_week)
                mileage_charging = (0.25 * difference)
                mileage_charge = mileage_charging + base_charge + (200 * rent_week)
                print("\tamount due: $", mileage_charge)
   PROMPT = input('''\nWould you like to continue (A/B)? ''')
if PROMPT == 'B':
   print ("\nThank you for your loyalty.")
