# Basic Data Types

### Variable Types

**Numbers**

```
a <- 3
b <- sqrt(a*a+3)
ls() # get list of variables defined in particular session
a <- c(1,2,3,4,5) # create a list (called a 'vector')
typeof(a) # determines data type used for a variable
a <- numeric(10) # initializes a list of 10 zeroes.
```

_Note_: In vectors, access first entry by doing `a[1]`. `a[0]` indicates how the data is stored.

**Strings**

```
a <- "hello"
a = character(10) # this will create 10 empty strings in a vector
```

**Factors**

```
summary(tree$CHBR)
tree$C
summary(tree$C)
tree$C <- factor(tree$C) # this will change the datatype, so now if you run summary, it will show the numbers and the freq. in which they appear
```

**Data Frames**

```
a <- c(1, 2, 3, 4)
b <- c(2, 4, 6, 8)
levels <- factor(c("A", "B", "A", "B"))
bubba <- data.frame(first=a, second=b, f=levels)
bubba$first # this will bring out "1 2 3 4"
bubba$f # this will print out A B A B
```

**Logical**

```
a = TRUE
typeof(a) # this will show "logical"
b = FALSE
typeof(b) # this will show "logical"
```

Standard Logical Operators:

```
<
>
<=, >=
==
!=
|, ||
!
&, &&
xor(a, b)
```

**Tables**

What are _One Way_ Tables?

```
a <- factor(c("A", "A", "B", "A", "B", "B", "C", "A", "C"))
results <- table(a)
```

What are _Two Way_ Tables?

If you want to add rows to your table just add another vector to the argument of the table command.