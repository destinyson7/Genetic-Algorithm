# from client_moodle import *
import random
import json

k = 4
num_iterations = 10

secret_key = 'se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2'

small_random_prob = 0.63

initial_coefficients = json.load(open("coefficients.txt"))
init = []

min_error = 10000000000
best_cooeff = []
errors = []

for i in initial_coefficients:
    if min_error > float(initial_coefficients[i]):
        min_error = float(initial_coefficients[i])
        best_cooeff = i.strip('][').split(', ')

    init.append(list(map(float, i.strip('][').split(', '))))
    errors.append((float(initial_coefficients[i]), list(map(
        float, i.strip('][').split(', ')))))

while len(init) < k:
    init.append(list(map(float, best_cooeff)))
    errors.append((float(min_error), list(map(float, best_cooeff))))

err = [[1, 1] for j in range(4)]

state = [init[j] for j in range(4)]


def get_errors(id, vector):
    return [1, 10000]


def mutate(child):
    index = random.randint(0, 10)

    new_val = random.uniform(-0.5, 0.5)
    child[index] += new_val

    if child[index] < -10:
        child[index] = 10

    elif child[index] > 10:
        child[index] = 10

    return child


def crossover(child1, child2):
    crossover_point = random.randint(0, 10)
    a = child1[:crossover_point] + child2[crossover_point:]
    b = child2[:crossover_point] + child1[crossover_point:]

    return a, b


def select(prob_weights):
    val = random.uniform(0, 100)

    if val < prob_weights[0]:
        return state[0]

    elif val < prob_weights[0] + prob_weights[1]:
        return state[1]

    elif val < prob_weights[0] + prob_weights[1] + prob_weights[2]:
        return state[2]

    else:
        return state[3]


for i in range(num_iterations):
    err = [get_errors(secret_key, state[j]) for j in range(k)]

    fitness = [err[j][1] for j in range(k)]

    # print(i, errors)
    # print()
    # print()
    # print()

    new_errors = errors
    new_errors.append((fitness[0], state[0]))
    new_errors.append((fitness[1], state[1]))
    new_errors.append((fitness[2], state[2]))
    new_errors.append((fitness[3], state[3]))
    new_errors.sort()

    errors = [new_errors[0], new_errors[1], new_errors[2], new_errors[3]]

    const = 100 / (1 / fitness[0] + 1 / fitness[1] +
                   1 / fitness[2] + 1 / fitness[3])

    perc = [const/fitness[j] for j in range(k)]

    new_state = [select(perc) for j in range(k)]

    for j in range(k // 2):
        new_state[2 * j], new_state[2 * j +
                                    1] = crossover(new_state[2 * j], new_state[2 * j + 1])

        new_state[2 * j] = mutate(new_state[2 * j])
        new_state[2 * j + 1] = mutate(new_state[2 * j + 1])

    state = new_state

new_coefficients = {
    str(errors[0][1]): errors[0][0],
    str(errors[1][1]): errors[1][0],
    str(errors[2][1]): errors[2][0],
    str(errors[3][1]): errors[3][0],
}

json.dump(new_coefficients, open("coefficients.txt", 'w'))
