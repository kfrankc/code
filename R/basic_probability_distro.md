# Basic Probability Distributions

## The Normal Distribution

**dnorm**: given a set of values, it returns the height of the probability distro at each point. 

```
> dnorm(0)
[1] 0.3989423
> dnorm(0)*sqrt(2*pi)
[1] 1
> dnorm(0,mean=4)
[1] 0.0001338302
> dnorm(0,mean=4,sd=10)
[1] 0.03682701
>v <- c(0,1,2)
> dnorm(v)
[1] 0.39894228 0.24197072 0.05399097
> x <- seq(-20,20,by=.1)
> y <- dnorm(x)
> plot(x,y)
> y <- dnorm(x,mean=2.5,sd=0.1)
> plot(x,y)
```

**pnorm**: given a number or a list it computes the probability that a normally distributed random number will be less than that number. 

```
> pnorm(0)
[1] 0.5
> pnorm(1)
[1] 0.8413447
> pnorm(0,mean=2)
[1] 0.02275013
> pnorm(0,mean=2,sd=3)
[1] 0.2524925
> v <- c(0,1,2)
> pnorm(v)
[1] 0.5000000 0.8413447 0.9772499
> x <- seq(-20,20,by=.1)
> y <- pnorm(x)
> plot(x,y)
> y <- pnorm(x,mean=3,sd=4)
> plot(x,y)
```

**qnorm**: the inverse of pnorm. You give it a probability, and it returns the number whose cumulative distribution matches the probability. 

```
> qnorm(0.5)
[1] 0
> qnorm(0.5,mean=1)
[1] 1
> qnorm(0.5,mean=1,sd=2)
[1] 1
> qnorm(0.5,mean=2,sd=2)
[1] 2
> qnorm(0.5,mean=2,sd=4)
[1] 2
> qnorm(0.25,mean=2,sd=2)
[1] 0.6510205
> qnorm(0.333)
[1] -0.4316442
> qnorm(0.333,sd=3)
[1] -1.294933
> qnorm(0.75,mean=5,sd=2)
[1] 6.34898
> v = c(0.1,0.3,0.75)
> qnorm(v)
[1] -1.2815516 -0.5244005  0.6744898
> x <- seq(0,1,by=.05)
> y <- qnorm(x)
> plot(x,y)
> y <- qnorm(x,mean=3,sd=2)
> plot(x,y)
> y <- qnorm(x,mean=3,sd=0.1)
> plot(x,y)
```

**rnorm**: generate random numbers whose distribution is normal. Give it the no. of random numbers that you want, and it has optional arguments to specify the mean and standard deviation.

```
> rnorm(4)
[1]  1.2387271 -0.2323259 -1.2003081 -1.6718483
> rnorm(4,mean=3)
[1] 2.633080 3.617486 2.038861 2.601933
> rnorm(4,mean=3,sd=3)
[1] 4.580556 2.974903 4.756097 6.395894
> rnorm(4,mean=3,sd=3)
[1]  3.000852  3.714180 10.032021  3.295667
> y <- rnorm(200)
> hist(y)
> y <- rnorm(200,mean=-2)
> hist(y)
> y <- rnorm(200,mean=-2,sd=4)
> hist(y)
> qqnorm(y)
> qqline(y)
```

## The Binomial Distribution

**dbinom**: Distribution function

**pbinom**: Cumulative probability distribution function

**qbinom**: Inverse cumulative probability distribution function

**rbinom**: Random numebrs generated according to binomial distro

The Chi-Squared Distribution follows similiar conventions.