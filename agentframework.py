import random

class Agent():
    def __init__(self, environment, agents):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
    
    def __str__(self):
       return "x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store)
    
    def move(self):
        """
        This modifies the x and y variable for the agent increasing or decreasing them randomly

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
            
    def eat(self):
        """ This allows the agents to interact with the environment."""
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share_with_neighbourhood(self, neighbourhood):
        """
        This searches for close neighbours and shares resources with them.

        Parameters
        ----------
        neighbourhood : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                average = sum /2
                # self.store = average
                self.store = average
                # agent.store = average
                agent.store = average
                #test code print below
                #print("sharing " + str(distance) + " " + str(average))
    # End if
# End loop
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

