import unittest
import numpy as np

from cobaya.model import get_model
from cobaya.install import install
from act_dr6_lenslike import ACTDR6LensLike

info = {
    "params" : {
        'ombh2': 0.02219218,
        'omch2': 0.1203058,
        'tau': 0.06574325,
        'ns': 0.9625356,
        'H0': 67.02393,
        'As': 2.15086031154146e-9,
        'omnuh2': 0.00064
        },
    "theory" : {
        "camb" : { 'extra_args' : {
                    'lmax' : 10000,
                    'lens_margin' : 1250,
                    'lens_potential_accuracy' : 4,
                    'AccuracyBoost' : 1,
                    'lSampleBoost' : 1,
                    'lAccuracyBoost' : 1,
                    'halofit_version' : 'mead2016'
                    }
            }
        }
}

# these parameters are close to those in https://mapsims.readthedocs.io/en/latest/camb.html
# BUT result in more chisq failures
# info = {
#     "params" : {
#         'ombh2': 0.02219218,
#         'omch2': 0.1203058,
#         'ns': 0.9625356,
#         'H0': 67.02393,
#         'As': 2.15086031154146e-9,
#         'omnuh2': 0.00064,
#         'omk': 0,
#         },
#     "theory" : {
#         "camb" : { 'extra_args' : {
#                     'AccuracyBoost' : 3,
#                     'lSampleBoost' : 1,
#                     'lAccuracyBoost' : 3,
#                     'Accuracy.LensingBoost': 3,
#                     'nu_mass_eigenstates': 1,
#                     'num_nu_massive': 1,
#                     'MassiveNuMethod': 1,
#                     'nonlinear': 3,
#                     'max_l': 10000,
#                     'max_eta_k':  20000.00000000000,
#                     'DoLensing': True,
#                     'share_delta_neff': True,
#                     'nu_mass_fractions': [1.0],
#                     'TCMB': 2.7255,
#                     'num_nu_massless': 2.046,
#                     'Alens': 1.00000000000000,
#                     'Reion.helium_delta_redshift': 0.5,
#                     'Reion.helium_redshiftstart': 5.0,
#                     'Reion.use_optical_depth': True,
#                     'Reion.optical_depth': 0.6574325E-01,
#                     'Transfer.accurate_massive_neutrinos': True,
#                     'NonLinearModel.halofit_version' : 'mead2016'
#                     }
#             }
#         }
# }

class ACTLikeTest(unittest.TestCase):

    def initialize(self):
        install({"likelihood": {"act_dr6_lenslike.ACTDR6LensLike": None}})

    def generic_call(self,variant,lens_only,exp_chisq=None):

        info['likelihood'] = {'ACTDR6LensLike' : {'external' : ACTDR6LensLike,
                                                  'variant' : variant,
                                                  'lens_only' : lens_only}}

        model = get_model(info)
        loglikes, derived = model.loglikes()

        chisq = -2 * loglikes[0]

        self.assertAlmostEqual(chisq,  exp_chisq, 1)

    def test_act_baseline_lensonly(self):
        self.generic_call('act_baseline',True,14.06)
    def test_act_baseline(self):
        self.generic_call('act_baseline',False,14.71)
    def test_actplanck_baseline_lensonly(self):
        self.generic_call('actplanck_baseline',True,21.07)
    def test_actplanck_baseline(self):
        self.generic_call('actplanck_baseline',False,21.97)
    def test_act_extended_lensonly(self):
        self.generic_call('act_extended',True,17.66)
    def test_act_extended(self):
        self.generic_call('act_extended',False,17.26)
    def test_actplanck_extended_lensonly(self):
        self.generic_call('actplanck_extended',True,24.4)
    def test_actplanck_extended(self):
        self.generic_call('actplanck_extended',False,24.26)
    def test_act_polonly_lensonly(self):
        self.generic_call('act_polonly',True,309.71)
    def test_act_cibdeproj_lensonly(self):
        self.generic_call('act_cibdeproj',True,15.16)
    def test_act_cinpaint_lensonly(self):
        self.generic_call('act_cinpaint',True,15.94)

if __name__ == '__main__':
    ACTLikeTest().test_act_baseline_lensonly()
    ACTLikeTest().test_act_baseline()
    ACTLikeTest().test_actplanck_baseline_lensonly()
    ACTLikeTest().test_actplanck_baseline()
    ACTLikeTest().test_act_extended_lensonly()
    ACTLikeTest().test_act_extended()
    ACTLikeTest().test_actplanck_extended_lensonly()
    ACTLikeTest().test_actplanck_extended()
    ACTLikeTest().test_act_polonly_lensonly()
    ACTLikeTest().test_act_cibdeproj_lensonly()
    ACTLikeTest().test_act_cinpaint_lensonly()
        
