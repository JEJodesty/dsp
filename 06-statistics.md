# Learn Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats" width="250" style="float: left;" />](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.


Complete the following exercises. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (Cohen's d)
2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (a random distribution)
4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (blue men)
5. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (household income)
6. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (weight vs. age)
7. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
8. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
9. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)


---

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?
```
Background Information: WikiGender: http://www.wikigender.org/index.php/Sex_Differences_and_Twins 
Twins: Estimated to be approximately 1.9% of the world population 
Monozygotic Twins (8% of all twins): making up 0.2% of the total world population 

Method: Think about twin birth events, rather than individual twins, and remember that Elvis was a twin as background information.

Hypotheses:
A: Elvis's birth event was an identical birth event
B: Elvis's birth event was a fraternal twin event

If identical twins are 8% of all twins, then identical birth events are 8% of all twin birth events, so the priors are
P(A) = 8%
P(B) = 92%

Relevant Evidence
E: Elvis's twin was male

Likelihoods
P(E|A) = 1
P(E|B) = 1/2

Because identical twins are necessarily the same sex, 
but fraternal twins are equally likely to be opposite sex (or, at least, I assume so).  
Therefore:
P(A|E) = 8/54 ~ 0.15.
```
---


---

How do frequentist and Bayesian statistics compare?

* Frequentists use probability only for sampling. Bayesians uses "prior distribution" - meaning a probability distribution reflecting the state of knowledge about h before collecting any data - to model both sampling and other kinds of uncertainty.

---
