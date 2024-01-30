import math
import matplotlib.pyplot as plt 
import numpy as np 

def winning_probability(dollars_risked, dollars_gained):
    return (1 - 0.6**(math.log2(dollars_risked)+1))**dollars_gained

def chance_of_winning(money_risking=128):
    x = np.linspace(0,100)
    y = winning_probability(money_risking,x)
    plt.plot(x,y,label="Martingale risk curve")
    plt.xlabel("Money gained")
    plt.ylabel("Probability of \"succeeding\"")
    plt.title(f"Chance you will win for a money gained while risking {money_risking}")
    plt.legend()
    

def exponential(x):
    return math.exp(x*-0.01)

if __name__ == "__main__":
    x = np.linspace(0,100)
    func = np.vectorize(exponential)
    plt.plot(x,func(x),label="My risk curve")
    chance_of_winning(128)
    plt.legend()
    plt.show()