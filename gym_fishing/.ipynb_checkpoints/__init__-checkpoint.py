from gym.envs.registration import register

register(
    id="fishing-v0",
    entry_point="gym_fishing.envs:FishingEnv",
)
