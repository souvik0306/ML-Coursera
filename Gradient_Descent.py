import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time 
import pickle
learning_rate = 0.01

def mean_square_error(y_true,y_predicted):
    cost = np.sum((y_true-y_predicted)**2)/len(y_true)
    return cost

def gradient_descent(x,y,iterations=1000,learning_rate=0.01,stopping_threshold=1e-6):
    current_weights = 0.1
    current_bias = 0.01
    iterations = iterations
    learning_rate = learning_rate
    n = float(len(x))

    costs = []
    weights = []
    previous_cost = None

    plt.ion()
    figure, ax = plt.subplots(figsize=(7,5))
    line1, = ax.plot(costs,weights)
    plt.xlabel('Weight')
    plt.ylabel('Cost')
    plt.ion()

    for i in range(iterations):

        y_predicted = (current_weights*x) + current_bias

        current_cost = mean_square_error(y,y_predicted)

        if previous_cost and abs(previous_cost-current_cost)<=stopping_threshold:
            break

        previous_cost = current_cost

        costs.append(current_cost)
        weights.append(current_weights)

        weight_derivative = -(2/n)*sum(x*(y-y_predicted))
        bias_derivative = -(2/n)*sum(y-y_predicted)

        current_weights = current_weights-(learning_rate * weight_derivative)
        current_bias = current_bias-(learning_rate * bias_derivative)

        print(f"Iteration {i+1}: Cost - {current_cost}, Weight - {current_weights}, Bias - {current_bias}" )
    
        # plt.plot(weights,costs)
        #plt.plot(costs, weights, 'bo')
        new_y = costs[i]

        line1.set_xdata(weights[i])
        line1.set_ydata(new_y)

        figure.canvas.draw()

        figure.canvas.flush_events()

        time.sleep(0.01)
            
        plt.scatter(weights[i],costs[i],marker='o',color='red')
        

    return current_bias,current_bias

x = 2 * np.random.rand(50,1)
y = 3 * x+np.random.randn(50,1)


estimated_weight,estimated_bias = gradient_descent(x,y,iterations = 2000)
y = estimated_weight*x+estimated_bias