import act_dr6_lenslike as alike
import numpy as np
import matplotlib.pyplot as plt

variant = 'act_baseline'
lens_only = False

cosmosis_data = False

# Do this once
data_dict = alike.load_data(variant,lens_only=lens_only)

# Get cl_kk, cl_tt, cl_ee, cl_te, cl_bb predictions
if cosmosis_data:
    data_dir = 'act_dr6_lenslike/data/v1.1/test_cls/'
    ell=  np.loadtxt(data_dir+'ell.txt', unpack=True)
    cl_pp = np.loadtxt(data_dir+'pp.txt', unpack=True)
    cl_tt = np.loadtxt(data_dir+'tt.txt', unpack=True)
    cl_ee = np.loadtxt(data_dir+'ee.txt',unpack=True)
    cl_te = np.loadtxt(data_dir+'te.txt', unpack=True)
    cl_bb = np.loadtxt(data_dir+'bb.txt',unpack=True)
    cl_kk = (ell*(ell+1))**2*cl_pp/4 # converting from cl_phiphi to cl_kk

    prefac = 2*np.pi/(ell**2)
    cl_bb = cl_bb*prefac
    cl_tt = cl_tt*prefac
    cl_ee = cl_ee*prefac
    cl_te = cl_te*prefac
    cl_kk = cl_kk*prefac

else:
    data_dir = 'act_dr6_lenslike/data/v1.1/'
    ell, cl_tt, cl_ee, cl_bb, cl_te, cl_pp, cl_tp, cl_ep= np.loadtxt(data_dir+'test_lenspotentialCls.dat', unpack=True)
    prefac = 2*np.pi/(ell**2)
    cl_kk=cl_pp/4
    cl_bb = cl_bb*prefac
    cl_tt = cl_tt*prefac
    cl_ee = cl_ee*prefac
    cl_te = cl_te*prefac
    cl_kk = cl_kk*2*np.pi
    
# Then call
ell_kk = ell
ell_cmb=ell

lnlike=alike.generic_lnlike(data_dict,ell_kk,cl_kk,ell_cmb,cl_tt,cl_ee,cl_te,cl_bb,trim_lmax = 2998)

print(f" The value obtained is chi^2 = -2lnlike = {-2*lnlike}, the expected value is 13.9896")
