from datetime import timedelta
from datetime import date


class Grid:
    def __init__(self):
        self._Phase = list()
        self._timesteps = list()
        self._days_in_step = list()
        self.current_pressure = list()
        self._amount_of_phases = 0

        self.base_pressure = 0
        self.porosity = 0
        self.oil_saturation = 0
        self.water_saturation = 0
        self.oil_fv_factor = 0
        self.gas_fv_factor = 0
        self.water_fv_factor = 0
        self.OOIP = 0
        self.GOIP = 0
        self.WOIP = 0
        self.oil_density = 0
        self.gas_density = 0
        self.water_density = 0

    def put_base_phases_parameters(self, pressure, porosity, oil_saturation, oil_fv_factor, oil_density, gas_density,
                                   water_density, OOIP, GOIP):
        self.base_pressure = pressure
        self.porosity = porosity
        self.oil_saturation = oil_saturation
        self.water_saturation = 1 - oil_saturation
        self.oil_fv_factor = 1 / oil_fv_factor
        self.gas_fv_factor = 0      #
        self.water_fv_factor = 0    #
        self.OOIP = OOIP
        self.GOIP = GOIP
        self.WOIP = 0       #
        self.oil_density = oil_density
        self.gas_density = gas_density
        self.water_density = water_density

    def add_property_of_phase(self, name):
        self._Phase.append(self._amount_of_phases)
        self._Phase[self._amount_of_phases] = Fluid(name, self._amount_of_phases, self._timesteps)
        self._amount_of_phases += 1

    @property
    def Phase(self):
        return self._Phase

    def fill_timesteps(self, date1, date2, step):
        start = date.fromisoformat(date1)
        current_step = start
        end = date.fromisoformat(date2)
        delta = timedelta(days=step)

        while current_step < end:
            self._timesteps.append(current_step)
            current_step += delta
            if current_step >= end:
                self._timesteps.append(end)

        for i in range(0, len(self._timesteps)):
            if i == 0 and len(self._timesteps) > 0:
                self._days_in_step.append(int(0))
            else:
                self._days_in_step.append(int((self._timesteps[i] - self._timesteps[i - 1]).days))

    def print_statistic(self):
        for i in range(len(self._timesteps)):
            print(self._timesteps[i], self._days_in_step[i])

    def pointer_on_phase(self, name_of_phase):
        for i in self._Phase:
            if name_of_phase.lower() == i.name.lower():
                return i
        print("Wrong phase")


class Fluid(Grid):
    def __init__(self, name_of_phase, index, timesteps):
        super().__init__()
        self.index = index
        self.name = name_of_phase
        self.weight_in_plast = [None] * len(timesteps)
        self.weight_extraction = [None] * len(timesteps)
        self.volume = [None] * len(timesteps)
        self.production = [None] * len(timesteps)
        self.current_density = [None] * len(timesteps)


TP22 = Grid()
TP22.fill_timesteps('2023-01-01', '2023-02-01', 7)
TP22.put_base_phases_parameters(210, 0.22, 0.6, 0.7, 0.793, 0.0007, 1, 839, 84)     # base_pressure, porosity, oil_saturation, oil_fv_factor, oil_density, gas_density, water_density, OOIP, GOIP
TP22.add_property_of_phase('Oil')
TP22.add_property_of_phase('Gas')
TP22.add_property_of_phase("Gas_in_oil")
TP22.add_property_of_phase('Water')
print(TP22.pointer_on_phase("Gas").name)

