import numpy as np


def calculate_surface_densities_by_group(group, data_transects, transect_lenght = 300):
    animal_group_data = data_transects[data_transects["Grupo"] == group]
    transect_width = 10
    point_radius = 25
    transects = animal_group_data["Transecto"].unique()
    species = animal_group_data["Especie"].dropna().unique()
    results_dic = {
        "Transecto": [],
        "Especie": [],
        "Densidad": [],
        "Distancia_max": [],
        "Tipo_vegetacion": [],
    }
    for transect in transects:
        for specie in species:
            mask = (animal_group_data.Transecto == transect) & (animal_group_data.Especie == specie)
            filtered_data = animal_group_data[mask]
            transect_data = animal_group_data[animal_group_data.Transecto == transect]
            vegetal_types = transect_data["Tipo_de_vegetacion"].unique()
            n_individuals = filtered_data["Cantidad_individuos"].sum()
            if group == "Ave":
                density_in_transect = n_individuals / (np.pi * point_radius**2 * 5)
            if group == "Tecolote":
                density_in_transect = n_individuals / (
                    transect_lenght * filtered_data["Distancia"].max() * 2
                )
            if group == "Reptil":
                density_in_transect = n_individuals / (transect_lenght * transect_width * 2)
            density_in_transect_ha = density_in_transect * 10_000
            results_dic["Especie"].append(specie)
            results_dic["Transecto"].append(transect)
            results_dic["Densidad"].append(density_in_transect_ha)
            results_dic["Distancia_max"].append(filtered_data["Distancia"].max())
            results_dic["Tipo_vegetacion"].append(check_array(vegetal_types))
    return results_dic


def check_array(array):
    if array.size == 0:
        return "NA"
    return array[0]
