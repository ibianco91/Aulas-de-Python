conversions = {
                "mm": {"mm": 1, "cm": 1/10, "m": 1/1000, "km": 1/1000000},
                "cm": {"mm": 10, "cm": 1, "m": 1/100, "km": 1/100000},
                "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 1/1000},
                "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
              }
unit1 = raw_input ("Which unit would you like to convert from?\n"
                   "We support: " + ", ".join(conversions.keys()))
unit2 = raw_input ("Which unit would you like to convert to?\n")
                   "We support: " + ", ".join(conversions[unit1].keys()))
while True:
    try:
        unit1 = raw_input ("Which unit would you like to convert from?\n"
                           "We support: "
                           ", ".join(conversions.keys())).lower()
        unit2 = raw_input ("Which unit would you like to convert to?\m")
                           "We support: "
                           ", ".join(conversions[unit1].keys())).lower()
        convert = conversions[unit1][unit2]
    except KeyError:
        print ("That is not a valid key, please try again")
while True:
    try:
        num1 = float(raw_input("Enter your value: " ))
    except ValueError:
        print ("That is not a valid float, please try again.")
ans = num1 * convert