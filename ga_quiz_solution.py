from pyevolve import G2DList, GSimpleGA;
from pyevolve.DBAdapters import DBFileCSV, DBURLPost


def getScorePointsByDistribution(chromosome):
    """Score points counting the distribution of milk. With a better distribution, it returns higher results """
    score = 0.0
    # iterate over the chromosome
    for row in chromosome:
        partial_sum = 0.0
        for column in row:
            partial_sum += column
        if partial_sum == 175:
            score += 10

    return score


def getScorePointsOmittingRepetition(chromosome, possibleValues):
    """Score points counting the number of repetitions. With less repetitions, it returns higher points. """
    score = 0.0
    repeatedValues = getNumberRepeatedValues(chromosome, possibleValues)

    if repeatedValues > 30:
        score +=11
    elif repeatedValues > 20:
        score+=22
    elif repeatedValues > 10:
        score+=33
    elif repeatedValues > 5:
        score+=34
    elif repeatedValues == 0:
        score+=35

    return score;


def getNumberRepeatedValues(matrix, listValues):
    for row in matrix:
        for columnValue in row:
            if columnValue in listValues:
                listValues.remove(columnValue)
    return len(listValues);


def eval_func(chromosome):
    """Fitness Function"""
    score = getScorePointsByDistribution(chromosome)

    possible_values = list(xrange(49))
    score += getScorePointsOmittingRepetition(chromosome, possible_values)

    return score


"""Main Workflow"""

genome = G2DList.G2DList(7,7)

genome.evaluator.set(eval_func)

genome.setParams(rangemin=1, rangemax=49)

ga = GSimpleGA.GSimpleGA(genome)

ga.setPopulationSize(100)

ga.setGenerations(1000)

ga.setMutationRate(0.1)

csv_adapter = DBFileCSV(identify="run1", filename="./stats.csv")

ga.setDBAdapter(csv_adapter)

ga.evolve(freq_stats=100)

print ga.bestIndividual()


