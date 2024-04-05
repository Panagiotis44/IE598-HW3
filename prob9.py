import random
import itertools
def generate_edge_functions(num_edges):
    edge_functions = []
    for i in range(num_edges):
        a = round(random.random(), 2)  # Round to 2 decimal points
        b = round(random.random(), 2)  # Round to 2 decimal points
        edge_functions.append((a, b))
    return edge_functions

def assign_edges_to_players_arbitrary(num_players, num_edges):
    player_edges = [random.randint(0, num_edges - 1) for _ in range(num_players)]
    edge_players = [[] for _ in range(num_edges)]
    for player_id, edge_id in enumerate(player_edges):
        edge_players[edge_id].append(player_id)
    return player_edges, edge_players

def calculate_player_cost(player_id, edge_functions, player_edges):
    edge_id = player_edges[player_id]
    edge_function = edge_functions[edge_id]
    num_players_on_edge = len([p for p in player_edges if p == edge_id])
    cost = edge_function[0] * num_players_on_edge + edge_function[1]
    return round(cost, 3)  # Round the cost to 3 decimals

def generate_edge_functions(num_edges):
    edge_functions = []
    for i in range(num_edges):
        a = round(random.random(), 2)  # Round to 2 decimal points
        b = round(random.random(), 2)  # Round to 2 decimal points
        edge_functions.append((a, b))
    return edge_functions

def calculate_final_total_cost(edge_assignment, edge_functions):
    total_cost = sum(calculate_player_cost(player_id, edge_functions, edge_assignment) for player_id in range(len(edge_assignment)))
    return total_cost

def find_min_total_cost(edge_functions, optimized_player_edges):
    num_players = len(optimized_player_edges)
    num_edges = len(edge_functions)
    initial_total_cost = sum(calculate_player_cost(player_id, edge_functions, optimized_player_edges) for player_id in range(num_players))
    min_total_cost = initial_total_cost
    
    # Generate all possible allocations of players to edges
    for edge_assignment in itertools.product(range(num_edges), repeat=num_players):
        total_cost = calculate_final_total_cost(edge_assignment, edge_functions)
        if total_cost < min_total_cost:
            min_total_cost = total_cost
    
    return min_total_cost

def enumerate_edge_allocations_with_cost(num_players, num_edges, edge_functions):
    # Generate all possible allocations of players to edges
    edge_allocations_with_cost = []
    for allocation in itertools.product(range(num_edges), repeat=num_players):
        total_cost = calculate_final_total_cost(allocation, edge_functions)
        edge_allocations_with_cost.append((allocation, total_cost))
    return edge_allocations_with_cost

def choose_minimum_total_cost_allocation(edge_allocations_with_cost):
    min_total_cost = float('inf')
    min_cost_allocation = None
    for allocation, total_cost in edge_allocations_with_cost:
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            min_cost_allocation = allocation
    return min_cost_allocation, min_total_cost
"""
def find_pure_nash_equilibria_with_costs(num_players, num_edges, edge_functions):
    pure_nash_equilibria = []
    total_costs = []
    
    # Generate all possible allocations of players to edges
    edge_allocations = itertools.product(range(num_edges), repeat=num_players)
    
    # Check each allocation for Nash equilibrium
    for allocation in edge_allocations:
        is_nash_equilibrium = True
        for player_id in range(num_players):
            current_cost = calculate_player_cost(player_id, edge_functions, allocation)
            for new_edge_id in range(num_edges):
                if new_edge_id != allocation[player_id]:
                    new_allocation = list(allocation)
                    new_allocation[player_id] = new_edge_id
                    new_cost = calculate_player_cost(player_id, edge_functions, new_allocation)
                    if new_cost < current_cost:
                        is_nash_equilibrium = False
                        break
            if not is_nash_equilibrium:
                break
        if is_nash_equilibrium:
            pure_nash_equilibria.append(allocation)
            total_cost = calculate_total_player_cost_pure_nash_equilibrium(allocation, edge_functions)
            total_costs.append(total_cost)
    
    return pure_nash_equilibria, total_costs

"""
def find_pure_nash_equilibria_with_costs(num_players, num_edges, edge_functions):
    pure_nash_equilibria = []
    total_costs = []
    
    # Generate all possible allocations of players to edges
    edge_allocations = itertools.combinations_with_replacement(range(num_edges), num_players)
    
    # Check each allocation for Nash equilibrium
    for allocation in edge_allocations:
        sorted_allocation = tuple(sorted(allocation))
        is_nash_equilibrium = True
        for player_id in range(num_players):
            current_cost = calculate_player_cost(player_id, edge_functions, sorted_allocation)
            for new_edge_id in range(num_edges):
                if new_edge_id != sorted_allocation[player_id]:
                    new_allocation = list(sorted_allocation)
                    new_allocation[player_id] = new_edge_id
                    new_cost = calculate_player_cost(player_id, edge_functions, tuple(new_allocation))
                    if new_cost < current_cost:
                        is_nash_equilibrium = False
                        break
            if not is_nash_equilibrium:
                break
        if is_nash_equilibrium:
            pure_nash_equilibria.append(sorted_allocation)
            total_cost = calculate_total_player_cost_pure_nash_equilibrium(sorted_allocation, edge_functions)
            total_costs.append(total_cost)
    
    return pure_nash_equilibria, total_costs

def calculate_total_player_cost_pure_nash_equilibrium(allocation, edge_functions):
    total_cost = calculate_final_total_cost(allocation, edge_functions)
    return total_cost

"""def find_PoA(k,m):
    num_players = k
    num_edges = m
    edge_functions = generate_edge_functions(num_edges)
    player_edges, edge_players = assign_edges_to_players_arbitrary(num_players, num_edges)
    edge_allocations_with_cost = enumerate_edge_allocations_with_cost(num_players, num_edges, edge_functions)
    min_cost_allocation, min_total_cost = choose_minimum_total_cost_allocation(edge_allocations_with_cost)
    pure_nash_equilibria, total_costs = find_pure_nash_equilibria_with_costs(num_players, num_edges, edge_functions)
    return total_costs[0]/min_total_cost"""

max_PoA= 0
"""
for n in range(2):
    k=random.randint(2,10)
    m=random.randint(2,8)
    PoA=find_PoA(k,m)
    print("now the PoA is: ",PoA)
    if PoA>max_PoA:
        max_PoA=PoA

print("worst PoA (and PoS) is: ",max_PoA)"""

for k in range(100):
    

    num_players = random.randint(2,10)
    num_edges = random.randint(2,8)

    edge_functions = generate_edge_functions(num_edges)

    player_edges, edge_players = assign_edges_to_players_arbitrary(num_players, num_edges)

    #print("players number is",num_players,"edges number is ",num_edges)
    #print(edge_functions)

    edge_allocations_with_cost = enumerate_edge_allocations_with_cost(num_players, num_edges, edge_functions)
    min_cost_allocation, min_total_cost = choose_minimum_total_cost_allocation(edge_allocations_with_cost)
    #print("Minimum Total Cost Allocation:", min_cost_allocation)
    #print("Minimum Total Cost:", min_total_cost)

    pure_nash_equilibria, total_costs = find_pure_nash_equilibria_with_costs(num_players, num_edges, edge_functions)
    #print("Pure Nash Equilibria:", pure_nash_equilibria[0])
    #print("Total Player Costs:", total_costs[0])

    # we see that all the pure nash equilibria have the same cost so we just need to choose one to divide it with the optimal cost
    # we will choose the first one without loss off generality
    #PoA=Pos

    PoA=total_costs[0]/min_total_cost
    if PoA>max_PoA:
        max_PoA=PoA
    print("Price of arachy is: ",PoA)

print("worst PoA is ",max_PoA)