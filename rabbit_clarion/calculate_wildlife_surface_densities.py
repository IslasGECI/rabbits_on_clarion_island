import numpy as np


def calculate_surface_densities_by_group(group, data_transects, transect_lenght = 300):
    animal_group_data = data_transects[data_transects["Grupo"] == group]
    TRANSECT_PARAMETERS = {"lenght" : transect_lenght,"width": 10, "point_radius": 25}
    transects = animal_group_data["Transecto"].unique()
    species = animal_group_data["Especie"].dropna().unique()
    results_dic = _init_results()
    for transect in transects:
        vegetal_types = obtain_vegetation_type_by_transect(animal_group_data, transect)
        for specie in species:
            filtered_data = filter_by_transect_and_species(animal_group_data, transect, specie)
            maximum_distance = filtered_data["Distancia"].max()
            density_in_transect_ha = calculate_density_in_transect(group, TRANSECT_PARAMETERS, filtered_data)
            update_results(results_dic, transect, specie, maximum_distance, vegetal_types, density_in_transect_ha)
    return results_dic


def obtain_vegetation_type_by_transect(animal_group_data, transect):
    transect_data = animal_group_data[animal_group_data.Transecto == transect]
    vegetal_types = transect_data["Tipo_de_vegetacion"].unique()
    return vegetal_types

def filter_by_transect_and_species(animal_group_data, transect, specie):
    mask = (animal_group_data.Transecto == transect) & (animal_group_data.Especie == specie)
    filtered_data = animal_group_data[mask]
    return filtered_data

def update_results(results_dic, transect, specie, maximum_distance, vegetal_types, density_in_transect_ha):
    results_dic["Especie"].append(specie)
    results_dic["Transecto"].append(transect)
    results_dic["Densidad"].append(density_in_transect_ha)
    results_dic["Distancia_max"].append(maximum_distance)
    results_dic["Tipo_vegetacion"].append(check_array(vegetal_types))

def calculate_density_in_transect(group, TRANSECT_PARAMETERS, filtered_data):
    n_individuals = filtered_data["Cantidad_individuos"].sum()
    if group == "Ave":
        density_in_transect = n_individuals / (np.pi * TRANSECT_PARAMETERS["point_radius"]**2 * 5)
    if group == "Tecolote":
        density_in_transect = n_individuals / (
                    TRANSECT_PARAMETERS["lenght"] * filtered_data["Distancia"].max() * 2
                )
    if group == "Reptil":
        density_in_transect = n_individuals / (TRANSECT_PARAMETERS["lenght"] * TRANSECT_PARAMETERS["width"] * 2)
    density_in_transect_ha = density_in_transect * 10_000
    return density_in_transect_ha


def check_array(array):
    if array.size == 0:
        return "NA"
    return array[0]

def _init_results():
    return {
        "Transecto": [],
        "Especie": [],
        "Densidad": [],
        "Distancia_max": [],
        "Tipo_vegetacion": [],
    }
