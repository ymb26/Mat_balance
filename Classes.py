from datetime import timedelta
from datetime import date


class Grid:
    def __init__(self, pore_volume, initial_pressure):
        self._Gas = None 1
        self._Oil = None 2
        self._Water = None 3
        self._Calculate = None
        self._pore_volume = pore_volume
        self._initial_pressure = initial_pressure

    def make_gas(self, name_phase, saturation, density, formation_factor, init_formation_factor):
        self._Gas = Gas(name_phase, saturation, density, formation_factor, init_formation_factor)

    def make_oil(self, name_phase, saturation, density, formation_factor, init_formation_factor, init_gas_solution,
                 current_gas_solution):
        self._Oil = Oil(name_phase, saturation, density, formation_factor, init_formation_factor, init_gas_solution,
                        current_gas_solution)

    def make_water(self, name_phase, saturation, density, formation_factor, init_formation_factor):
        self._Water = Water(name_phase, saturation, density, formation_factor, init_formation_factor)

    def check_all_phase(self, start, end, step, oil_production):
        if not self._Gas:
            print("No Gas")
        elif not self._Oil:
            print("No Oil")
        elif not self._Water:
            print("No Water")
        else:
            self._Calculate = Calculate(start, end, step, oil_production)
            self._Calculate.count_and_fill_timestep()
            self._Calculate.fill_days()

    @property
    def Calculate(self):
        return self._Calculate

    @property
    def Gas(self):
        return self._Gas

    @property
    def Oil(self):
        return self._Oil

    @property
    def Water(self):
        return self._Water


class Gas:
    def __init__(self, name_phase, saturation, density, formation_factor, init_formation_factor):
        self._name = name_phase
        self._saturation = saturation
        self._density = density
        self._form_factor = formation_factor
        self._init_form_factor = init_formation_factor

    def print_saturation(self):
        print(self._name, self._saturation, self._init_form_factor)


class Oil:
    def __init__(self, name_phase, saturation, density, formation_factor, init_formation_factor, init_gas_solution,
                 current_gas_solution):
        self._name = name_phase
        self._saturation = saturation
        self._density = density
        self._form_factor = formation_factor
        self._init_form_factor = init_formation_factor
        self._init_gas_solution = init_gas_solution
        self._current_gas_solution = current_gas_solution

    def print_saturation(self):
        print(self._name, self._saturation, self._current_gas_solution)


class Water:
    def __init__(self, name_phase, saturation, density, formation_factor, init_formation_factor):
        self._name = name_phase
        self._saturation = saturation
        self._density = density
        self._form_factor = formation_factor
        self._init_form_factor = init_formation_factor

    def print_saturation(self):
        print(self._name, self._saturation)


class Calculate:
    def __init__(self, start, end, step, oil_production):
        self._start_date = start
        self._end_date = end
        self._step = step
        self._oil_prod = oil_production
        self._timestep = []
        self._days_in_step = []
        self._ROIP = []
        self._current_density_oil = []
        self._current_form_factor_oil = []
        self._current_pressure = []

    def count_and_fill_timestep(self):
        start = date.fromisoformat(self._start_date)
        current_step = start
        end = date.fromisoformat(self._end_date)
        delta = timedelta(days=self._step)

        while current_step < end:
            self._timestep.append(current_step)
            current_step += delta
            if current_step >= end:
                self._timestep.append(end)

    def fill_days(self):
        for i in range(0, len(self._timestep)):
            if i == 0 and len(self._timestep) > 0:
                self._days_in_step.append(int(0))
            else:
                self._days_in_step.append(int((self._timestep[i] - self._timestep[i - 1]).days))

    def amount_of_steps(self):
        return len(self._timestep)

    def print_timesteps(self):
        for date_s, day_s in zip(self._timestep, self._days_in_step):
            print(date_s, day_s)
