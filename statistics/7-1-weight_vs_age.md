[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

* Excersize 7-1: Make a scatter plot of birth weight versus mother's age. Plot percentiles of birth weight versus mother's age. Compute Pearson's and Spearman's correlations. 
  * Question: How would you characterize the relationship between these variables?

* Code:
```
import numpy as np
import first
import thinkplot
import thinkstats2

thinkstats2.RandomSeed(17)

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

# Bin the data by age and plot percentiles of weight for each bin.
bins = np.arange(10, 48, 3)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)

thinkplot.Show(root='chap07scatter3', formats=['jpg'],
               xlabel="mother's age (years)",
               ylabel='birth weight (lbs)')

ages = live.agepreg
weights = live.totalwgt_lb

#ScatterPlot
thinkplot.Scatter(ages, weights, alpha=1.0)
thinkplot.Config(xlabel='age (years)',
                 ylabel='weight (lbs)',
                 xlim=[10, 45],
                 ylim=[0, 15],
                 legend=False)
thinkplot.Show(root='chap07scatter1',
               legend=False,
               formats=['jpg'])

print("Pearson's Correlation", thinkstats2.Corr(ages, weights))
print("Spearman's Correlation",
      thinkstats2.SpearmanCorr(ages, weights))
```

* Output:
  * Percentiles Plot
![Imgur](http://i.imgur.com/MsNttJm.png)
  * Scatter Plot
![Imgur](http://i.imgur.com/oiENcnJ.png)
```
-------Pearson's and Spearman's Correlations-------
("Pearson's Correlation", 0.068833970354109084)
("Spearman's Correlation", 0.094610041096582262)
```

* Answer:
```
The scatterplot shows a weak relationship between the variables 
baised on the correlations. Pearson's is approximately 0.07, 
and Spearman's is approximately 0.09. 
"The difference between them suggests some influence
of outliers or a non-linear relationsip"

"Plotting percentiles of weight versus age suggests that the
relationship is non-linear.  Birth weight increases more quickly
in the range of mother's age from 15 to 25.  After that, the effect
is weaker."

(Allen B, Downey)
```
