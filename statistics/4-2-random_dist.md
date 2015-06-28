[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

* Exercise 2: 
 * Generate 1000 numbers using random.random plot the PMF and CDF. Is the distribution is uniform?

* Code:
```
import thinkstats2
import thinkplot
import random

t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show(xlabel='1000 Random Numbers', ylabel='PMF - Probability')

cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Probability of 1000 Random numbers (PMF)', ylabel='CDF - Precentile of Probability')

print "The distribution is uniform."
```

* Answer: The distribution is uniform, because the PMF's distribution is rectangular while the CDF's is a straight line.
* Output:
  * PMF & CDF on 1000 generated numbers from random.random
    * PMF
    ![Imgur](http://i.imgur.com/ZVk3phd.png)
    * CDF
    ![Imgur](http://i.imgur.com/rI8g4L2.png)
