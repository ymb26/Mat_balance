phase = ['Gas', 'Oil', 'Water']


class Phase:
    def __init__(self, name, saturation):
        self.name = name
        self.saturation = saturation


for i in phase:
    print(i)


