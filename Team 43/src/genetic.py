from client_moodle import *
import random
import json

k = 10
num_generations = 100

secret_key = 'A51UvRlUeV9TMY3xKjLgA3J4yvKFG4GfZwHqoORuGtH7S2Xkn0'

small_random_prob = 0.63

initial_coefficients = json.load(open("coefficients.txt"))
init = []

max_fitness = -1e12
best_coeff = []
errors = []

ratio = 1
mutation_range = 1e-13


def fitness_fn(training_error, validation_error):
    fitness = 1 / (0 * (training_error + validation_error) + 2 * abs(training_error - 0 * validation_error))

    return fitness


for i in initial_coefficients:
    if max_fitness < float(fitness_fn(initial_coefficients[i][0], initial_coefficients[i][1])):
        max_fitness = float(fitness_fn(initial_coefficients[i][0], initial_coefficients[i][1]))

        best_coeff = i.strip('][').split(', ')
        both_errors = (initial_coefficients[i][0], initial_coefficients[i][1])

    init.append(list(map(float, i.strip('][').split(', '))))

    errors.append((float(fitness_fn(initial_coefficients[i][0], initial_coefficients[i][1])), list(map(
        float, i.strip('][').split(', '))), (initial_coefficients[i][0], initial_coefficients[i][1])))

while len(init) < k:
    init.append(list(map(float, best_coeff)))
    errors.append((max_fitness, list(map(float, best_coeff)), both_errors))

err = [[1, 1] for j in range(k)]

state = [init[j] for j in range(k)]


# def get_errors(id, vector):
#     return [1, 10000]


# print(errors)
# print()
# print()
# print()


def mutate(child):
    no_of_mutation = random.randint(1, 3)
    # no_of_mutation = 1

    for i in range(no_of_mutation):
        index = random.randint(0, 10)

        new_val = random.uniform(-10, 10)
        new_val /= 100
        new_val *= child[index]

        child[index] += new_val
        child[index] = max(child[index], -10)
        child[index] = min(child[index], 10)

    return child


def crossover(child1, child2):
    crossover_point = random.randint(0, 10)
    a = child1[:crossover_point] + child2[crossover_point:]
    b = child2[:crossover_point] + child1[crossover_point:]

    return a, b


def store_best(fitness, err, errors):
    new_errors = errors

    for j in range(k):
        tup = (fitness[j], state[j], (err[j][0], err[j][1]))
        new_errors.append(tup)
    new_errors.sort(reverse=True)

    errors = [new_errors[j] for j in range(k)]

    return errors


def get_weights(fitness):
    const = 100 / sum(fitness)
    perc = [(const * fitness[j]) for j in range(k)]

    return perc


def select_new_population(old_population, weights, population_size):
    return random.choices(old_population, weights, k=population_size)


def crossover_and_mutate(population):
    for j in range(k // 2):
        population[2 * j], population[2 * j + 1] = crossover(population[2 * j], population[2 * j + 1])

        population[2 * j] = mutate(population[2 * j])
        population[2 * j + 1] = mutate(population[2 * j + 1])

    return population


for i in range(num_generations):

    err = [get_errors(secret_key, state[j]) for j in range(k)]
    fitness = [fitness_fn(err[j][0], err[j][1]) for j in range(k)]

    errors = store_best(fitness, err, errors)

    perc = get_weights(fitness)

    new_state = select_new_population(state, perc, k)
    new_state = crossover_and_mutate(new_state)

    state = new_state


# print(errors)

new_coefficients = {}
for i in range(k):
    new_coefficients[str(errors[i][1])] = [errors[i][2][0], errors[i][2][1]]

json.dump(new_coefficients, open("coefficients.txt", 'w'))
