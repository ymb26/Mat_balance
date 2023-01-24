from datetime import timedelta
from datetime import date


class Grid:
    def __init__(self):
        self._Phase = list()
        self._timesteps = list()
        self._days_in_step = list()
        self.current_pressure = list()
        self._amount_of_phases = 0

    def add_property_of_phase(self, name, density, saturation):
        self._Phase.append(self._amount_of_phases)
        self._Phase[self._amount_of_phases] = Fluid(name, self._amount_of_phases, density, saturation, self._timesteps, self._days_in_step)
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

    def calculate_something(self):
        x = 0
        for i in range(self._amount_of_phases):
            x += self._Phase[i].do_it()
        print(x)


class Fluid(Grid):
    def __init__(self, name, index, density, saturation, timesteps, days_in_step):
        super().__init__()
        self.index = index
        self.name = name
        self.density = density
        self.saturation = saturation
        self._timesteps = timesteps
        self._days_in_step = days_in_step
        self.current_density = [None] * len(self._timesteps)

    def do_it(self):
        print(self._timesteps)
        return float(self.saturation)

    def print_density(self):
        for i in self.current_density:
            print(i)


TP22 = Grid()
TP22.fill_timesteps('2023-01-01', '2023-02-01', 7)
TP22.print_statistic()
TP22.add_property_of_phase('Oil', 793, 0.600)
TP22.add_property_of_phase('Gas', 330, 0.700)
TP22.Phase[0].print_density()
