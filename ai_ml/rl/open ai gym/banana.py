import gym
import gym_banana

env = gym.make('Banana-v0')

count = 0 
for _ in range(1):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  print(action)
  observation, reward, done, info = env.step(action)
  print("obseravtion : ", observation)
  
  # count+=1
  # print(count)

  if done:
    observation = env.reset()
env.close()