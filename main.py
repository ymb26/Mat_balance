from Classes import Grid

TP22 = Grid(150, 100)

TP22.make_gas('Gas', 1, 2, 3, 4)  # 5
TP22.make_oil('Oil', 1, 2, 3, 4, 5, 6)  # 7
TP22.make_water('Water', 1, 2, 3, 4)  # 5
TP22.check_all_phase('2023-01-01', '2023-01-31', 7, 25000)  # 3
TP22.Calculate.print_timesteps()

