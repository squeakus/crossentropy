import random
import numpy as np
from matplotlib import pyplot
import graph
#random.seed(0)

def fitness(indiv):
    difference = 0
    target = [9,9,9,9,9,9,9,9,9,9]

    for idx, val in enumerate(target):
        difference += abs(val - indiv[idx])

    return difference

def print_pop(population):
    for indiv in population:
        print indiv, "fitness:", fitness(indiv)

def init_pop(popsize, length):
    population = []
    for _ in range(popsize):
        indiv = []
        for i in range(length):
            indiv.append(random.randint(0,9))
        population.append(indiv)
    return population

def next_pop(popsize, mean, std):
    population = []

    for _ in range(popsize):
        indiv = []
        for idx, val in enumerate(mean):
            indiv.append(random.gauss(mean[idx], std[idx]))
        population.append(indiv)
    return population

def get_distributions(population):
    poparray = np.array(population)
    mean = np.mean(poparray, 0)
    std = np.std(poparray,0)
    return mean, std

def main():
    popsize, variables, elites = 100, 100, 10
    fitnesses = []
    pop = init_pop(popsize, variables)

    for gen in range(50):
        pop.sort(key=fitness)
        #print "gen", gen, "best indiv:", pop[0], "fitness", fitness(pop[0])
        fitnesses.append(fitness(pop[0]))
        
        #now make the next set
        best = pop[:elites]
        mean, std = get_distributions(best)
        pop = next_pop(popsize, mean, std)

        # this shows the distribution of the first row
        #firstrow = [row[1] for row in pop]
        #print firstrow
        #pyplot.hist(firstrow)
        #pyplot.xlim(-5,15)
        #pyplot.show()

    return fitnesses

def experiment():
    runs = []

    for i in range(50):
        run = main()
        runs.append(run)

    graph.plot_3d(runs, "cross entropy")

if __name__ == '__main__':
    experiment()

