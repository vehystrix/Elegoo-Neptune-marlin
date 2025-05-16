#!/usr/bin/env python

import os
from datetime import date
from pathlib import Path
from argparse import ArgumentParser

# Parse command-line arguments
parser = ArgumentParser(description="Build firmware for different models and temperatures.")
## eg -DDEBUG_EEPROM_READWRITE=1 -DDEBUG_EEPROM_READWRITE_EXTRA=1
parser.add_argument('--buildflags', type=str, default='', help='Additional build flags to pass to PlatformIO')
args = parser.parse_args()

builddir = Path(os.path.dirname(os.path.realpath(__file__))) / '.pio' / 'build' / 'MKS_E3_V2'
outdir = Path.cwd() / 'build'
outdir.mkdir(parents=True, exist_ok=True)

softversion_define = f" -DSOFTVERSION=\\\"{date.today().strftime('%y%m%d')}\\\""

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

    os.system('platformio run --target clean -e MKS_E3_V2')
    build_flags = os.environ.get('PLATFORMIO_BUILD_FLAGS', '')
    os.environ['PLATFORMIO_BUILD_FLAGS'] = build_flags + f" -DNEPTUNE_3_{model}=1" + temp_define + softversion_define + f" {args.buildflags}"
    os.system('platformio run -e MKS_E3_V2')
    os.replace(builddir / 'ZNP_ROBIN_NANO.bin', outdir / f"{model}_{tempname}ZNP_ROBIN_NANO.bin")
    os.environ['PLATFORMIO_BUILD_FLAGS'] = build_flags
# def build


for model in MODELS:
    for temp in [260, 300, 320, 350]:
        build(model, temp)
    # for
# for
