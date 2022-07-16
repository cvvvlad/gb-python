class Road:

    def __init__(self, length_m, width_m):
        self._length_m = length_m
        self._width_m = width_m

    def calc_mass(self, mass_kg_per_cm, thickness_cm):
        return self._length_m * self._width_m * mass_kg_per_cm * thickness_cm


road = Road(20, 5000)
mass_kg = road.calc_mass(25, 5)
mass_tonn_str = f"{mass_kg / 1000:_.2f}".replace('_', ' ')
print(f"Масса асфальта, необходимого для покрытия всей дороги составляет {mass_tonn_str} т.")
