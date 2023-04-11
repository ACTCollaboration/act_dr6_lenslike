# ACT DR6 Lensing Likelihood

This repository contains likelihood software for the ACT DR6 CMB lensing analysis. If you use this software and/or the associated data, please cite both of the following papers:
1. Madhavacheril, Qu, Sherwin, MacCrann, Li et al ACT Collaboration (2023)
2. Qu, Sherwin, Madhavacheril, Han, Crowley et al ACT Collaboration (2023)


## Step 1: clone this repository

## Step 2: copy data

The data is available to ACT group members here:
- ``niagara:/gpfs/fs0/project/r/rbond/msyriac/lensing/dr6/likelihood/data``
- ``nersc:/global/project/projectdirs/act/data/lensing/dr6/likelihood/data``

Copy such that the `data` directory is inside the directory that has `__init__.py` in the cloned repositry. Only then should you proceed with the next step.

## Step 3: install Python package

Install with

    pip install -e . --user
    
## Step 4: use in Python codes

### Generic Python likelihood

```
import act_dr6_lenslike as alike

variant = 'act_baseline'
lens_only = False

# Do this once
data_dict = alike.load_data(variant,lens_only=lens_only)

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
- `halofit`:`mead2016`

## Planned updates

- Cobaya YAML files
- CosmoSIS wrapper


