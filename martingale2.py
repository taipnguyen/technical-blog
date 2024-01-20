import math
import matplotlib.pyplot as plt 
import numpy as np 

def winning_probability(dollars_risked, dollars_gained):
    return (1 - 0.6**(math.log2(dollars_risked)+1))**dollars_gained

def chance_of_winning():
    x = np.linspace(0,100)
    y = winning_probability(128,x)
    plt.plot(x,y)
    plt.xlabel("Money gained")
    plt.ylabel("Probability of \"succeeding\"")
    plt.title("Chance you will win for a money gained")
    plt.show()

def regular_log(x):
    return 1-(0.9)**x

if __name__ == "__main__":
    x = np.linspace(1,100)
    func = np.vectorize(regular_log)
    plt.plot(x,func(x))
    chance_of_winning()