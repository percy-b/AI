import random

def generate_individual():
    # Generate a random individual (a list of numbers)
    return [random.uniform(-10, 10) for _ in range(3)]

def evaluate_fitness(individual):
    # Evaluate the fitness of an individual (the maximum value of the function)
    x, y, z = individual
    return x**2 + y**2 + z**2

def select_fittest(population, num_selected):
    # Select the fittest individuals from the population
    return sorted(population, key=evaluate_fitness, reverse=True)[:num_selected]

def mutate(individual):
    # Introduce mutations to an individual
    mutated = []
    for gene in individual:
        if random.random() < 0.1:  # 10% chance of mutation
            mutated.append(gene + random.gauss(0, 1))  # Add a random Gaussian noise
        else:
            mutated.append(gene)
    return mutated

def genetic_algorithm(num_generations):
    # Main function to run the genetic algorithm
    population = [generate_individual() for _ in range(100)]  # Initialize the population
    for i in range(num_generations):
        fittest = select_fittest(population, 50)  # Select the fittest individuals
        population = fittest  # Replace the population with the fittest individuals
        population += [mutate(individual) for individual in fittest]  # Introduce mutations to create a new generation
    return population[0]  # Return the fittest individual in the final generation

solution = genetic_algorithm(100)
print(solution)  # Output: [x, y, z] (the maximum value of the function)
