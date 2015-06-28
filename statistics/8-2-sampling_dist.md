[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

* Exercise 8.2: Suppose you draw a sample with size $n=10$ from a population with an exponential disrtribution with lambda=2.  Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.

* Conlusions:
  * As sample size increases, standard error and the CI decreases 
  * All three CI's contain the actual value 2.

* Code:
```
import thinkstats2
import thinkplot
import numpy as np
import math

# Computes the root mean squared error of a sequence of estimates.
def RMSE(estimates, actual):
    """
    estimate: sequence of numbers
    actual: actual value
    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

# Sampling distribution of L as an estimator of exponential parameter.
def SimulateSample_Exp_Dist(lam=2, n=10, m=1000):
    # lam: parameter of an exponential distribution
    # n: sample size
    # m: number of iterations

    # 1/lam = the mean of an exp. distribution
    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1.0 / np.mean(xs)
        estimates.append(L)

    # Compute Standard Error
    stderr = RMSE(estimates, lam)
    print('standard error', stderr)

    # This function plots vertical lines at at the CI's Percentile endpoints
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color="0.8", linewidth=3)

    # Compute Confidence Interval
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95) # 90% CI
    print('confidence interval', ci)
    # Vertical Line at 5th Percentile
    VertLine(ci[0])
    # Vertical Line at 95th Percentile
    VertLine(ci[1])

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')
    print ""
    return stderr
print "------- n = 10 -------"
SimulateSample_Exp_Dist()
print "------- n = 100 -------"
SimulateSample_Exp_Dist(2, 100, 1000)
# print "------- n = 200 -------"
# SimulateSample_Exp_Dist(2, 200, 1000)
# print "------- n = 500 -------"
# SimulateSample_Exp_Dist(2, 500, 1000)
print "------- n = 1000 -------"
SimulateSample_Exp_Dist(2, 1000, 1000)
```

* Output
```
------- n = 10 -------
('standard error', 0.7981030858885545)
('confidence interval', (1.2741381519173596, 3.5258972562027693))
```
![Imgur](http://i.imgur.com/w9KaKYJ.png)
  * Benign Error
```
C:\Users\Joshua\Anaconda\lib\site-packages\matplotlib\axes\_axes.py:475: UserWar
  warnings.warn("No labelled objects found. "
```

```
------- n = 100 -------
('standard error', 0.19617726405747027)
('confidence interval', (1.7135686665456182, 2.3516234748376941))
```
![Imgur](http://i.imgur.com/F8jULNm.png)

```
------- n = 1000 -------
('standard error', 0.06375074861560748)
('confidence interval', (1.895057145581325, 2.101630531798047))
```
![Imgur](http://i.imgur.com/mrhvxrJ.png)
