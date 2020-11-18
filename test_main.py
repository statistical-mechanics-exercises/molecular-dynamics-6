import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_var_vel(self) :
        nsamples = 500
        nresamples = 20
        for T in [0.5,1.0,1.5,2.0] : 
            vartot, vartot2 = 0, 0
            for i in range(nresamples) : 
                mean, mean2 = 0, 0 
                for j in range(nsamples) : 
                    vel = gen_vel(T)
                    mean = mean + vel
                    mean2 = mean2 + vel*vel
                mean = mean / nsamples 
                var = (nsamples / (nsamples-1) )*( mean2/nsamples - mean*mean )
                vartot = vartot + var
                vartot2 = vartot2 + var*var
    
            vartot = vartot / nresamples 
            fvar = (nresamples/(nresamples-1) )*( vartot2/nresamples - vartot*vartot )
            bar = np.sqrt( fvar / nresamples )*st.norm.ppf(0.95) 
            self.assertTrue( np.abs( vartot - T )<bar, "the variance for the distribution of velocities appears to be incorrect" )
            
    def test_mean_vel(self) : 
        nsamples = 1000
        for T in [0.5,1.0,1.5,2.0] : 
            bar = np.sqrt( T / nsamples )*st.norm.ppf(0.95)
            mean = 0 
            for i in range(nsamples) : mean = mean + gen_vel(T)
            self.assertTrue( np.abs( mean / nsamples )<bar, "the mean velocity appears to  be incorrect" )
