import random
import string


target = 'The quick brown fox jumped over the lazy dog, The quick brown fox jumped over the lazy dog'
mutation_rate = 1/len(target)

def get_random_string(length):
    return ''.join(random.choice(string.printable) for _ in range(length))


def get_difference(s1, s2):
   return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def create_child(parent1, parent2):
    fitness1 = get_difference(parent1, target)
    fitness2 = get_difference(parent2, target)

    child = ''
    for i in range(len(target)):
        if random.random() < mutation_rate:
            child+=str(random.choice(string.printable))
        else:
            child+=str(random.choice(fitness2*parent1[i] + fitness1*parent2[i]))

    return child
    
def get_fittest(sample):
    fittest = ''
    min_v = 100
    for test in sample:
        if get_difference(test, target) < min_v:
            fittest = test
            min_v = get_difference(test, target)

    second_fittest = ''
    second_min_v = 100
    for test in sample:
        if get_difference(test, target) < second_min_v and test != fittest:
            second_fittest = test
            second_min_v = get_difference(test, target)
    
    return fittest, second_fittest

size = 100
population = [get_random_string(len(target)) for _ in range(size)]

starting_group = [get_random_string(len(target)) for _ in range(size)]



turn = 1
while True:
    parent1, parent2 = get_fittest(starting_group)
    print(turn, parent1, get_difference(parent1, target))
    if get_difference(parent1, target) == 0:
        break
    new_gen = [create_child(parent1, parent2) for _ in starting_group]
    starting_group = new_gen
    turn +=1

