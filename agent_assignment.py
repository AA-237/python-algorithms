class Agent:
    def __init__(self, name, location, isAvailable=True):
        self.name = name
        self.location = location
        self.isAvailable = isAvailable

class Request:
    def __init__(self, volume, location):
        self.volume = volume
        self.location = location

class AgentSystemManager:
    def __init__(self):
        self.agents = [] # list of agents

    def add_agent(self, agent):    
        self.agents.append(agent)

    # function to find cloaset available agents    
    def closest_available_agents(self, request):
        min_distance = float('inf')
        closest_agent = None
        for agent in self.agents:
            if agent.isAvailable:
                distance = self.calculate_distance(agent.location, request.location)
                if distance < min_distance:
                    min_distance = distance
                    closest_agent = agent
        return closest_agent

   # handling a request
    def handle_request(self, request):
        if request.volume < 160:
            return self.closest_available_agents(request)
        else:
            available_agents_distance = []           
            for agent in self.agents:
                if agent.isAvailable:
                    distance = self.calculate_distance(agent.location, request.location)
                    available_agents_distance.append((agent, distance))
            # available_agents_distance.sort()  
            available_agents = []
            for agent, distance in available_agents_distance:
                available_agents.append(agent)
            return available_agents  
    
    
    @staticmethod
    def calculate_distance(location1, location2):
        # return math.sqrt((location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2)    
        return abs(location1 - location2)        


# Example for testing by changing values
agent1 = Agent("Mark", 10)
agent2 = Agent("Sam", 20)
agent3 = Agent("Fred", 40, False)

system = AgentSystemManager()
system.add_agent(agent1)
system.add_agent(agent2)
system.add_agent(agent3)

request1 = Request(190, 16)
# request2 = Request(180, 46)


result = system.handle_request(request1)
print(result)

if request1.volume < 160:
    print(f"The closest agents available is {result.name} at location {result.location}.")
else:
    print(f"The available agent sported by distance are: ")
    for agent in result:
        print(f"{agent.name} at location {agent.location}.")
               
