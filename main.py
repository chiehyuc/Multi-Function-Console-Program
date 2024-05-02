ONE_POUND_TO_KG = 0.45359237
ONE_FT_TO_INCHES = 12
ML_WATER_PER_KG_WEIGHT = 35

import math

def main():
    print("Hello there, this is a multi-function program that can do 3 things: ")
    print("1. Calculate and check if your BMI is normal")
    print("2. Check if your blood pressure is normal")
    print("3. Calculate how much water you should drink everyday")
    the_task = input('Enter one number ("1" or "2" or "3") to run your program! :) \nEnter "4" if you want to exit this whole app!')
    while (the_task != '4'):
        while (the_task != '1') and (the_task != '2' and (the_task != '3') and (the_task != '4')):
            print("You input is invalid.")
            the_task = input('Enter one number ("1" or "2" or "3") to run your program! :) \nEnter "4" if you want to exit this whole app!')
        if the_task == '1':
            my_bmi_app()
        elif the_task == '2':
            # task 2: check blood pressure
            my_blood_pressure_app()
        elif the_task == '3':
            # task 3: calculate how many bottles of water to drink each day given weight and bottle size
            water_checker_app()
        if the_task != '4':
            print("-------------------------------------------------------------------")
            print("This is a multi-function program that can do 3 things: ")
            print("1. Calculate and check if your BMI is normal")
            print("2. Check if your blood pressure is normal")
            print("3. Calculate how much water you should drink everyday")
            the_task = input('Enter one number ("1" or "2" or "3") to run your program! :) \nEnter "4" if you want to exit this whole app!')
    print("\n****** This program now ends, thank you! :) ****** ")


def my_bmi_app():
    # print("\n")
    print("\n*****************************************************")
    print("Welcome! This is a BMI calculator!")
    weight_unit = input('Enter the unit your weight is in, is it in "kg" or "lb"? ')
    while (weight_unit != 'kg') and (weight_unit != 'lb'):
        print("You input is invalid.")
        weight_unit = input('Enter the unit your weight is in, is it in "kg" or "lb"? ')
    weight = float(input("Enter your weight: "))
    height_unit = input('Enter the unit your height is in, is it in "cm", "m" or "ft"? ')
    while (height_unit != 'cm') and (height_unit != 'm') and (height_unit != 'ft'):
        print("You input is invalid.")
        height_unit = input('Enter the unit your height is in, is it in "cm", "m" or "ft"? ')

    if height_unit == 'ft':
        height_in_ft_and_inches = input('Enter your height in the following format - "5.4" (this equals to 5 ft 4 inches): ').split(".")
        feet = int(height_in_ft_and_inches[0])
        inches = int(height_in_ft_and_inches[1])
    else:
        height = float(input("Enter your height: "))

    if (weight_unit == 'lb'):
        weight = weight * ONE_POUND_TO_KG

    if (height_unit == 'ft'):
        height = (feet * ONE_FT_TO_INCHES + inches)
        height = round(height * 2.54, 1)

    elif (height_unit == 'm'):
        height = height * 100

    # now weight is in kg and height is in cm
    bmi_value = bmi_calculator(weight, height)
    print("Your BMI is: ", bmi_value)
    bmi_range(weight, height, bmi_value)



def bmi_calculator(weight, height):
    bmi_value = weight/(height**2) * 10000
    return round(bmi_value, 2)

def bmi_range(weight, height, bmi_value):
    # gender = input("Are you male or female? ")
    # while (gender != 'male') and (gender != 'female'):
    #     print("You input is invalid.")
    #     gender = input("Are you male or female? ")
    # if gender == 'male':
    #     print("You are a male!")
    # else: # gender is female
    #     print("You are a female!")
    if bmi_value < 18.5:
        print("Your BMI value is less than normal, you are underweight.")
        upper_weight, lower_weight = normal_upper_lower_weight(weight, height)
        gain_at_least = lower_weight - weight
        gain_at_least = round(gain_at_least, 2)
        gain_at_most = upper_weight - weight
        gain_at_most = round(gain_at_most, 2)
        print("You have to gain at least " + str(gain_at_least) + "kg, at most " + 
        str(gain_at_most) + "kg to reach a normal BMI given that your height is " + 
        str(height) + "cm.\n")
    elif bmi_value > 24.9:
        print("Your BMI value is higher than normal, you are overweight.")
        upper_weight, lower_weight = normal_upper_lower_weight(weight, height)
        lose_at_least = weight - upper_weight
        lose_at_least = round(lose_at_least, 2)
        lose_at_most = weight - lower_weight
        lose_at_most = round(lose_at_most, 2)
        print("You have to lose at least " + str(lose_at_least) + "kg, at most " + 
        str(lose_at_most) + "kg to reach a normal BMI given that your height is " + 
        str(height) + "cm.\n")
    else:
        print("The normal BMI range is 18.5 ~ 24.9, your BMI is normal.\n")



def normal_upper_lower_weight(weight, height):
    # normal bmi upper limit (gain at most this amount of weight)
    at_most_weight = 24.9/10000 * (height**2)
    at_most_weight = round(at_most_weight, 2)

    # gain at least this amount of weight
    at_least_weight = 18.5/10000 * (height**2)
    at_least_weight = round(at_least_weight, 2)

    return (at_most_weight, at_least_weight)




def my_blood_pressure_app():
    # print("\n")
    print("\n*****************************************************")
    print("Welcome! This program checks if your blood pressure is normal")
    # print("This program is based on The American College of Cardiology/American Heart Association 2017 Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults.")
    
    pressure = input('Enter your systolic and diastolic pressures seperated by a "/" (e.g. "113/71"): ').split("/")
    systole_pressure = int(pressure[0])
    diastole_pressure = int(pressure[1])
    if ((systole_pressure < 120) and (diastole_pressure < 80)):
        if ((systole_pressure >= 90) and (diastole_pressure >= 60)):
            # print("\n")
            print("Your blood pressure is normal.\n")
        else:
            # print("\n")
            print("Your blood pressure is lower than normal. Please seek medical advice for more information.\n")
    elif ((systole_pressure >= 120 and systole_pressure <= 129) and (diastole_pressure < 80)):
        # print("\n")
        print("Your blood pressure is elevated. You are at risk but is not yet considered to be hypertension. Please seek medical advice for more information.\n")
    elif ((systole_pressure >= 130) or (diastole_pressure >= 80)):
        # print("\n")
        print("Your blood pressure is higher than normal, you are highly likely to have hypertension. Please seek medical advice for more information.\n")


def water_checker_app():
    # print("\n")
    print("\n*****************************************************")
    print("Welcome! This is your daily water intake calculator!")
    weight_unit = input('Enter the unit your weight is in, is it in "kg" or "lb"? ')
    while (weight_unit != 'kg') and (weight_unit != 'lb'):
        print("You input is invalid.")
        weight_unit = input('Enter the unit your weight is in, is it in "kg" or "lb"? ')
    weight = float(input("Enter your weight: "))

    if (weight_unit == 'lb'):
        weight = weight * ONE_POUND_TO_KG

    water_amount_in_ml = weight * ML_WATER_PER_KG_WEIGHT
    water_unit = input('Enter the unit your water bottle is in, is it in "ml", "cc" or "l"? ')
    while (water_unit != 'ml') and (water_unit != 'cc') and (water_unit != 'l'):
        print("You input is invalid.")
        water_unit = input('Enter the unit your water bottle is in, is it in "ml", "cc" or "l"? ')
    bottle_size = float(input("Enter the size of your water bottle: "))
    if water_unit == 'l':
        bottle_of_water_per_day = (water_amount_in_ml/1000)/bottle_size
    else:
        bottle_of_water_per_day = water_amount_in_ml/bottle_size
    bottle_of_water_per_day = round(bottle_of_water_per_day + 0.4)
    # print("\n")
    print("\nYou have to drink " + str(bottle_of_water_per_day) + " bottles of water per day! :)\n")

if __name__ == "__main__":
    main()