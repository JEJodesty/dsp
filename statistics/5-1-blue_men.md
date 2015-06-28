[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

* Question: What percentage of the US male population is in the range of 5'10'' & 6'1''?
* Output/Answer:
```
("Percentage of the US male population is between 5'10'' & 6'1'':", 34.209468294
```

* Code:
```
# scipy.stats contains objects that represent analytic distributions
import scipy.stats

mu = 178
sigma = 7.7
# scipy.stats.norm represents a normal distribution.
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

# How many people are between 5'10" and 6'1"?
low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
low, high, high-low

diff = high-low
perc = 100 * diff

print('Percentage of the US male population is between 5\'10\'\' & 6\'1\'\':', perc)
```
