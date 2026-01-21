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

