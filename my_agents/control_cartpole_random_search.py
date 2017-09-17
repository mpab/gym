import gym
import random
import numpy as np

from statistics import median, mean
from collections import Counter

LR = 1e-3
env = gym.make("CartPole-v0")
env.reset()
goal_steps = 500
score_requirement = 50
initial_games = 10000

def random_search_control_run_episode(required_reward, env, parameters):
    
    observation = env.reset()
    env._max_episode_steps = required_reward
    env._reward_threshold = required_reward * 0.975
    totalreward = 0

    for _ in range(required_reward):
        
        env.render()

        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward

        if (done):
            break

    return totalreward

def random_search_control():

    required_reward = 5000

    bestparams = None
    bestreward = 0

    for _ in range(1000):
        parameters = np.random.rand(4) * 2 - 1
        
        reward = random_search_control_run_episode(required_reward, env, parameters)

        if (reward > bestreward):
            bestreward = reward
            bestparams = parameters
            print ("Improvement: ", reward, "rewards" )
            print ("parameters: ", parameters)

        if (reward == required_reward):
            print ("Success!")
            break
            
random_search_control()
