class Environment:
    def __init__(self):
        self.rooms = {
            "A": 1,
            "B": 0,
            "C": 1
        }
class SimpleReflexVacuumAgent:
    def __init__(self, environment, start):
        self.environment = environment
        self.location = start
        self.actions = []
        self.cost = 0
    def run(self):
        sequence = ["A", "B", "C"]
        index = sequence.index(self.location)
        for i in range(3):
            current = sequence[index]
            if self.environment.rooms[current] == 1:
                self.environment.rooms[current] = 0
                self.actions.append("CLEAN " + current)
                self.cost += 1
            next_index = (index + 1) % 3
            next_room = sequence[next_index]
            self.actions.append("MOVE " + current + "->" + next_room)
            self.cost += 1
            index = next_index
        # Display results
        print("Actions:", self.actions)
        print("Cost:", self.cost)
        print(
            "Final:",
            "A=" + str(self.environment.rooms["A"]),
            "B=" + str(self.environment.rooms["B"]),
            "C=" + str(self.environment.rooms["C"])
        )
environment = Environment()
agent = SimpleReflexVacuumAgent(environment, "B")
agent.run()