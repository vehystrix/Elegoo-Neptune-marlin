#!/usr/bin/env python

import os
from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import subprocess

PLATFORMIO_COMMAND = Path.home() / ".platformio" / "penv" / "Scripts" / "platformio.exe"

# Parse command-line arguments
parser = ArgumentParser(
    description="Build firmware for different models and temperatures."
)
## eg -DDEBUG_EEPROM_READWRITE=1 -DDEBUG_EEPROM_READWRITE_EXTRA=1
parser.add_argument(
    "--buildflags",
    type=str,
    default="",
    help="Additional build flags to pass to PlatformIO",
)
# Add command-line arguments for model, temperature, and debug status
parser.add_argument(
    "--model",
    type=str,
    choices=["PRO", "PLUS", "MAX"],
    help="Specify the model to build (PRO, PLUS, MAX)",
)
parser.add_argument(
    "--temperature",
    type=int,
    help="Specify the maximum temperature (default: 260, 300, 320, 350)",
)
parser.add_argument(
    "--debug", action="store_true", help="Enable debug EEPROM read/write"
)
parser.add_argument("--wifi", action="store_true", help="Enable WiFi support")
args = parser.parse_args()

builddir = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".pio" / "build" / "MKS_E3_V2"
)
outdir = Path.cwd() / "build"
outdir.mkdir(parents=True, exist_ok=True)

softversion_define = f' -DSOFTVERSION=\\"{date.today().strftime("%y%m%d")}\\"'

MODELS = ["PRO", "PLUS", "MAX"]


def build(model: str, temp: int, debug_eeprom: bool = False, wifi: bool = False):
    if model not in MODELS:
        raise ValueError("Unknown model")

    temp_define = ""
    tempname = ""
    if temp != 260:
        temp_define = f" -DHEATER_0_MAXTEMP={temp + 15}"
        tempname = f"MAXTEMP_{temp}_"

        if temp > 290:
            temp_define += " -DTEMP_SENSOR_0=61"
    # if
    debug_define = ""
    debug_name = ""
    if debug_eeprom:
        debug_define += " -DDEBUG_EEPROM_READWRITE=1 -DDEBUG_EEPROM_READWRITE_EXTRA=1"
        debug_name = "DEBUG_"

    wifi_define = ""
    wifi_name = ""
    if wifi:
        wifi_define = " -DN3P_WIFI=1"
        wifi_name = "WIFI_"

    subprocess.run(f"{PLATFORMIO_COMMAND} run --target clean -e MKS_E3_V2", check=False)
    build_flags = os.environ.get("PLATFORMIO_BUILD_FLAGS", "")
    os.environ["PLATFORMIO_BUILD_FLAGS"] = (
        build_flags
        + f" -DNEPTUNE_3_{model}=1"
        + temp_define
        + debug_define
        + softversion_define
        + wifi_define
        + f" {args.buildflags}"
    )
    subprocess.run(
        f"{PLATFORMIO_COMMAND} run -e MKS_E3_V2", env=os.environ, check=False
    )
    os.replace(
        builddir / "ZNP_ROBIN_NANO.bin",
        outdir / f"{model}_{tempname}{wifi_name}{debug_name}ZNP_ROBIN_NANO.bin",
    )
    os.environ["PLATFORMIO_BUILD_FLAGS"] = build_flags


# def build

if args.model:
    models = [args.model]
else:
    models = MODELS
if args.temperature:
    temperatures = [args.temperature]
else:
    temperatures = [260, 300, 320, 350]


for model in models:
    for temp in temperatures:
        build(model, temp, debug_eeprom=args.debug, wifi=args.wifi)
    # for
    # if not args.debug:
    #     build(model, 260, debug_eeprom=True)
    if not args.wifi:
        build(model, 260, debug_eeprom=False, wifi=True)
