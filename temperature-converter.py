def convert_temp(unit_from, unit_to, temp):
    def to_kelvin(temp, unit):
        if unit == "k":
            return temp
        elif unit == "c":
            return (temp + 273.15)
        elif unit == "f":
            return ((temp - 32) * (5/9) + 273.15)
    
    temp_in_k = to_kelvin(temp, unit_from)
    
    if unit_to == "c":
        return (temp_in_k - 273.15)
    elif unit_to == "f":
        return ((temp_in_k - 273.15) * (9/5) + 32)
    elif unit_to == "k":
        return temp_in_k
    else:
        return 0

unit_from = input("what unit are you converting from?\n> ")
unit_to = input("what unit are you converting to?\n> ")
temp = int(input("what's the temperature?\n> "))

print(str(convert_temp(unit_from, unit_to, temp)) + " " + unit_to.upper())