from datetime import timedelta
from datetime import date


def count_timestep(date1, date2, step):
    start = date.fromisoformat(date1)
    current_step = start
    end = date.fromisoformat(date2)
    delta = timedelta(days=step)
    count_of_timestep = 0

    while current_step < end:
        current_step += delta
        count_of_timestep += 1
        print(current_step)
        if current_step >= end:
            print(current_step - end)
    print(count_of_timestep)
    print("!", int((end - start).days))


count_timestep('2023-01-01', '2024-01-16', 7)
