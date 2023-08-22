import unittest
import numpy as np

from cobaya.model import get_model
from cobaya.install import install
from act_dr6_lenslike import ACTDR6LensLike

info = {
    "params" : {
        'ombh2': 2.2337930e-2,
        'omch2': 1.2041740e-1,
        'tau':5.1464010e-2,
        'ns':9.6556980e-1,
        'H0':6.7175290e1,
        'As':2.1005920e-9,
        'mnu': 0.06
        },
    "theory" : {
        "camb" : { 'extra_args' : {
                    'lmax' : 4000,
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
        
