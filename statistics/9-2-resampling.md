[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

* Conclusion: "Using resampling instead of permutation has very little effect on the results. The two models are based on slightly difference assumptions, and in this example there is no compelling reason to choose one or the other. But in general p-values depend on the choice of the null hypothesis; different models can yield very different results." (Downey)

* Code:
```
import hypothesis
import numpy as np
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
live = live[live.prglngth > 27]
live = live[live.totalwgt_lb > 0]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

class DiffMeansResample(hypothesis.DiffMeansPermute):
    """Tests a difference in means using resampling."""

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2

data_prglngth = firsts.prglngth.values, others.prglngth.values
ht = DiffMeansResample(data_prglngth)
p_value = ht.PValue(iters=10000)
print('\nmeans permute preglength')
print('p-value =', p_value)
print('actual =', ht.actual)
print('ts max =', ht.MaxTestStat())

data_birthwgt = firsts.birthwgt_lb.values, others.birthwgt_lb.values
ht = DiffMeansResample(data_birthwgt)
p_value = ht.PValue(iters=10000)
print('\nmeans permute preglength')
print('p-value =', p_value)
print('actual =', ht.actual)
print('ts max =', ht.MaxTestStat())
```
