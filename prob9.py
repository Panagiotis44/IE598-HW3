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

"""def optimize_allocation(player_edges, edge_functions):
    num_players = len(player_edges)
    num_edges = len(edge_functions)
    changed = True
    while changed:
        changed = False
        for player_id in range(num_players):
            current_cost = calculate_player_cost(player_id, edge_functions, player_edges)
            best_cost = current_cost
            best_edge_id = player_edges[player_id]
            for new_edge_id in range(num_edges):
                if new_edge_id != best_edge_id:      
                    new_cost = calculate_player_cost(player_id, edge_functions, [new_edge_id if i == player_id else e for i, e in enumerate(player_edges)])
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_edge_id = new_edge_id
            if best_edge_id != player_edges[player_id]:
                player_edges[player_id] = best_edge_id
                changed = True
    return player_edges"""

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


def calculate_total_player_cost_pure_nash_equilibrium(allocation, edge_functions):
    total_cost = calculate_final_total_cost(allocation, edge_functions)
    return total_cost

k=6
m=4
num_players = k
num_edges = m

edge_functions = generate_edge_functions(num_edges)

player_edges, edge_players = assign_edges_to_players_arbitrary(num_players, num_edges)
"""
optimized_player_edges = optimize_allocation(player_edges, edge_functions)

while True:
    new_player_edges = optimize_allocation(optimized_player_edges, edge_functions)
    if new_player_edges == optimized_player_edges:
        break
    optimized_player_edges = new_player_edges

optimal_cost=0
for player_id, edge_id in enumerate(optimized_player_edges):
    cost = calculate_player_cost(player_id, edge_functions, optimized_player_edges)
    #print(f"Player {player_id+1} assigned to Edge {edge_id+1} with cost {cost}")
    optimal_cost+=cost
"""
print("players number is",num_players,"edges number is ",num_edges)
print(edge_functions)
"""
optimized_player_edges = optimize_allocation(player_edges, edge_functions)
            
while True:
    new_player_edges = optimize_allocation(optimized_player_edges, edge_functions)
    if new_player_edges == optimized_player_edges:
        break
    optimized_player_edges = new_player_edges
                
"""
"""            
final_totalcost=0
for player_id, edge_id in enumerate(optimized_player_edges):
    cost = calculate_player_cost(player_id, edge_functions, optimized_player_edges)
    print(f"Player {player_id+1} assigned to Edge {edge_id+1} with cost {cost}")
    final_totalcost+=cost        
print("the final totalcost is ",final_totalcost)
"""

"""min_total_cost = find_min_total_cost(edge_functions, optimized_player_edges)
print("Minimum Total Cost:", min_total_cost)"""

edge_allocations_with_cost = enumerate_edge_allocations_with_cost(num_players, num_edges, edge_functions)
min_cost_allocation, min_total_cost = choose_minimum_total_cost_allocation(edge_allocations_with_cost)
print("Minimum Total Cost Allocation:", min_cost_allocation)
print("Minimum Total Cost:", min_total_cost)

pure_nash_equilibria, total_costs = find_pure_nash_equilibria_with_costs(num_players, num_edges, edge_functions)
print("Pure Nash Equilibria:", pure_nash_equilibria[0])
print("Total Player Costs:", total_costs[0])

# we see that all the pure nash equilibria have the same cost so we just need to choose one to divide it with the optimal cost
# we will choose the first one without loss off generality
#PoA=Pos

PoA=total_costs[0]/min_total_cost
print("Price off arachy is: ",PoA)