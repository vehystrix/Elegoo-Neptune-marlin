#!/usr/bin/env python3
"""
Marlin Build Helper Script
Automates PlatformIO builds for Marlin firmware.
"""

import subprocess
import sys
from pathlib import Path

# Configuration
PLATFORMIO_PATH = Path.home() / ".platformio" / "penv" / "Scripts" / "platformio.exe"
WORKSPACE_ROOT = Path(__file__).parent
DEFAULT_ENV = "MKS_E3_V2"


def run_build(env_name: str | None = None, verbose: bool = False) -> int:
    """
    Run PlatformIO build for the specified environment.

    Args:
        env_name: PlatformIO environment name (default: MKS_E3_V2)
        verbose: Enable verbose output

    Returns:
        0 on success, 1 on failure
    """
    env = env_name or DEFAULT_ENV
    workspace = str(WORKSPACE_ROOT)

    # Verify PlatformIO exists
    if not PLATFORMIO_PATH.exists():
        print(f"Error: PlatformIO not found at {PLATFORMIO_PATH}")
        return 1

    # Build command
    cmd = [PLATFORMIO_PATH, "run", "-e", env]
    if verbose:
        cmd.insert(2, "--verbose")

    print(f"Building Marlin for environment: {env}")
    print(f"Workspace: {workspace}")
    print("-" * 60)

    # Run build
    result = subprocess.run(
        cmd, cwd=workspace, capture_output=True, text=True, check=False
    )

    # Print output
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    # Check result
    if result.returncode == 0:
        print("-" * 60)
        print(f"✓ Build successful for {env}")

        # Check for output file
        output_dir = WORKSPACE_ROOT / ".pio" / "build" / env
        firmware_elf = output_dir / "firmware.elf"
        if firmware_elf.exists():
            print(f"✓ Firmware ELF: {firmware_elf}")

        return 0
    else:
        print("-" * 60)
        print(f"✗ Build failed for {env}")
        return 1


def list_environments() -> None:
    """List available PlatformIO environments."""
    if not PLATFORMIO_PATH.exists():
        print(f"Error: PlatformIO not found at {PLATFORMIO_PATH}")
        return

    cmd = [PLATFORMIO_PATH, "environment", "--list"]
    result = subprocess.run(
        cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True, check=False
    )
    print(result.stdout)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build Marlin firmware")
    parser.add_argument("-e", "--env", help="PlatformIO environment name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument(
        "--list-envs", action="store_true", help="List available environments"
    )

    args = parser.parse_args()

    if args.list_envs:
        list_environments()
    else:
        sys.exit(run_build(args.env, args.verbose))
