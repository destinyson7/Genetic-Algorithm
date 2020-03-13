from client_moodle import *
import random

k = 4
small_random_prob = 0.63
init1 = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
init2 = [ random.uniform(-10, 10) for i in range(11) ]
init3 = [ random.uniform(-10, 10) for i in range(11) ]
init4 = [ random.uniform(-10, 10) for i in range(11) ]

err1 = err2 = err3 = err4 = [1, 1]

state = [[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12], [0.0, -5.690169131131135, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12], [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12], [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, -8.528488635238805, 4.1614924993407104e-11, -6.732420176902565e-12]]
best = state
mini = 1e17
def mutate(child):
	index = random.randint(0, 10)
	new_val = random.uniform(-10, 10)
	child[index] = new_val
	return child

for i in range(10):
	err1 = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', state[0])
	err2 = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', state[1])
	err3 = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', state[2])
	err4 = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', state[3])

	# print(err1, err2, err3, err4, state, end = '\n')
	print(err1)
	print(err2)
	print(err3)
	print(err4)
	print(state)
	print()
	print()
	print()

	fitness1 = err1[0] + 100*err1[1]
	fitness2 = err2[0] + 100*err2[1]
	fitness3 = err3[0] + 100*err3[1]
	fitness4 = err4[0] + 100*err4[1]
	if min((fitness1, fitness2, fitness3, fitness4)) < mini:
		mini = min((fitness1, fitness2, fitness3, fitness4))
		best = state 

	const = 100 / (1/fitness1 + 1/fitness2 + 1/fitness3 + 1/fitness4)
	perc1 = const / fitness1
	perc2 = const / fitness2
	perc3 = const / fitness3
	perc4 = const / fitness4

	new_state = []
	for j in range(k):
		val = random.uniform(0, 100)
		if val < perc1:
			new_state.append(state[0])
		elif val < perc1 + perc2:
			new_state.append(state[1])
		elif val < perc1 + perc2 + perc3:
			new_state.append(state[2])
		else:
			new_state.append(state[3])

	for j in range(k//2):
		crossover_point = random.randint(0, 10)
		temp = new_state[2*j]
		new_state[2*j] = new_state[2*j][:crossover_point] + new_state[2*j + 1][crossover_point:]
		new_state[2*j + 1] = new_state[2*j + 1][:crossover_point] + temp[crossover_point:]
		
		mutation_prob = random.uniform(0, 1)
		if mutation_prob > small_random_prob:
			new_state[2*j] = mutate(new_state[2*j])

		mutation_prob = random.uniform(0, 1)
		if mutation_prob > small_random_prob:
			new_state[2*j + 1] = mutate(new_state[2*j + 1])

	state = new_state

print("******", best, "*******")