import random
import pylab
import numpy

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    for rabbit in range(0,CURRENTRABBITPOP):
        if random.random() <= 1.0 - CURRENTRABBITPOP / MAXRABBITPOP:
            CURRENTRABBITPOP += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for fox in range(0,CURRENTFOXPOP):
        if random.random() <= CURRENTRABBITPOP/MAXRABBITPOP and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= .33333:
                CURRENTFOXPOP += 1
        elif random.random() <= .90 and CURRENTFOXPOP > 10:
            CURRENTFOXPOP -= 1
            
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    fox_pop_over_time = []
    rabbit_pop_over_time = []
    for trial in range(0,numSteps):
        rabbitGrowth()
        foxGrowth()
        fox_pop_over_time.append(CURRENTFOXPOP)
        rabbit_pop_over_time.append(CURRENTRABBITPOP)
    pylab.plot(fox_pop_over_time)
    pylab.plot(rabbit_pop_over_time)
    coeff = numpy.polyfit(range(len(fox_pop_over_time)), fox_pop_over_time, 2)
    pylab.plot(numpy.polyval(coeff, range(len(fox_pop_over_time))))

print(runSimulation(200))
