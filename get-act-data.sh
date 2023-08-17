#!/usr/bin/env bash

# script from Joe Zuntz

if [ -d act_dr6_lenslike/data/v1.1 ]
then
    echo ACT DR6 Lensing data already downloaded
elif ! command -v wget &> /dev/null
then
    echo wget not installed. Please obtain it \(e.g. conda install wget\) to download the data.
else
    mkdir -p act_dr6_lenslike/data
    pushd act_dr6_lenslike/data
    wget https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/likelihood/data/ACT_dr6_likelihood_v1.1.tgz
    tar -zxvf ACT_dr6_likelihood_v1.1.tgz
    rm ACT_dr6_likelihood_v1.1.tgz
    popd
fi