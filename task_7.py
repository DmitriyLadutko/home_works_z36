def conversion_from_inches_to_centimeters(inch):
    conversion_inch_in_cm_and_rounded = round((inch * 2.54), 2)
    if float(conversion_inch_in_cm_and_rounded):
        print(inch, ' inch = ', conversion_inch_in_cm_and_rounded, 'cm')


conversion_from_inches_to_centimeters(float(input('Enter any number\n')))


def conversion_from_centimeters_to_inches(cm):
    conversion_cm_in_inch_and_rounded = round((cm * 0.393701), 2)
    if float(conversion_cm_in_inch_and_rounded):
        print(cm, 'cm = ', conversion_cm_in_inch_and_rounded, 'inch')


conversion_from_centimeters_to_inches(float(input('Enter any number\n')))


def conversion_miles_to_kilometers(mile):
    conversion_miles_in_kilometers_and_rounded = round((mile * 1.60934), 2)
    if float(conversion_miles_in_kilometers_and_rounded):
        print(mile, 'mile = ', conversion_miles_in_kilometers_and_rounded, 'kilometers')


conversion_miles_to_kilometers(float(input('Enter any number\n')))


def conversion_kilometers_to_miles(kilometers):
    conversion_kilometers_to_miles_and_rounded = round((kilometers * 0.621371), 2)
    if float(conversion_kilometers_to_miles_and_rounded):
        print(kilometers, 'kilometers = ', conversion_kilometers_to_miles_and_rounded, 'miles')


conversion_kilometers_to_miles(float(input('Enter any number\n')))


def conversion_of_pounds_to_kilograms(pounds):
    conversion_of_pounds_to_kilograms_and_rounded = round((pounds * 0.453592), 2)
    if float(conversion_of_pounds_to_kilograms_and_rounded):
        print(pounds, 'pounds = ', conversion_of_pounds_to_kilograms_and_rounded, 'kilograms')


conversion_of_pounds_to_kilograms(float(input('Enter any number\n')))


def conversion_of_kilograms_to_pounds(kilograms):
    conversion_of_kilograms_to_pounds_and_rounded = round((kilograms * 2.200462), 2)
    if float(conversion_of_kilograms_to_pounds_and_rounded):
        print(kilograms, 'kilograms = ', conversion_of_kilograms_to_pounds_and_rounded, 'pounds')


conversion_of_kilograms_to_pounds(float(input('Enter any number\n')))


def conversion_of_ounce_to_grams(ounce):
    conversion_of_ounce_to_grams_and_rounded = round((ounce * 28.3495), 2)
    if float(conversion_of_ounce_to_grams_and_rounded):
        print(ounce, 'ounce = ', conversion_of_ounce_to_grams_and_rounded, 'grams')


conversion_of_ounce_to_grams(float(input('Enter any number\n')))


def conversion_of_grams_to_ounce(grams):
    conversion_of_grams_to_ounce_and_rounded = round((grams * 0.035274), 2)
    if float(conversion_of_grams_to_ounce_and_rounded):
        print(grams, 'grams = ', conversion_of_grams_to_ounce_and_rounded, 'ounce')


conversion_of_grams_to_ounce(float(input('Enter any number\n')))


def conversion_of_gallons_to_liters(gallons):
    conversion_of_gallons_to_liters_and_rounded = round((gallons * 3.78541), 2)
    if float(conversion_of_gallons_to_liters_and_rounded):
        print(gallons, 'gallons = ', conversion_of_gallons_to_liters_and_rounded, 'liters')


conversion_of_gallons_to_liters(float(input('enter an integer number\n')))


def conversion_of_liters_to_gallons(liters):
    conversion_of_liters_to_gallons_and_rounded = round((liters * 0.264172), 2)
    if float(conversion_of_liters_to_gallons_and_rounded):
        print(liters, 'liters = ', conversion_of_liters_to_gallons_and_rounded, 'gallons')


conversion_of_liters_to_gallons(float(input('enter an integer number\n')))


def conversion_of_liters_to_pints(liters):  # взял американскую жидкую пинту в литры
    conversion_of_liters_to_pints_and_rounded = round((liters * 2.11338), 2)
    if float(conversion_of_liters_to_pints_and_rounded):
        print(liters, 'liters = ', conversion_of_liters_to_pints_and_rounded, 'pints')


conversion_of_liters_to_pints(float(input('enter an integer number\n')))


def conversion_of_pints_to_liters(pints):  # взял американскую жидкую пинту в литры
    conversion_of_pints_to_liters_and_rounded = round((pints * 0.473176), 2)
    if float(conversion_of_pints_to_liters_and_rounded):
        print(pints, 'pints = ', conversion_of_pints_to_liters_and_rounded, 'liters')


conversion_of_pints_to_liters(float(input('enter an integer number\n')))

list_function = []
