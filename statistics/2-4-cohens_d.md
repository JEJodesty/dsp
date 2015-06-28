[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

* Exercise 2.4: Investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quatify the difference detween groups. 
  * Question: How does it compare to the difference in pregnancy length?

* Answer
```
First born babies are approximately 0.117 lbs (1.88 oz) lighter that other babies:
Cohen d of first born and other babies' weight:
The difference in weight means is Approx. -0.087

First born babies where born approximately 0.06 weeks later
Cohen d of first born and other babies' pregnancy length:
The difference in pregnancy length means is Approx. 0.029
```

* Code
```
import thinkstats2
import numpy as np
import math

def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df


def CleanFemPreg(df):
    # mother's age is encoded in centiyears; convert to years
    df.agepreg /= 100.0
    # birthwgt_lb contains at least one bogus value (51 lbs)
    # replace with NaN
    df.birthwgt_lb[df.birthwgt_lb > 20] = np.nan
    # replace 'not ascertained', 'refused', 'don't know' with NaN
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    df.hpagelb.replace(na_vals, np.nan, inplace=True)
    df.babysex.replace([7, 9], np.nan, inplace=True)
    df.nbrnaliv.replace([9], np.nan, inplace=True)
    # birthweight is stored in two columns, lbs and oz.
    # convert to a single column in lb
    # NOTE: creating a new column requires dictionary syntax,
    # not attribute assignment (like df.totalwgt_lb)
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
    # due to a bug in ReadStataDct, the last variable gets clipped;
    # so for now set it to NaN
    df.cmintvw = np.nan

# Cohen's d.
def CohenEffectSize(group1, group2):
    """Compute
    group1: Series or NumPy array
    group2: Series or NumPy array
    returns: float
    """
    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

# Explore the difference in weight between first babies and others.
def WeightDifference(live, firsts, others):
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    std_dev1 = firsts.prglngth.std()
    std_dev2 = others.prglngth.std()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    print('------Weight------')
    print('---Mean')
    print('First babies', mean1)
    print('Others', mean2)
    print ('---Standard Deviation')
    print ('First babies', std_dev1)
    print ('Others', std_dev2)
    print('---Variance')
    print('First babies', var1)
    print('Others', var2)
    print ('---Differences')
    print('Difference in lbs', mean1 - mean2)
    print('Difference in oz', (mean1 - mean2) * 16)
    print('Difference relative to mean (%age points)',
          (mean1 - mean2) / mean0 * 100)

    d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('---Cohen d', d)
    print ""

# Explore the difference in pregnancy length between first babies and others.
def LengthDifference(live, firsts, others):
    mean0 = live.prglngth.mean()
    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()

    std_dev1 = firsts.prglngth.std()
    std_dev2 = others.prglngth.std()

    var1 = firsts.prglngth.var()
    var2 = others.prglngth.var()
    print('------Pegnancy Length------')
    print('---Mean')
    print('First babies', mean1)
    print('Others', mean2)
    print ('---Standard Deviation')
    print ('First babies', std_dev1)
    print ('Others', std_dev2)
    print('---Variance')
    print('First babies', var1)
    print('Others', var2)
    print('---Diferences')
    print('Difference in pergnancy length', mean1 - mean2)
    print('Difference relative to mean (%age points)',
          (mean1 - mean2) / mean0 * 100)

    d = CohenEffectSize(firsts.prglngth, others.prglngth)
    print('---Cohen d', d)
    print ""

preg = ReadFemPreg()
live = preg[preg.outcome == 1]
live = live[live.prglngth > 27]
live = live[live.totalwgt_lb > 0]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

WeightDifference(live, firsts, others)
LengthDifference(live, firsts, others)
```

*Output
```
------Weight------
---Mean
('First babies', 7.2384382217090071)
('Others', 7.3561745364381199)
---Standard Deviation
('First babies', 2.4488029373012217)
('Others', 2.1689497188194857)
---Variance
('First babies', 1.8265303984117147)
('Others', 1.8028984031621189)
---Differences
('Difference in lbs', -0.11773631472911283)
('Difference in oz', -1.8837810356658053)
('Difference relative to mean (%age points)', -1.6129746743593874)
('---Cohen d', -0.087408739945202638)

------Pegnancy Length------
---Mean
('First babies', 38.722863741339495)
('Others', 38.655023717119448)
---Standard Deviation
('First babies', 2.4488029373012217)
('Others', 2.1689497188194857)
---Variance
('First babies', 5.9966358257350905)
('Others', 4.7043428827671256)
---Diferences
('Difference in pergnancy length', 0.067840024220046757)
('Difference relative to mean (%age points)', 0.17535259551908602)
('---Cohen d', 0.029389469448765332)
```
