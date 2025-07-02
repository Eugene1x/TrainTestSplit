import numpy as np

def trainTestSplit(X, Y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    num_samples = len(X)
    indices = np.arange(num_samples)
    np.random.shuffle(indices)

    split_index = int(num_samples * (1 - test_size))

    train_indices = indices[:split_index]
    test_indices = indices[split_index:]

    x_train = X[train_indices]
    y_train = Y[train_indices]
    x_test = X[test_indices]
    y_test = Y[test_indices]

    return x_train, x_test, y_train, y_test
