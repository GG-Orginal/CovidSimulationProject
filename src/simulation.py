# Contains the logic for the loop that
# executes the actual simulation

from Person import Person
from random import randrange
import numpy as np

class simulation: 

    

    #Constructor 
    #def simulateCovid(self, is_infected, infected_counter): 
     


        #transmit method to see if the disease was transmitted between people

    def transmit(person, neighbor):

        #check to see if the person is compliant and the neighbor is compliant
        # if so, drop out 
        if (person.is_compliant == True) and (neighbor.is_compliant == True):
            return


        #check to see if the neighbor is healthy and if the person is healthy
        #if so, drop out
        if (neighbor.is_healthy == True) and (person.is_healthy == True):
            return


        #Generate a number that is less than 75, if so, it will return true
        random =  randrange(100) < 75
        if (random == True):

            # Possibilty that the virus will be transmitted
            infected_counter += 1
            person.is_infected = True
            neighbor.is_infected = True

    def initiatePopulation():
        #original_population_state = [[Person() for x in range(10)] for y in range (10)]
        original_population_state = np.empty((10,10), dtype = Person)
        return original_population_state

    def updateStatus(original_population_state):
        new_population_state = original_population_state[:]
        for i in range(len(new_population_state)):
          for j in range(len(new_population_state[i])):
             transmit(new_population_state[i][j], new_population_state[i][j+1])
             transmit(new_population_state[i][j], new_population_state[i][j-1])
             transmit(new_population_state[i][j], new_population_state[i+1][j])
             transmit(new_population_state[i][j], new_population_state[i-1][j])
        original_population_state = new_population_state[:]
        return original_population_state
            
