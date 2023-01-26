import value_of_table


class Grid:
    def __init__(self, amount_of_phases, phases):
        self.Phase = [Fluid(phases[ph]) for ph in range(amount_of_phases)]
        self.pressure = 0
        self.critical_pressure = 0
        self.porosity = 0
        self.effective_volume = 0
        self.amount_phases = amount_of_phases

    def take_phase(self, name_of_phase):
        for ph in self.Phase:
            if name_of_phase.lower() == ph.name.lower():
                return ph


class Fluid:
    def __init__(self, name_of_phase):
        self.name = name_of_phase
        self.density = 0
        self.volume = 0
        self.saturation = 0
        self.fv_factor = 0
        self.mass_in_plast = 0
        self.mass_extraction = 0
        self.viscosity = 0
        self.compressibility = 0

    def mass(self):
        return self.mass_in_plast

    def mass_extra(self):
        return self.mass_extraction

    def read_mass_dens(self, m, density):
        self.mass_in_plast = m
        self.density = density

    def current_fv_factor(self, pressure):
        if self.name.lower() == "Gas_in_oil".lower():
            self.fv_factor = (1 / pressure)
            print(self.fv_factor)
        elif self.name.lower() == "Gas".lower():
            self.fv_factor = (1 / pressure)
            print(self.fv_factor)
        elif self.name.lower() == "Oil".lower():
            self.fv_factor = (-0.002 * pressure + 1.4)
            print(self.fv_factor)
        elif self.name.lower() == "Water".lower():
            self.fv_factor = (1 - (4 / 100000) * (pressure - 1))
            print(self.fv_factor)


class Cell:
    def __init__(self, steps, amount_of_phases, phases):
        self.Step = [Grid(amount_of_phases, phases) for st in range(steps)]
        self.amount_of_step = steps

    def print_statistic(self):
        output_file = open("statistic.txt", "w")
        print("Pressure ", "Mass_in         ", "Mass_out            ", "Density         ", "FV_factor           ", "Saturation          ")
        output_file.write("Pressure\tMass_in\t\t\tMass_out\t\t\tDensity\t\t\tFV_factor\t\t\tSaturation\n")
        for step in self.Step:
            print(step.pressure, end='  ')
            output_file.write(str(step.pressure) + "\t")
            for phase in step.Phase:
                print(phase.mass_in_plast, end='    ')
                output_file.write(str(phase.mass_in_plast) + '\t')
            for phase in step.Phase:
                print(phase.mass_extraction, end='    ')
                output_file.write(str(phase.mass_extraction) + '\t')
            for phase in step.Phase:
                print(phase.density, end='    ')
                output_file.write(str(phase.density) + '\t')
            for phase in step.Phase:
                print(phase.fv_factor, end='    ')
                output_file.write(str(phase.fv_factor) + '\t')
            for phase in step.Phase:
                print(phase.saturation, end='    ')
                output_file.write(str(phase.saturation) + '\t')
            print()
            output_file.write('\n')



density_table = [0.0007, 0.0007, 0.793]
mass_table = [84, 0, 839]
TP22 = Cell(10, 3, ['Gas_in_oil', 'Gas', 'Oil'])

TP22.Step[0].pressure = 210
TP22.Step[0].critical_pressure = 110
TP22.Step[0].porosity = 0.22
TP22.Step[0].effective_volume = 11450
for i in range(TP22.Step[0].amount_phases):
    TP22.Step[0].Phase[i].density = density_table[i]
    TP22.Step[0].Phase[i].mass_in_plast = mass_table[i]
    TP22.Step[0].Phase[i].current_fv_factor(TP22.Step[0].pressure)

TP22.print_statistic()

#TP22.Step[0].take_phase('Oil').fv_factor = 1 / 0.7
#TP22.Step[0].take_phase('Oil').saturation = 0.6
#TP22.Step[0].take_phase('Oil').density = 0.793
#TP22.Step[0].take_phase('Oil').volume = TP22.Step[0].take_phase('Oil').saturation * TP22.Step[0].porosity * TP22.Step[0].effective_volume
#P22.Step[0].take_phase('Oil').mass_in_plast = TP22.Step[0].take_phase('Oil').volume * (1 / TP22.Step[0].take_phase("oil").fv_factor) * TP22.Step[0].take_phase('oil').density
