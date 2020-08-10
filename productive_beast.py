
class Node():
    def __init__(self, identification, action, level):
        self.id = identification
        self.action = action
        self.level = level


class Stack():
    def __init__(self):
        self.content = []
    
    def add(self, node):
        self.content.append(node)

    def remove(self):
        if self.content != []:
            node = self.content[-1]
            self.content = self.content[:-1]
            return node

class Queue():
    def __init__(self):
        self.content = []
    
    def add(self, node):
        self.content.append(node)

    def remove(self):
        if self.content != []:
            node = self.content[0]
            self.content = self.content[1:]
            return node

class Game():

    def __init__(self, obstacle1, obstacle2, obstacle3, method):
        self.actions = ["jump", "duck", "incant"]
        self.method = method
        self.arrangement = [obstacle1, obstacle2, obstacle3]        
        self.rules = {
                        "b" : "jump", 
                        "d" : "duck", 
                        "n" : "incant"
                     }
        self.explored = []
        self.checking = []
        self.solution = []
        self.nodeSolution = []
        self.goal = [self.rules[obstacle1], self.rules[obstacle2], self.rules[obstacle3]]

    # Expands only until the number of obstacles.
    # Decision tree is as deep as the number of obstacles excluding the initial state,
    def expand(self, parent, method, actions):
        print("(Expanding selected node ...)")
        print(f"parent: {parent.id} {parent.action} {parent.level}")
        increment = 0
        for action in actions:
            increment += 1
            level = parent.level + 1
            nodeID = round(parent.id + 0.1 ** level * increment, level)
            node = Node(identification=nodeID, action=action, level=level)
            print(f"child: {node.id} {node.action} {node.level}")
            method.add(node)
        self.checking = None 
        if isinstance(method, Queue):
            print("(Queueing child nodes ...)")  
        elif isinstance(method, Stack):
            print("(Pushing child nodes ...)")



    def explore(self, node):
        if len(self.solution) <= 2 and node.action == self.goal[len(self.solution)] and node.level-1 == len(self.solution):
            self.nodeSolution.append(node)
            self.solution.append(node.action)
        self.explored.append(node)

    def run(self):
        if self.method == "dfs":
            
            stack = Stack()
            initial = Node(identification=0, action=None, level=0)
            stack.add(initial)

            while self.solution != self.goal:
                print("............................")
                print("Current Nodes in Stack:")
                for i in stack.content:
                    print(f"{i.id} {i.action}")
                print("............................")
                check = stack.remove()
                self.checking = check
                self.explore(check)
                print(f"Popped Node: ID-({check.id}) ACTION-({check.action}) LEVEL-({check.level})")
                if check.level < 3:
                    self.expand(parent=check, method=stack, actions=self.actions)
                    

            else:
                print("")
                print("==========   Unexplored  ============")
                for i in stack.content:
                    print(f"{i.id} {i.action}")
                print(f"States unexplored: {len(stack.content)}")
                print("==========   Explored   ==============")
                for i in self.explored:
                    print(f"{i.id} {i.action}")
                print(f"States explored: {len(self.explored)}")
                print("========== The solution ==============")
                for step in self.nodeSolution:
                    print(f"{step.id} {step.action}")
                print("NOW IN THE WORKPLACE! WORK YOUR ASS OFF!")

        elif self.method == "bfs":
            
            queue = Queue()
            initial = Node(identification=0, action=None, level=0)
            queue.add(initial)

            while self.solution != self.goal:
                print("............................")
                print("Current Nodes in Queue:")
                for i in queue.content:
                    print(f"{i.id} {i.action}")
                print("............................")
                check = queue.remove()
                self.checking = check
                self.explore(check)
                print(f"Dequeued Node: ID-({check.id}) ACTION-({check.action}) LEVEL-({check.level})")
                if check.level < 3:
                    self.expand(parent=check, method=queue, actions=self.actions)
                    

            else:
                print("")
                print("==========  Unexplored ============")
                for i in queue.content:
                    print(f"{i.id} {i.action}")
                print(f"States unexplored: {len(queue.content)}")
                print("==========  Explored  ==============")
                for i in self.explored:
                    print(f"{i.id} {i.action}")
                print(f"States explored: {len(self.explored)}")
                print("==========The solution==============")
                for step in self.nodeSolution:
                    print(f"{step.id} {step.action}")
                print("YOUR AGENT IS IN THE WORKPLACE! WORK YOUR ASS OF NOW!")
print("")
print("")
print("**********************************************")
print('       WELCOME TO THE PRODUCTIVTY BEAST       ')
print("**********************************************")
print("")
print("")
print("Goal: help the agent get to its workplace")
print("Obstacle: b-bed d-flying Doritos, n-Netflix portal (obstacles may be repeated)")
print("Actions: jump, duck, and incant")
print("Rule: Agent should jump over a bed, duck under flying Doritos, and incant when faced with a Netflix portal.")
print("Note: Agent starts with a state found in an empty space and gets to its workplace once all obstacles are cleared.")
print('Note: "If there is a will, there is a way." The agent will always be able to find a way to reach its workplace.')
print("")
print("")
print("Please layout the obstacles (b, d, n) and state the search method (bfs or dfs).")
first_input = input("State the first obstacle: ").lower()
second_input = input("State the second obstacle: ").lower()
third_input = input("State the third obstacle: ").lower()
method = input("bfs or dfs: ").lower()
work =  Game(first_input, second_input, third_input, method)
work.run()








    