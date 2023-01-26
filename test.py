from datetime import timedelta
from datetime import date


class Fluid:
    def __init__(self, name, index, density, saturation):
        self.index = index
        self.name = name
        self.density = density
        self.saturation = saturation
        self.current_density = [None]


class Grid:
    def __init__(self, pressure, porosity, original_oil_saturated_pore_volume):
        self._Phase = list()
        self._timesteps = list()
        self._days_in_step = list()
        self.ROIP = list()
        self.current_pressure = list()
        self._amount_of_phases = 0
        self._porosity = porosity
        self._pressure = pressure
        self._OOV = original_oil_saturated_pore_volume
        self._OOIP =

    def add_property_of_phase(self, name, density, saturation):
        self._Phase.append(self._amount_of_phases)
        self._Phase[self._amount_of_phases] = Fluid(name, self._amount_of_phases, density, saturation)
        self._amount_of_phases += 1

    @property
    def Phase(self):
        return self._Phase

    def calculate_oil(self, oil_rate):
        for i in range(len(self._timesteps)):
            if i == 0:
                self.ROIP.append(self.OOIP)
            else:
                self.ROIP.append(self.ROIP[i - 1] - oil_rate/self._days_in_step[i])

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
            print(self._timesteps[i], self._days_in_step[i], self.ROIP[i])


TP22 = Grid(210, 0.22, 1511400)
TP22.add_property_of_phase('Oil', 793, 0.600)

setattr(Grid, 'OOIP', 840000)

TP22.fill_timesteps('2023-01-01', '2023-02-01', 7)
TP22.calculate_oil(25000)
TP22.print_statistic()

