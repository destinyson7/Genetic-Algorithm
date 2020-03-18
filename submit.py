from client_moodle import *
import json

secret_key = 'se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2'

coefficients = json.load(open("coefficients.txt"))

init = []

min_error = 10000000000
best_coeff = []

for i in coefficients:
    init.append(list(map(float, i.strip('][').split(', '))))

for i in range(len(init)):
    submit(secret_key, init[i])
