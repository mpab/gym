import gym
import random
import numpy as np

env = gym.make("CartPole-v0")
env.reset()

def random_search_control_run_episode(required_reward, env, parameters):
    
    observation = env.reset()
    env._max_episode_steps = required_reward
    env._reward_threshold = required_reward * 0.975
    totalreward = 0

    for _ in range(required_reward):
        
        #env.render()
        env.render(close=True)

        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward

        if (done):
            break

    return totalreward

def random_search_control(start_parameters = None):

    required_reward = 5000

    bestparams = None
    bestreward = 0

    for _ in range(1000):
        if (start_parameters == None):
            parameters = np.random.rand(4) * 2 - 1
        else:
            parameters = start_parameters
        
        reward = random_search_control_run_episode(required_reward, env, parameters)

        if (reward > bestreward):
            bestreward = reward
            bestparams = parameters
            print ("Improvement: ", reward, "rewards" )
            print ("parameters: ", parameters)

        if (reward == required_reward):
            print ("Success!")
            break

if __name__ == "__main__":
    random_search_control([ 0.26594176, 0.31772193, 0.92617377, 0.35116463])
    #random_search_control()
