from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
from _core import is_winner, opponent, start 

start(MLAgent)

class MyAgent(MLAgent):
  def evaluate(self, board):
      if is_winner(board, self.symbol):
          reward = 1
      elif is_winner(board, opponent[self.symbol]):
          reward = -1
      else:
          reward = 0
      return reward
    
 
my_agent = load('MyAgent_3000')
my_agent.learning = True

validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

plot_validation(validation_result)