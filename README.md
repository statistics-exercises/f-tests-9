# The error sum of squares

Some of the black points in the graph that was generated at the end of the previous task lay above the red line and some lay below this line.  The reason for this is that the black dots and the red line both indicate estimates of the sample means computed using:

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^nX_i)

where the ![](https://render.githubusercontent.com/render/math?math=X_i) are standard normal random variables.  The expectation and variance for this random variable are:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(\overline{X})=0\qquad\textrm{var}(\overline{X})=\frac{1}{n})

As you can see only the variance depends on the number of random variables that the estimate of the mean was generated from.  The expectations of the distributions from which we sampled the black dots and the red line are thus the same.  All the estimates of this quantity that we obtain by sampling are different, however, because we are computing these estimates from random numbers.

This reminder of the theory aside lets return to the question of the statistic we should use for testing if all the distributions that we have sampled from have the same expectation.  We are going to need to compute two key quantities from the multiple samples that we learned to generate in the last exercise in order to obtain this statistic so in this task and the next we are going to learn to compute these.  In this task, in particular, we are going to learn how to compute the error sum of squares (SSE).  To compute this quantity you proceed as follows:

1. compute a sample variance for each of the t individual samples using:

![](https://render.githubusercontent.com/render/math?math=S_j^2=\frac{n_j}{n_j-1}\left[\frac{1}{n_j}\sum_{i=1}^{n_j}X_i^2-\left(\frac{1}{n_j}\sum_{i=1}^{n_j}X_i\right)^2\right])

where ![](https://render.githubusercontent.com/render/math?math=n_j) is the number of data points in the jth set of samples

2. From the t sample variances that you have computed you then calculate the common variance using:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{SS_E}{\sum_{j=1}^t(n_j-1)}=\frac{\sum_{j=1}^t(n_j-1)s_j^2}{\sum_{j=1}^t(n_j-1)})

It is important to note that S here is just an expression for the common variance that we learned about last week when we were learning about hypothesis tests for doing a comparison of means with small sample sizes.  Here though it is a common variance for t different distributions as opposed to two.  

__Your task is thus to complete the functions in the cell on the left for computing the error sum of squares and the common variance for the data in the file called `mydata.dat`.__  

To understand how to complete this task let's start by looking at the data in `mydata.dat`. You will notice that each row in that file is a set of distinct results.  In other words, all the numbers in the first rows are samples from one distribution, while all the numbers in the second row are samples from a second, possibly different distribution.  The third row also then contains samples from a distribution that is different from the one that was sampled in the first and second rows and so on.  There are 10 samples in total and each is a set of 6 random variables.

The data from mydata.dat has been loaded into a NumPy array called `allsamples`.  If you add the command:

````
print( allsamples )
````

at the end of the code and run you should thus see that all the data from the file is printed out in the terminal window.  If you look at the end of all the numbers that are printed you will see that the printout ends with  ] ] as opposed to simply ] we have seen when we printed NumPy arrays in the past.  The reason for this is we are using a two-dimensional NumPy array here.  We thus need two indices in order to print a specific element of this array.  To see what I mean try replacing the print statement you just wrote with the following one:

````
print( allsamples[1,2] )    
````

If you now run the command and look at the output you should see that the single number that is output by this command is the same as the number in the second column and the third row of `mydata.dat`.  You can experiment with commands such as the one above in order to better understand how to print specific numbers from mydata.dat.  Once you are happy with this idea replace the print statement with:

````
print( allsamples[1,:] )   
````

You should now see that a 1D NumPy array is output.  Furthermore, the numbers in this 1D NumPy array should be the same as the numbers in the second row of `mydata.dat`. Now notice that print is just another function and that if you write something similar to the above in any other function a 1D NumPy array will be passed to the function.

With this understanding of 2D NumPy arrays in place, you are in a position to complete the task.  You essentially need to complete three functions:

1. `sample_variance` - takes a 1D NumPy array called `data` as input.  The function should return the sample variance computed from the data in `data`.
2. `error_sum_of_squares` - takes a 2D NumPy array called `samples` as input.  The function should call `sample_variance` to compute the sample variance for each row of data in `samples`.  The function should then use the definitions above to compute and return the error sum of squares from these individual sample variances.
2. `common_variance` - takes a 2D NumPy array called `samples` as input.  The function should call `error_sum_of_squares` to compute the error sum of squares.  The common variance should then be computed and returned using the definitions given above.

Once these functions are complete and the code is run error sum of squares and the common variance for the data in allsamples will be output.
