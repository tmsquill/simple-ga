from fuzzywuzzy import fuzz
import random
import string

class Agent:

	def __init__(self, length):

		self.string = ''.join(random.choice(string.letters) for _ in xrange(length))
		self.fitness = -1

	def __str__(self):

		return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness) 

in_str = None
in_str_len = None
population = 20
generations = 10000

def ga():

	agents = init_agents(population, in_str_len) 

	for generation in xrange(generations):

		print 'Generation: ' + str(generation)

		agents = fitness(agents)
		agents = selection(agents)
		agents = crossover(agents)
		agents = mutation(agents)

def init_agents(population, length):

	return [Agent(length) for _ in xrange(population)]

def fitness(agents):

	for agent in agents:

		agent.fitness = fuzz.ratio(agent.string, in_str)

	return agents

def selection(agents):

	agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
	print '\n'.join(map(str, agents))
	agents = agents[:int(0.2 * len(agents))]

	return agents

def crossover(agents):

	offspring = []

	for _ in xrange((population - len(agents)) / 2):

		parent1 = random.choice(agents)
		parent2 = random.choice(agents)
		child1 = Agent(in_str_len)
		child2 = Agent(in_str_len)
		split = random.randint(0, in_str_len)
		child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
		child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

		offspring.append(child1)
		offspring.append(child2)

	agents.extend(offspring)

	return agents

def mutation(agents):

	for agent in agents:

		for idx, param in enumerate(agent.string):

			if random.uniform(0.0, 1.0) <= 0.1:

				agent.string = agent.string[0:idx] + random.choice(string.letters) + agent.string[idx+1:in_str_len] 

	return agents

if __name__ == '__main__':

	in_str = 'TroySquillaci'
	in_str_len = len(in_str)
	ga()
