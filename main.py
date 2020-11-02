import numpy as np 

def sample_variance( data ) : 
  # This should return the sample variance calculated from the 
  # 1D NumPy array called data that is passed to the function.
  # You need to replace the return statement
  return 1 
  
def error_sum_of_squares( samples ) : 
  # This functions takes a 2D numpy array in input.  You add code to make it 
  # compute and return the error sum of squares.
  # You need to replace the return statement
  return 1

def common_variance( samples ) : 
  # This functions takes a 2D numpy array in input.  It should return
  # common variance.
  # You need to replace the return statement.
  return 1


# You should not need to modify any of the code from here
allsamples = np.loadtxt("mydata.dat")
print("The error sum of squares for the generated data is", error_sum_of_squares( allsamples ) )
print("The common variance for the generated data is", common_variance( allsamples ) )
