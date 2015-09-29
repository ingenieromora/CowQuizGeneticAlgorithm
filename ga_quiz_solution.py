from pyevolve import G2DList, GSimpleGA;

def getNumberRepeatedValues(matrix, listValues):
    for row in matrix:
        for columnValue in row:
            if columnValue in listValues:
                listValues.remove(columnValue)
    return len(listValues);

def eval_func(chromosome):
    score = 0.0
    # iterate over the chromosome
    for row in chromosome:
        partial_sum = 0.0
        for column in row:
            partial_sum += column

        if partial_sum == 175:
            score += 10

    cowList = list(xrange(49))
    repeatedValues = getNumberRepeatedValues(chromosome, cowList)

    if repeatedValues < 30:
        score +=10
    elif repeatedValues < 20:
        score+=20
    elif repeatedValues < 10:
        score+=30
    elif repeatedValues < 40:
        score+=30
    elif repeatedValues == 0:
        score+=1000

    return score

genome = G2DList.G2DList(7,7)
genome.evaluator.set(eval_func)
genome.setParams(rangemin=1, rangemax=49)
ga = GSimpleGA.GSimpleGA(genome)
ga.evolve(freq_stats=10000)
print ga.bestIndividual()

#TODO Hacer que en la representacion no haya numeros repetidos
#TODO Hacer que se impriman SOLO aquellas poblaciones cuyo resuletado fue 70