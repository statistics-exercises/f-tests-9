import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variance(self) :
        for i in range(5) : 
            tdata = np.random.normal(0,1,size=6)
            mu = sum(tdata) / len(tdata)
            var = (len(tdata) / (len(tdata)-1))*( sum(tdata*tdata) / len(tdata) - mu*mu )
            self.assertTrue( np.abs( var - sample_variance(tdata) )<1e-7, "Your code for calculating the sample variance is not correct" )
            
    def test_error_sum_of_squares(self) : 
        tvar, samples = 0, np.zeros([10,6])
        for i in range(10) : 
            samples[i,:] = np.random.normal(size=6)
            tvar = tvar + (len(samples[i,:])-1)*sample_variance( samples[i,:] )
        self.assertTrue( np.abs( tvar - error_sum_of_squares(samples))<1e-7, "Your code for calculating the error sum of squares is not correct"  )
        
    def test_common_variance(self) :
        tvar, norm, samples = 0, 0, np.zeros([10,6])
        for i in range(10) : 
            samples[i,:] = np.random.normal(size=6)
            tvar = tvar + (len(samples[i,:])-1)*sample_variance( samples[i,:] )
            norm = norm + (len(samples[i,:])-1)
        tvar = tvar / norm
        self.assertTrue( np.abs( tvar - common_variance(samples))<1e-7, "Your code for calculating the common variance is not correct"  )
