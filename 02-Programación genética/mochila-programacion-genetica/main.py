import random


def should_mutate(pct):
  pass

def mutate(agent, pct):
  if should_mutate(pct):
    random_value_1 = random.randint(0, len(agent) - 1)
    agent[random_value_1] = 0 if agent[random_value_1] == 0 else 1
  
  return agent
 

def select_best_population(population, population_size):
  pass

def fitness(agent):
  pass

def merge(population, childrens):
  merged_population = population + childrens
  return merged_population

def create_agent(agent_size):
  return [random.randint(0, 1) for _ in range(agent_size)]

def create_population(population_size, agent_size):
  return [create_agent(agent_size) for x in range(population_size)]
   
def crossover(agent1, agent2):
  pass


def main(population_size, max_generations, mutation_pct=0.05):
  backpack_weight_limit = 15
  objects = [{"weight": 1, "value": 1},
            {"weight": 6, "value": 4},
            {"weight": 4, "value": 7},
            {"weight": 5, "value": 6},
            {"weight": 1, "value": 3},
            {"weight": 6, "value": 8},
            {"weight": 3, "value": 6},
            {"weight": 10, "value": 11},
            {"weight": 4, "value": 4},
            {"weight": 7, "value": 3}]