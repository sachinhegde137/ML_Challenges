## Challenge
Here are the test scores of 10 students in physics
and history:
```
Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
```

When a student scores 10 in Physics, what is his 
probable score in History? Compute the answer correct
to one decimal place.

## Input format
The first line has n integers that represents x values
(independent variable). The second line has n integers
that represent y values (dependent variable). The third
line is an integer that is a test input for which the y
value has to be found.

## Explanation

To estimate the probable score in History when a 
student scores 10 in Physics, we can use the least
squares regression line. The formula for the 
regression line of *Y* on *X* (where *Y* is the 
dependent variable, History scores, and *X* is the 
independent variable, Physics scores) is:
$$Y = a + bX $$

where,
- *b* is the slope of the regression line and 
is given by:
$$b={n\sum(XY)-\sum X\sum Y\over n\sum X^2-(\sum X)^2}$$
- *a* is the y-intercept, which is calculated using:
$$a={{\sum Y\over n}-b{\sum X\over n}}$$

Once we find the regression line, we can substitute
*X* = 10 to predict the corresponding value of *Y*.

## Sample input
```
15 12 8 8 7 7 7 6 5 3
10 25 17 11 13 17 20 13 9 15
10
```