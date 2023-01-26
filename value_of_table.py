def read_file_make_dictionary(phase):
    table = {}
    file = open('%s_pressure' % phase, 'r')
    for key_words in file.readline().split():
        table[key_words] = []
    for line in file:
        for value, keys in zip(line.split(), table):
            table[keys].append(float(value))
    print(table)
    return table


def calculation_value_on_two_points(pressure, point1, pressure1, point2, pressure2):
    value = ((point1 - point2)/(pressure1 - pressure2)) * (pressure - pressure1) + point1
    return value


def take_value(parameter, pressure, phase):
    table = read_file_make_dictionary(phase)
    for i in range(len(table["Pressure"])):
        if pressure < int(table["Pressure"][i]) and i == 0:
            print(pressure, "First zone", int(table["Pressure"][i]))  ##function
            return calculation_value_on_two_points(pressure, table[parameter][1], table["Pressure"][1], table[parameter][0], table["Pressure"][0])
        elif pressure == int(table["Pressure"][i]):
            print(pressure, "Equil")
            return table[parameter][i]
        elif int(table["Pressure"][i]) > pressure > int(table["Pressure"][i - 1]):
            print(pressure, "Second zone", int(table["Pressure"][i-1]), int(table["Pressure"][i]))
            return calculation_value_on_two_points(pressure, table[parameter][i], table["Pressure"][i], table[parameter][i - 1], table["Pressure"][i - 1])
        elif pressure > int(table["Pressure"][i]) and i == len(table["Pressure"]) - 1:
            print(i, pressure, "Last zone",int(table["Pressure"][i-1]), int(table["Pressure"][i]))
            return calculation_value_on_two_points(pressure, table[parameter][i], table["Pressure"][i], table[parameter][i - 1], table["Pressure"][i - 1])




