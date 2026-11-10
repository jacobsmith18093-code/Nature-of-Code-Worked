import random
import string
from math import *

def random_Character():
    character = random.choice(string.ascii_lowercase + " ")
    return character

class DNA:
    def __init__(self, length):
        self.genes = []
        self.fitness = 0 
        for i in range(length):
            self.genes.append(random_Character())
        
    def crossover(self,partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0,len(self.genes))
        for i in range(len(child.genes)):
            if i <= midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child
def generateRandomPop(n,target):
    population = []
    for i in range(n):
        population.append(DNA(len(target)))
    return population

def calculate_Fitness(target, pop):
    for i in pop:
        score=- 0 
        for j in range(len(target)):
            if i.genes[j] == target[j]:
                score+= 1
        i.fitness = (score**2)/(len(target)**2)
def generate_Mating_Pool(pop):
    mating_pool = []
    for e in pop:
        n=floor(e.fitness*100)
        for i in range(n):
            mating_pool.append(e)
    return mating_pool

def breedNewPopulation(n, mating_pool):
    new_pop =[]
    for i in range(n):
        parent_a = random.choice(mating_pool)
        parent_b = random.choice(mating_pool)
        child = parent_a.crossover(parent_b)
        new_pop.append(child)
    return new_pop
def mutate_Popuylation(population, mutation_rate):
    for e in population:
        for c in range(len(e.genes)):
            if random.random() < mutation_rate:
                e.genes[c] = random_Character()
    return population
def CheckForWinners(population,target):
    for e in population:
        print("Generation", generation , "".join(e.genes))
        if "".join(e.genes) == target:
            print("Target reached", "".join(e.genes))
            return True
    return False

target = "to be or not to be that is the question"
n = 150 
population = generateRandomPop(n, target)
mutation_rate = 0.01
generation = 0

while not CheckForWinners(population, target):
    calculate_Fitness(target, population)
    mating_pool = generate_Mating_Pool(population)
    population = breedNewPopulation(n, mating_pool)
    generation += 1
    population = mutate_Popuylation(population, mutation_rate)