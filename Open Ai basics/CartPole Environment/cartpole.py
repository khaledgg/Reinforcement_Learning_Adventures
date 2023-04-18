'''
Following the tutorial:

https://www.youtube.com/watch?v=2sp_eucoX2I
https://aleksandarhaber.com/cart-pole-control-environment-in-openai-gym-gymnasium-introduction-to-openai-gym/

Action Space:
Push Left
Push Right

Observation Space:
- Cart Position
- Cart Velocity
- Pole angle of rotation
- pole angular velocity

Episode Termination:

'''
import gym
import numpy as np
import time

#create environment
env = gym.make('CartPole-v1', render_mode = 'human')

(state,_)=env.reset()

# render the environment
env.render()
# close the environment
env.close()

# push cart in one direction
env.step(0)