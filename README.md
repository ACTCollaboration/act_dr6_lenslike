# ACT DR6 Lensing Likelihood
[![PyPI Badge](https://img.shields.io/pypi/v/act_dr6_lenslike?label=PyPI&logo=pypi)](https://pypi.org/project/act_dr6_lenslike/)
[![CI Badge](https://github.com/ACTCollaboration/act_dr6_lenslike/actions/workflows/testing.yml/badge.svg)](https://github.com/ACTCollaboration/act_dr6_lenslike/actions)

This repository contains likelihood software for the ACT DR6 CMB lensing analysis. If you use this software and/or the associated data, please cite both of the following papers:
- [Madhavacheril, Qu, Sherwin, MacCrann, Li et al ACT Collaboration (2023), arxiv:2304.05203](https://arxiv.org/abs/2304.05203)
- [Qu, Sherwin, Madhavacheril, Han, Crowley et al ACT Collaboration (2023), arxiv:2304.05202](https://arxiv.org/abs/2304.05202)

In addition, if you use the ACT+Planck lensing combination variant from the likelihood, please also cite:
- [Carron, Mirmelstein, Lewis (2022), arxiv:2206.07773, JCAP09(2022)039](https://arxiv.org/abs/2206.07773)

## Chains

A pre-release version of the chains from Madhavacheril et al are available [here](https://portal.nersc.gov/project/act/act_dr6_lensing/chains/). Please make sure to read the README file.

## Step 1: Install
### Option 1: Install from PyPI
You can install the likelihood directly with:

    pip install act_dr6_lenslike

### Option 2: Install from Github
If you wish to be able to make changes to the likelihood for development, first clone this repository. Then install with symbolic links:

    pip install -e . --user

Tests can be run using 

    python setup.py test

## Step 2: download and unpack data

This can be performed automatically with the supplied `get-act-data.sh` script. Otherwise follow the steps below.

Download the likelihood data tarball for ACT DR6 lensing from [NASA's LAMBDA archive](https://lambda.gsfc.nasa.gov/product/act/actadv_prod_table.html).

Extract the tarball into the `act_dr6_lenslike/data/` directory in the cloned repository such the directory `v1.2` is directly inside it. Only then should you proceed with the next steps.
    
## Step 3: use in Python codes

### Generic Python likelihood

```
import act_dr6_lenslike as alike

variant = 'act_baseline'
lens_only = False # use True if not combining with any primary CMB data
like_corrections = True # should be False if lens_only is True

# Do this once
data_dict = alike.load_data(variant,lens_only=lens_only,like_corrections=like_corrections)
# This dict will now have entries like `data_binned_clkk` (binned data vector), `cov`
# (covariance matrix) and `binmat_act` (binning matrix to be applied to a theory
# curve starting at ell=0).

# Get cl_kk, cl_tt, cl_ee, cl_te, cl_bb predictions from your Boltzmann code.
# These are the CMB lensing convergence spectra (not potential or deflection)
# as well as the TT, EE, TE, BB CMB spectra (needed for likelihood corrections)
# in uK^2 units. All of these are C_ell (not D_ell), no ell or 2pi factors.
# Then call
lnlike=alike.generic_lnlike(data_dict,ell_kk,cl_kk,ell_cmb,cl_tt,cl_ee,cl_te,cl_bb)
```

### Cobaya likelihood

Your Cobaya YAML or dictionary should have an entry of this form

```
likelihood:
    act_dr6_lenslike.ACTDR6LensLike:
        lens_only: False
        stop_at_error: True
        lmax: 4000
        variant: act_baseline
```

No other parameters need to be set. (e.g. do not manually set `like_corrections` or `no_like_corrections` here).
An example is provided in `ACTDR6LensLike-example.yaml`

### Important parameters

- `variant` should be
    - `act_baseline` for the ACT-only lensing power spectrum with the baseline multipole range
    - `act_extended` for the ACT-only lensing power spectrum with the extended multipole range (L<1250)
    - `actplanck_baseline` for the ACT+Planck lensing power spectrum with the baseline multipole range
    - `actplanck_extended` for the ACT+Planck lensing power spectrum with the extended multipole range (L<1250)
- `lens_only` should be
    - False when combining with any primary CMB measurement
    - True when not combining with any primary CMB measurement

### Recommended theory accuracy

For CAMB calls, we recommend the following (or higher accuracy):
- `lmax`: 4000
- `lens_margin`:1250
- `lens_potential_accuracy`: 4
- `AccuracyBoost`:1
- `lSampleBoost`:1
- `lAccuracyBoost`:1
- `halofit_version`:`mead2016`
