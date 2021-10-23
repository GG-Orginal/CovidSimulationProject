# Contains the logic for the loop that
# executes the actual simulation

from Person import Person
from random import randrange

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

    
            
