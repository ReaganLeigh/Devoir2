from schedule import Schedule
from solver_naive import solve as naive_solve  
import random


def cost(schedule: Schedule, solution: dict) -> int:
    return schedule.get_n_creneaux(solution)

# solution naive
def generate_initial_solution(schedule: Schedule) -> dict:
    sol = naive_solve(schedule)   
    schedule.verify_solution(sol) 
    return sol


def generate_neighbors(solution: dict, schedule: Schedule) -> list[dict]:
    neighbors = []

    courses = list(solution.keys())
    course = random.choice(courses) # on prend randomly un cours

    current_slot = solution[course]
    used_slots = set(solution.values())

    # on essaie tous les créneaux déjà utilisés
    for slot in used_slots:
        if slot == current_slot:
            continue
        new_sol = solution.copy()
        new_sol[course] = slot      # essaie de mettre un cours dans un nouveau timeslot
        neighbors.append(new_sol)   # retourne toutes les solutions possibles ou non

    return neighbors

# Trouve le meilleur prochaine voisin à explorer et retourne celui-ci
def select_neighbor(valid_neighbors: list[dict], schedule: Schedule) -> dict:
    best = None
    best_cost = None
    for n in valid_neighbors: # parcours les voisins et évalue leur nombre de timeslots (cost)
        c = cost(schedule, n)
        if best is None or c < best_cost: # si le voisin courant est meilleur que le précédent, on le garde
            best = n
            best_cost = c
    return best



def solve(schedule: Schedule):
    S = generate_initial_solution(schedule)
    S_best = S.copy()
    best_cost = cost(schedule, S_best)

    max_iter = 10000
        

    
    return S_best
