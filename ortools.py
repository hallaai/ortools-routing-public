#!/usr/bin/env python
# coding: utf-8

#import os
#os.system("pip install ortools")
#os.system("pip install geopy")

#from statistics import mean
#from geopy.geocoders import Nominatim
#import geopy.distance
#from ortools.constraint_solver import routing_enums_pb2
#from ortools.constraint_solver import pywrapcp

import pandas as pd
dist_matrix = pd.read_excel('dist_mtrx.xlsx')
print(dist_matrix.head())

"""Vehicles Routing Problem (VRP). One function"""
def getOrtoolsRoutes(d_matrix, nTargets):
    from ortools.constraint_solver import pywrapcp
    def create_data_model():
        """Stores the data for the problem."""
        data = {}
        data['distance_matrix'] = list(map(lambda x: list(d_matrix.iloc[0:rng, 0:rng].iloc[x]), range(0, dist_matrix.iloc[0:rng, 0:rng].shape[0])))
        data['initial_routes'] = [
            [0],
            [0],
            [0],
        ]
        data['num_vehicles'] = nTargets
        data['depot'] = 0
        return data


    def print_solution(data, manager, routing, solution):
        """Prints solution on console."""
        print(f'Objective: {solution.ObjectiveValue()}')
        max_route_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += ' {} -> '.format(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(
                    previous_index, index, vehicle_id)
            plan_output += '{}\n'.format(manager.IndexToNode(index))
            plan_output += 'Distance of the route: {}m\n'.format(route_distance)
            print(plan_output)
            max_route_distance = max(route_distance, max_route_distance)
        print('Maximum of the route distances: {}m'.format(max_route_distance))

#def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(transit_callback_index,0,300000000,True,dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    initial_solution = routing.ReadAssignmentFromRoutes(data['initial_routes'],True)
    print('Initial solution:')

    # Set default search parameters.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.time_limit.FromSeconds(30)
    search_parameters.log_search = True

    # Solve the problem.
    solution = routing.SolveFromAssignmentWithParameters(initial_solution, search_parameters)

    # Print solution on console.
    if solution:
        print('Solution after search:')
    print_solution(data, manager, routing, solution)
    
    routes = get_routes(solution, routing, manager)
    # Display the routes.
    for i, route in enumerate(routes):
        print('Route', i, route)
    return routes

#Solve rountes problem
ortoolsRoutes = getOrtoolsRoutes(dist_matrix,3)

print('\nSecond route: ')
#Print routes of the last target
print(ortoolsRoutes[2])