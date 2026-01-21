# Import necessary libraries
import numpy as np 
import pandas as pd
from sklearn.datasets import make_regression

# Create a base regression dataset devoid of noises and complexities
def generate_base_dataset(
        n_samples=500,
        n_features=6,
        noise=0.0,
        random_state=42
):
    X, y = make_regression(
        n_samples=n_samples,
        n_features=n_features,
        noise=noise,
        random_state=random_state
    )

    feature_names = [f"feature_{i+1}" for i in range(n_features)]
    X = pd.DataFrame(X, columns=feature_names)
    y = pd.Series(y, name="target")

    return X, y

# Add Gaussian noise to the target
def add_noise_to_target(y, noise_level=20, random_state=42):
    """
    Parameters:
    y (pd.Series): original target variable
    noise_level(float): standard deviation of the noise
    random_state(int): seed for reproducibility
    Returns:
    pd.Series: noisy targets 
    """

    np.random.seed(random_state)
    noise = np.random.normal(0, noise_level, size=y.shape[0])
    y_noisy = y + noise 
    return y_noisy

if __name__ == "__main__":
    # Generate base dataset
    X, y = generate_base_dataset()

    # Introduce noise to the target variable
    y_noisy = add_noise_to_target(y, noise_level=20)

    # Display first few rows 
    print(y.head())
    print(y_noisy.head())

# Introduce multicolinearity among features
def add_multicollinearity(X, correlated_pairs=[(0, 1)], noise_level=0.01, random_state=42):
    """
    Parameters:
    X (pd.DataFrame): original feature set
    n_correlated (int): number of features to make correlated
    correlation_strength (float): strength of correlation (0 to 1)
    random_state (int): seed for reproducibility
    Returns:
    pd.DataFrame: feature set with multicollinearity induced
    """

    np.random.seed(random_state)
    X_corr = X.copy()
    
    for base_idx, corr_idx in correlated_pairs:
        X_corr.iloc[:, corr_idx] = X_corr.iloc[:, base_idx] * 0.8 + \
        np.random.normal(0, noise_level, size=X.shape[0])

    return X_corr


if __name__ == 'main':
    X, y = generate_base_dataset()
    X_corr = add_multicollinearity(X, correlated_pairs=[(0, 1)])
    print(X.head())
    print(X_corr.head())


# Downsample the base dataset
def downsample_dataset(X, y, n_samples=50, random_state=42):
    """
    Return smaller sample from base dataset
    
    Parameters:
    X (pd.DataFrame): features
    y (pd.Series): target
    n_samples(int): number of samples
    random_state (int): random seed

    Retruns:
    X_small, y_small
    """
    np.random.seed(random_state)
    idx = np.random.choice(X.index, size=n_samples, replace=False)
    return X.loc[idx].reset_index(drop=True), y.loc[idx].reset_index(drops=True)

# Quick test
if __name__ == "__main__":
    X, y = generate_base_dataset()
    X_small, y_small = downsample_dataset(X, y, n_samples=50)
    print(X_small.shape, y_small.shape)