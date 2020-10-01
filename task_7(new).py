def conversion_from_inches_to_centimeters(inch):
    conversion_inch_in_cm_and_rounded = round((inch * 2.54), 2)
    print(inch, ' inch = ', conversion_inch_in_cm_and_rounded, 'cm')
    return conversion_from_inches_to_centimeters


def conversion_from_centimeters_to_inches(cm):
    conversion_cm_in_inch_and_rounded = round((cm * 0.393701), 2)
    print(cm, 'cm = ', conversion_cm_in_inch_and_rounded, 'inch')
    return conversion_from_centimeters_to_inches


def conversion_miles_to_kilometers(mile):
    conversion_miles_in_kilometers_and_rounded = round((mile * 1.60934), 2)
    print(mile, 'mile = ', conversion_miles_in_kilometers_and_rounded, 'kilometers')
    return conversion_miles_to_kilometers


def conversion_kilometers_to_miles(kilometers):
    conversion_kilometers_to_miles_and_rounded = round((kilometers * 0.621371), 2)
    print(kilometers, 'kilometers = ', conversion_kilometers_to_miles_and_rounded, 'miles')
    return conversion_kilometers_to_miles


def conversion_of_pounds_to_kilograms(pounds):
    conversion_of_pounds_to_kilograms_and_rounded = round((pounds * 0.453592), 2)
    print(pounds, 'pounds = ', conversion_of_pounds_to_kilograms_and_rounded, 'kilograms')
    return conversion_of_pounds_to_kilograms


def conversion_of_kilograms_to_pounds(kilograms):
    conversion_of_kilograms_to_pounds_and_rounded = round((kilograms * 2.200462), 2)
    print(kilograms, 'kilograms = ', conversion_of_kilograms_to_pounds_and_rounded, 'pounds')
    return conversion_of_kilograms_to_pounds


def conversion_of_ounce_to_grams(ounce):
    conversion_of_ounce_to_grams_and_rounded = round((ounce * 28.3495), 2)
    print(ounce, 'ounce = ', conversion_of_ounce_to_grams_and_rounded, 'grams')
    return conversion_of_ounce_to_grams


def conversion_of_grams_to_ounce(grams):
    conversion_of_grams_to_ounce_and_rounded = round((grams * 0.035274), 2)
    print(grams, 'grams = ', conversion_of_grams_to_ounce_and_rounded, 'ounce')
    return conversion_of_grams_to_ounce


def conversion_of_gallons_to_liters(gallons):
    conversion_of_gallons_to_liters_and_rounded = round((gallons * 3.78541), 2)
    print(gallons, 'gallons = ', conversion_of_gallons_to_liters_and_rounded, 'liters')
    return conversion_of_gallons_to_liters


def conversion_of_liters_to_gallons(liters):
    conversion_of_liters_to_gallons_and_rounded = round((liters * 0.264172), 2)
    print(liters, 'liters = ', conversion_of_liters_to_gallons_and_rounded, 'gallons')
    return conversion_of_liters_to_gallons


def conversion_of_liters_to_pints(liters):  # взял американскую жидкую пинту в литры
    conversion_of_liters_to_pints_and_rounded = round((liters * 2.11338), 2)
    print(liters, 'liters = ', conversion_of_liters_to_pints_and_rounded, 'pints')
    return conversion_of_liters_to_pints


def conversion_of_pints_to_liters(pints):  # взял американскую жидкую пинту в литры
    conversion_of_pints_to_liters_and_rounded = round((pints * 0.473176), 2)
    print(pints, 'pints = ', conversion_of_pints_to_liters_and_rounded, 'liters')
    return conversion_of_pints_to_liters


dict_function = {
    '1': conversion_from_centimeters_to_inches,
    '2': conversion_miles_to_kilometers,
    '3': conversion_miles_to_kilometers,
    '4': conversion_kilometers_to_miles,
    '5': conversion_of_pounds_to_kilograms,
    '6': conversion_of_kilograms_to_pounds,
    '7': conversion_of_ounce_to_grams,
    '8': conversion_of_grams_to_ounce,
    '9': conversion_of_gallons_to_liters,
    '10': conversion_of_liters_to_gallons,
    '11': conversion_of_liters_to_pints,
    '12': conversion_of_pints_to_liters
}

user_choice = input('Enter a number greater than zero to continue.\n'
                    'Enter 0 to exit \n')
while user_choice != '0':
    user_choice = input('enter a number from 1 to 12 to select the value to convert\n'
                        '1 - conversion_from_centimeters_to_inches \n'
                        '2 - conversion_miles_to_kilometers \n'
                        '3 - conversion_miles_to_kilometers\n'
                        '4 - conversion_kilometers_to_miles \n'
                        '5 - conversion_of_pounds_to_kilograms \n'
                        '6 - conversion_of_kilograms_to_pounds \n'
                        '7 - conversion_of_ounce_to_grams \n'
                        '8 - conversion_of_grams_to_ounce \n'
                        '9 - conversion_of_gallons_to_liters \n'
                        '10 - conversion_of_liters_to_gallons \n'
                        '11 - conversion_of_liters_to_pints \n'
                        '12 - conversion_of_pints_to_liters\n')

    function_ = dict_function.get(user_choice, lambda: "Sorry bro wrong input")
    num_to_convert = float(input('Enter number for conversion \n'))
    print(function_(num_to_convert))

