# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---
* Answer: Making an estimate in this manner is slightly biased.
  * MeanError: -0.029850746268656716

* Code:
```
import math
import random
import numpy as np
import thinkplot
import thinkstats2

def RMSE(estimates, actual):
    """
    Computes the root mean squared error of a sequence of estimates.
    estimate: sequence of numbers
    actual: actual value
    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    """Computes the mean error of a sequence of estimates.
    estimate: sequence of numbers
    actual: actual value
    returns: float mean error
    """
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

# Simulates a game and returns the estimated goal-scoring rate.
def SimulateGame(lam):
    # lam: actual goal scoring rate in goals per game
    # Lam: 1.0 / Desired mean of 1 (Game)
    # lam's (lambda's) distribution is 1
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1

    # estimated goal-scoring rate is the actual number of goals scored
    # print ('Games: ', games)
    L = goals
    return L

def VertLine(x, y=1):
    thinkplot.Plot([x, x], [0, y], color="0.8", linewidth=3)

# Simulates multiple game and returns the estimated goal-scoring rate.
def SimulateGames(lam, games):
    # lam: actual goal scoring rate in goals per game
    # Lam: 1.0 / Desired mean of 1 (Game)
    # lam's (lambda's) distribution is 1

    # L = SimulateGame(lam)
    estimates = []
    count = 0
    while count <= games:
        estimates.append(SimulateGame(lam))
        count += 1

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    # Vertical Line at 5th Percentile
    VertLine(ci[0])
    # Vertical Line at 95th Percentile
    VertLine(ci[1])

    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel='goal-score rate mean',
                   ylabel='CDF',
                   title='goals-score rate distribution')

    #print ('Goal Rates: ', estimates)

    print ('RMSE: ', RMSE(estimates, lam))
    print ('MeanError: ', MeanError(estimates, lam))
    print ""

SimulateGames(2, 200)
```

* Output
```
('confidence interval', (0, 4))
('RMSE: ', 1.4728048848560087)
('MeanError: ', -0.029850746268656716)
```
![Imgur](http://i.imgur.com/FQvmuw6.png)

* Benign Error
```
C:\Users\Joshua\Anaconda\lib\site-packages\matplotlib\axes\_axes.py:475: UserWarning: No labelled objects fo
  warnings.warn("No labelled objects found. "
```
---
