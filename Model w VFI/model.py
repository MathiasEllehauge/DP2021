# Import package
import numpy as np
import tools

def setup():
    class par: pass

    # Demograhpics
    par.age_min = 25 # Only relevant for figures
    par.T = 90-par.age_min
    par.Tr = 65-par.age_min # Retirement age, no retirement if TR=T
    
    # Preferences
    par.rho = 2
    par.beta = 0.96

    # Income parameters
    par.G = 1.03

    par.sigma_xi = 0.1
    par.sigma_psi = 0.1

    par.low_p = 0.005 # Called pi in slides
    par.low_val = 0 # Called mu in slides.
    
    # Saving and borrowing
    par.R = 1.04
    par.kappa = 0.0

    # Numerical integration and grids
    par.a_max = 20 # maximum point in grid for a
    par.a_phi = 1.1 # curvature parameters

    par.Nxi  = 8 # number of quadrature points for xi
    par.Npsi = 8 # number of quadrature points for psi
    par.Na = 500 # number of points in grid for a

    # 6. simulation
    par.sim_mini = 2.5 # initial m in simulation
    par.simN = 500000 # number of persons in simulation
    par.simT = 100 # number of periods in simulation

    return par


    