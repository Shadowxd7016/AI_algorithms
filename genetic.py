import random

# -----------------------------
# Problem Data
# -----------------------------

items = ["N1", "N2", "N3", "N4", "N5", "N6"]

values = [14, 23, 8, 9, 17, 15]
weights = [1, 3, 7, 4, 5, 6]

capacity = 10

POP_SIZE = 10
MAX_GEN = 20
MUTATION_PROB = 0.1


# -----------------------------
# Create Initial Population
# -----------------------------
def initialize_population():
    """
    Create a population of random binary chromosomes.
    Each chromosome length = number of items.
    """
    population = []

    # TODO:
    # Generate POP_SIZE individuals
    for i in range(POP_SIZE):
        ind=[random.randint(0, 1) for _ in range(6)]
    # Each individual should be a list of 0s and 1s
        population.append(ind)
    # Example: [1,0,1,0,0,1]
    return population


# -----------------------------
# Fitness Function
# -----------------------------
def fitness(chromosome):
    """
    Calculate fitness of a chromosome.
    Fitness = total value of selected items.
    Apply penalty if weight exceeds capacity.
    """

    total_value = 0
    total_weight = 0

    # TODO:
    # Loop through chromosome
    i=0
    for gene in chromosome:
        if gene==1:
            total_value+=values[i]
            total_weight+=weights[i]
        i+=1
    # If gene == 1:
    #   add corresponding value
    #   add corresponding weight
    # TODO:
    if total_weight > capacity:
        total_value=1
    # apply penalty (return smaller fitness)
    
    return total_value


# -----------------------------
# Tournament Selection
# -----------------------------
def tournament_selection(population):
    """
    Select one parent using tournament selection.
    """

    k = 3  # tournament size

    # TODO:
    # Randomly select k individuals from population
    selected = random.sample(population, k)
    fit=[]
    for chromosome in selected:
        fit.append(fitness(chromosome))
    # Compute their fitness
    return selected[fit.index(max(fit))]
    # Return the one with highest fitness
    
    return None


# -----------------------------
# One Point Crossover
# -----------------------------
def crossover(parent1, parent2):
    """
    Perform one-point crossover.
    """

    # TODO:
    # Choose random crossover point
    point =random.randint(1, len(parent1) - 1)
    # Create two children by swapping genes
    
    child1 = parent1[:point]+parent2[point:]
    child2 = parent2[point:]+parent1[:point]

    return child1, child2


# -----------------------------
# Mutation
# -----------------------------
def mutate(chromosome):
    """
    Flip bits randomly based on mutation probability.
    """
    for i in range(len(chromosome)):
        rand_num=random.random()
        if rand_num < MUTATION_PROB:
            chromosome[i]=1-chromosome[i]
    # TODO:
    # For each gene:
    # if random number < MUTATION_PROB
    # flip bit (0->1, 1->0)

    return chromosome


# -----------------------------
# Replace Least Fit Individuals
# -----------------------------
def replacement(population, children):
    """
    Replace the least-fit individuals with new children.
    """

    # TODO:
    # Sort population based on fitness
    fitness_values = [fitness(ind) for ind in population]
    worst_idx1 = fitness_values.index(min(fitness_values))
    fitness_values[worst_idx1] = float('inf')
    worst_idx2 = fitness_values.index(min(fitness_values)) 
    
    # Replace the worst individuals
    population[worst_idx1] = children[0]
    population[worst_idx2] = children[1]
    return population


# -----------------------------
# Main Genetic Algorithm
# -----------------------------
def genetic_algorithm():

    population = initialize_population()

    for generation in range(MAX_GEN):

        # TODO:
        # Select two parents
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        # TODO:
        # Apply crossover
        child1, child2 = crossover(parent1, parent2)

        # TODO:
        # Apply mutation
        child1 = mutate(child1)
        child2 = mutate(child2)

        # TODO:
        # Replace worst individuals
        population = replacement(population, [child1, child2])

        # Optional: print best fitness each generation
        best = max(population, key=fitness)
        print("Generation:", generation, "Best:", best, "Fitness:", fitness(best))


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    genetic_algorithm()
