# Basic Plots

We look at some of the ways R can display information graphically.

## Strip Charts

A strip chart plots the data in order along a line with each data point represented as a box. 

```
>  w1 <- read.csv(file="w1.dat",sep=",",head=TRUE)
> names(w1)
[1] "vals"
>  tree <- read.csv(file="trees91.csv",sep=",",head=TRUE)
> names(tree)
 [1] "C"      "N"      "CHBR"   "REP"    "LFBM"   "STBM"   "RTBM"   "LFNCC"
 [9] "STNCC"  "RTNCC"  "LFBCC"  "STBCC"  "RTBCC"  "LFCACC" "STCACC" "RTCACC"
[17] "LFKCC"  "STKCC"  "RTKCC"  "LFMGCC" "STMGCC" "RTMGCC" "LFPCC"  "STPCC"
[25] "RTPCC"  "LFSCC"  "STSCC"  "RTSCC"
```

```
> help(stripchart)
> stripchart(w1$vals)
```

## Histograms

Plots the frequencies that data appears within certain ranges. 

```
> hist(w1$vals)
> hist(w1$vals,main="Distribution of w1",xlab="w1")
```

## Boxplots

Boxplots are useful in that theyu provide a graphical view of the median, quartiles, max, and min of a data set. 

```
> boxplot(w1$vals)
```

## Scatter Plots

A scatter plot is useful because it provides a graphical view of the relationship between two sets of numbers. 

```
> plot(tree$STBM, tree$LFBM)
```