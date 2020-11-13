import gym
from gym_fishing.envs.abstract_fishing_env import AbstractFishingEnv

class FishingCtsEnv(AbstractFishingEnv):
    def __init__(self,
                 r = 0.3, 
                 K = 1, 
                 sigma = 0.1,
                 init_state = 0.75,
                 Tmax = 100,
                 file = None):
        super().__init__(params = {"r": r, "K": K, "sigma": sigma},
                         init_state = init_state,
                         Tmax = Tmax,
                         file = file)

