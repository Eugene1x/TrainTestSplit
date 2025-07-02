import numpy as np

if randomState is not None:
    np.random.seed(randomState)

numSamples = len(x)

indices = np.arange(numSamples)
print(indices)