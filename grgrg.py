import numpy as np

x = np.arange(10)  # Just 0 to 9
randomState = 100 # Try None too

if randomState is not None:
    np.random.seed(randomState)

np.random.shuffle(x)
print(x)
