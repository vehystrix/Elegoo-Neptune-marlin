---
name: marlin-build
description: "Build Marlin 3D printer firmware using PlatformIO. Use when: compiling Marlin firmware, building for a specific board, running platformio build, verifying compilation after code changes, checking build success/failure, or any request involving 'build', 'compile', 'pio', 'platformio', 'firmware', or 'flash' in a Marlin project."
---

# Marlin Firmware Build Skill

## Overview

This skill automates building Marlin 3D printer firmware using PlatformIO. It handles environment detection, build execution, and result reporting.

**Use this skill whenever the user asks to:**
- Build or compile the Marlin firmware
- Verify compilation after code changes
- Check if the build succeeds
- Flash firmware to a board
- Run PlatformIO builds (`pio run`, `platformio run`)
- Test builds for a specific board
- Any request involving build/compile/flash in this project

**Project context:** This is a Marlin 3D printer firmware repository. The workspace root contains `platformio.ini` and `Marlin/` directory with the firmware source code.

## Prerequisites

- PlatformIO installed in virtual environment at `%USERPROFILE%\.platformio\penv\Scripts\platformio.exe`
- Workspace root: Current project directory (where `platformio.ini` is located)
- Default environment: `MKS_E3_V2`

## Build Process

### 1. Verify Environment

Check if PlatformIO is available:
```powershell
Test-Path "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe"
```

### 2. Run Build

Execute the build command from the workspace root:
```powershell
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run -e MKS_E3_V2
```

### 3. Check Results

**Success indicators:**
- Output contains `================================================================ [SUCCESS] Took X.XX seconds ===============================================================`
- `firmware.elf` OR `ZNP_ROBIN_NANO.els` exists in `.pio\build\MKS_E3_V2\`
- RAM and Flash usage percentages are displayed

**Failure indicators:**
- `error:` messages in output
- Exit code non-zero
- No `.elf` generated


### Build default environment
```powershell
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run
```

### Build with verbose output
```powershell
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run -v
```

### Clean build artifacts
```powershell
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run --target clean
```

## Quality Checks

After successful build:
1. Verify RAM usage < 80%
2. Verify Flash usage < 95%
3. Check for any `error:` messages (warnings are acceptable)
4. Confirm output file exists: `.pio\build\MKS_E3_V2\firmware.bin` OR `.pio\build\MKS_E3_V2\ZNP_ROBIN_NANO.bin`

## Troubleshooting

### PlatformIO Not Found
```powershell
# Check virtual environment
Get-ChildItem "$env:USERPROFILE\.platformio\penv\Scripts" -Filter "platformio*"
```

### Build Fails with Missing Dependencies
```powershell
# Clear PlatformIO cache and rebuild
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run --target clean
& "$env:USERPROFILE\.platformio\penv\Scripts\platformio.exe" run
```

## Example Prompts

- "Build the Marlin firmware"
- "Compile for MKS_E3_V2"
- "Verify the build after changes"
- "Run platformio build"
- "Check if the build compiles"
- "Clean and rebuild"

## Related Files

- `platformio.ini` — PlatformIO configuration
- `Marlin/config.ini` — Marlin build configuration
- `buildroot/share/PlatformIO/boards/` — Board definitions
- `.pio/build/` — Build output directory
