"""

  Wavesolve program main program.  Runs main routine and calls calculations 
  from functions from math and physics libraries.
  
  
  Built using Canopy Enthought IDE and frameworks.
  
  @required_packages
  bigfloat - Python wrapper for MPFR for handling arbitrarily large precision 
             floating point numbers.
  MPFR - GNU C library for multiple-precision floating-point computation.  Note,
         GMP is required for installation.
         http://www.mpfr.org
  GMP - GNU Multiple Precision library for arbitrary precision 
        arithmetic, operating on signed integers, rational numbers, and 
        floating-point numbers.
        https://gmplib.org/
  
  @author Kai Pak
  @start_date January 1, 2014
  @current_version 1.0
  
  History
  
"""


import ws_maths, ws_physics
#from bigfloat import *
from sympy import *
import timeit
from IPython.display import display

# Bits of precison that will be used throughout application
#setcontext(quadruple_precision)

def main():
    #mw = MainWindow()
    #mw.configure_traits()
    init_printing()
    start_time = timeit.default_timer()
    # print ws_physics.hfs_gamma(2,2,2)
    #print int(scipy.misc.comb(5,1))
    
    # bigmatrix = ws_maths.rand_matrix(10)
    
    
    #for row in bigmatrix:
    #    print row

    # print linalg.eig(bigmatrix)
    #L_alt = ws_maths.b_cholesky_L(bigmatrix)
    #L = pstates_maths.cholesky_L(bigmatrix)
    
    #print "\n\nDisplaying some maths.\n"
    #print x
    
    
    #print "\n\nSome Cholesky Decomposition of a matrix:\n"
    
    #for row in L_alt:
    #    print row
    
    
    test_psy = ws_physics.gen_wave_func(1)
    hamiltonian = []
    
    for term in test_psy:
        hamiltonian.append(ws_physics.hamiltonian_r(term))

    for term in hamiltonian:
        display(term)
        print term
    
    #ws_physics.quantum_state(test_psy[0], hamiltonian[0])
    
    # print test_psy.factor()
    print '\n'
    # display(test_psy)
    # display(ws_physics.hamiltonian_r(test_psy))
        
    
    
    stop_time = timeit.default_timer()
    print "\n\nTime elapsed in seconds: "
    print stop_time - start_time


if __name__ == '__main__':
    main()