#!/usr/bin/env python

import os
from pathlib import Path

builddir = Path(os.path.dirname(os.path.realpath(__file__))) / '.pio' / 'build' / 'MKS_E3_V2'
outdir = Path.cwd() / 'build'
outdir.mkdir(parents=True, exist_ok=True)

MODELS = ['PRO', 'PLUS', 'MAX']

def build(model: str, temp: int):
    if model not in MODELS: raise ValueError('Unknown model')

    temp_define = ''
    tempname = ''
    if temp != 260:
        temp_define = f" -DHEATER_0_MAXTEMP={temp + 15}"
        tempname = f"MAXTEMP_{temp}_"
        
        if temp > 290: temp_define += ' -DTEMP_SENSOR_0=61'
    # if

    os.environ['PLATFORMIO_BUILD_FLAGS'] = f"-DNEPTUNE_3_{model}=1" + temp_define
    os.system('platformio run -e MKS_E3_V2')
    os.replace(builddir / 'ZNP_ROBIN_NANO.bin', outdir / f"{model}_{tempname}ZNP_ROBIN_NANO.bin")
# def build

for model in MODELS:
    for temp in [260, 300, 320, 350]:
        build(model, temp)
    # for
# for
