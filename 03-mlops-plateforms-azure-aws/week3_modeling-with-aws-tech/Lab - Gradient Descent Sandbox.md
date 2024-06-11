# Gradient Descent Sandbox

## Lab Goal

Experiment with gradient descent optimization by iteratively running cells in a Jupyter notebook.

## Lab Description

In this interactive lab you will implement gradient descent in a live Jupyter notebook to minimize f(x)=x^2. You will run code cells to define the problem, execute gradient descent, and visualize the optimization path. By tweaking parameters and re-running cells, you can gain intuition for how learning rates, convergence thresholds, and other hyperparameters affect performance.

## Lab Steps
1. Import libraries (matplotlib, numpy)
2. Define objective function f(x)=x^2
3. Compute derivative function df(x)/dx
4. Initialize gradient descent settings
5. Run gradient descent cell
6. Plot visualization
7. Tweak parameters like learning rate, iterations, etc
8. Rerun cells to experiment with effects


## Reflection Questions
1. How does the learning rate affect convergence speed and accuracy?
2. What causes gradient descent diverge?
3. Should you minimize loss or minimize the absolute value of df(x)?
4. How can you tweak code to improve visualization?
5. What other objective functions could you experiment with?

## Challenge Exercises
1. Try different learning rates and numbers of iterations.
2. Modify the function to f(x) = x^3.
3. Print f(x) over iterations to show minimization.
4. Set a convergence threshold and stop early if reached.
5. Compare gradient descent to other SciPy optimizers.

