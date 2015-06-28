[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

* Code
```
import thinkstats2
import thinkplot

# CleanFenResp() is an empty function
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    pass

def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

resp = ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='Actual')

biased = BiasPmf(pmf, label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel='Family Size', ylabel='Probability')

print 'Means of Children in a household:'
print 'Actual PMF mean', pmf.Mean()
print 'Biased PMF mean', biased.Mean()
```

* Output
![Imgur](http://i.imgur.com/LaoisUM.png)
```
Means of Children in a household:
Actual mean 1.02420515504
Biased mean 2.40367910066
```


