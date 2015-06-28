[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

* Problem: Compute the median, mean, skewness and Pearson's skewness of the resulting sample.  
  * Question: What fraction of households reports a taxable income below the mean?  
    * Answer for log_upper=6: 0.660005879567
    * Answer for log_upper=7: 0.856563066521
  * Question: How do the results depend on the assumed upper bound?
    * Answer:  
      * Increasing the upper bound also increases moment-based skewness. 
      * The Pearson skewness suprizingly goes down. It seems that "increasing the upper bound has a modest effect on the mean, and a stronger effect on standard deviation. Since std is in the denominator with exponent 3, it has a stronger effect on the result." (Allen B Downey)

*Code
```
# Makes a sample of log10 household income.
def InterpolateSample(df, log_upper=6.0):
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample

def main():
    df = hinc.ReadData()
    log_sample_a = InterpolateSample(df, log_upper=6.0)
    log_sample_b = InterpolateSample(df, log_upper=7.0)

    # CDF & PDF plots with an log_upper of 6.0
    log_cdf = thinkstats2.Cdf(log_sample_a)
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')

    sample = np.power(10, log_sample_a)
    mean, median = density.Summarize(sample)

    pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='PDF')

    cdf = thinkstats2.Cdf(sample)
    print("log_upper = 6.0")
    print('cdf[mean]', cdf[mean])
    print(" ")

    # CDF & PDF plots with an log_upper of 6.0
    log_cdf = thinkstats2.Cdf(log_sample_b)
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')

    sampleb = np.power(10, log_sample_b)
    meanb, medianb = density.Summarize(sampleb)

    pdfb = thinkstats2.EstimatedPdf(sampleb)
    thinkplot.Pdf(pdfb)
    thinkplot.Show(xlabel='household income',
                   ylabel='PDF')

    cdf = thinkstats2.Cdf(sampleb)
    print("log_upper = 7.0")
    print('cdf[mean]', cdf[meanb])
    print(" ")

if __name__ == "__main__":
    main()
```

* Output:
-------Results with log_upper=6-------
mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
cdf[mean]: 0.660005879567

  * CDF
![Imgur](http://i.imgur.com/HUD3m9s.png)
 * PDF
![Imgur](http://i.imgur.com/ZtmPVsK.png)

-------Results with log_upper=7-------
mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277
cdf[mean] 0.856563066521

  * CDF
![Imgur](http://i.imgur.com/4Q35k4N.png)
  * PDF
![Imgur](http://i.imgur.com/qCrjlEb.png)
