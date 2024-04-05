import random

def generate_players():
    num_players = random.randint(2, 10)
    return num_players

def generate_edges():
    num_edges = random.randint(2, 8)
    return num_edges

def generate_edge_functions(num_edges):
    edge_functions = []
    for i in range(num_edges):
        a = round(random.random(), 2)  # Round to 2 decimal points
        b = round(random.random(), 2)  # Round to 2 decimal points
        edge_functions.append((a, b))
    return edge_functions

""" initial optimal allocation (different problem)
def assign_edges_to_players(num_players, num_edges, edge_functions):
    player_edges = [None] * num_players  # Initialize list to store player-edge associations
    edge_players = [[] for _ in range(num_edges)]  # Initialize list to store players for each edge
    for player_id in range(1, num_players + 1):
        min_cost = 50  # Initialize minimum cost to infinity
        best_edge_id = None
        for edge_id in range(num_edges):
            edge_function = edge_functions[edge_id]  # Get edge function for this edge
            total_players_on_edge = len(edge_players[edge_id])  # Total number of players using this edge
            cost = total_players_on_edge * edge_function[0] + edge_function[1]
            if cost < min_cost:
                min_cost = cost
                best_edge_id = edge_id
        player_edges[player_id - 1] = best_edge_id  # Store edge ID for this player
        edge_players[best_edge_id].append(player_id)  # Store player ID for this edge
    return player_edges, edge_players
"""

def assign_edges_to_players_arbitrary(num_players, num_edges):
    player_edges = [random.randint(0, num_edges - 1) for _ in range(num_players)]
    edge_players = [[] for _ in range(num_edges)]
    for player_id, edge_id in enumerate(player_edges):
        edge_players[edge_id].append(player_id)
    return player_edges, edge_players

"""
def calculate_cost(num_players_on_edge, edge_function):
    cost = num_players_on_edge * edge_function[0] + edge_function[1]
    return round(cost,5)
"""

def calculate_player_cost(player_id, edge_functions, player_edges):
    edge_id = player_edges[player_id]
    edge_function = edge_functions[edge_id]
    num_players_on_edge = len([p for p in player_edges if p == edge_id])
    cost = edge_function[0] * num_players_on_edge + edge_function[1]
    return round(cost, 3)  # Round the cost to 3 decimals


"""
def optimize_edges(player_edges, edge_players, edge_functions):
    num_players = len(player_edges)
    num_edges = len(edge_functions)
    while True:
        changed = False
        for player_id in range(num_players):
            current_edge = player_edges[player_id]
            current_cost = calculate_cost(len(edge_players[current_edge]), edge_functions[current_edge])
            min_cost = current_cost
            best_edge_id = current_edge
            for new_edge_id in range(num_edges):
                print("edge functions: ",edge_functions)
                print("number of players: ",num_players)
                print("playes edges: ",player_edges)
                print("edges player: ",edge_players)
                print("current cost:",current_cost)
                if new_edge_id != current_edge:
                    new_cost = calculate_cost(len(edge_players[new_edge_id]), edge_functions[new_edge_id])
                    print("got inside")
                    if new_cost < min_cost:
                        min_cost = new_cost
                        best_edge_id = new_edge_id
            if best_edge_id != current_edge:
                edge_players[current_edge].remove(player_id + 1)
                edge_players[best_edge_id].append(player_id + 1)
                player_edges[player_id] = best_edge_id
                changed = True
        if not changed:
            break
    return player_edges, edge_players
"""

def optimize_allocation(player_edges, edge_functions):
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
                global count
                count+=1
                changed = True
    return player_edges

for k in range(2,11):
    for m in range(2,9):
        n=10000
        total_count=0
        for it in range(n):
            #num_players = generate_players()
            num_players = k
            #num_edges = generate_edges()
            num_edges = m
            edge_functions = generate_edge_functions(num_edges)

            #player_edges, edge_players = assign_edges_to_players(num_players, num_edges, edge_functions)
            player_edges, edge_players = assign_edges_to_players_arbitrary(num_players, num_edges)
            """
            print("num of players: ",num_players)
            print("num of edges: ",num_edges)
            print("edges functions: ",edge_functions)
            print("-------->Initial Player-edge associations:", player_edges)
            """
            initial_cost=0
            for j in range(num_players):
                #print("player",j+1,"initial cost: ",calculate_player_cost(j,edge_functions,player_edges))
                initial_cost+=calculate_player_cost(j,edge_functions,player_edges)

            count=0
            optimized_player_edges = optimize_allocation(player_edges, edge_functions)
            # we just did the first optimization for the allocation
            # Keep optimizing until no more changes happen, and counting them
            while True:
                new_player_edges = optimize_allocation(optimized_player_edges, edge_functions)
                if new_player_edges == optimized_player_edges:
                    break
                optimized_player_edges = new_player_edges
                

            # Print the optimized allocations
            final_totalcost=0
            for player_id, edge_id in enumerate(optimized_player_edges):
                cost = calculate_player_cost(player_id, edge_functions, optimized_player_edges)
                #print(f"Player {player_id+1} assigned to Edge {edge_id+1} with cost {cost}")
                final_totalcost+=cost

            """
            print("-------->final player-edge allocation: ", player_edges)
            print("Initial cost was: ",initial_cost," and final cost was: ",final_totalcost)
            """
            #print("number of changes in allocation: ",count)

            total_count+=count
        print("for k=",k," and m=",m," , the average changes out of 1000 is: ",total_count/10000)

#print("avg runs to converge to sol: ",total_count/n)

