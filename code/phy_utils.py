import os
import logging
from pathlib import Path
from shutil import copy2, copytree

from phy.apps.template import template_gui


def copy_most_files(
    source_path: Path,
    destination_path: Path,
    symlink_file_types: list[str]
):
    """Recursively copy files from source_path to destination_path -- but make symlinks for selected file types."""

    logging.info(f"Copy {source_path} to {destination_path} using symlinks for {symlink_file_types}")

    def copy_most(src, dst, *, follow_symlinks=True):
        src_path = Path(src)
        dst_path = Path(dst)
        if src_path.suffix in symlink_file_types and not dst_path.exists():
            os.symlink(src, dst)
            logging.info(f"Created symlink: {src} -> {dst}")
        else:
            copy2(src, dst, follow_symlinks=follow_symlinks)

    copytree(source_path, destination_path, dirs_exist_ok=True, copy_function=copy_most)


def run_phy(
    phy_path: Path
):
    """Run phy itself, similar to command line: phy template-gui params.py"""
    # Disable Chromium "sandboxing" to allow running Phy as root.
    # We don't want to run as root!
    # But misconfigured Docker containers or Code Ocean capsules might force us to be root.
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

    params_py = Path(phy_path, "params.py")
    logging.info(f"Running Phy for {params_py}")
    template_gui(params_py)


def copy_changed_files(
    phy_path: Path,
    start_time: float,
    results_path: Path
):
    """Find files within phy_path that have changed since start_time and copy them into results_path."""

    logging.info(f"Looking for Phy files within: {phy_path}")
    logging.info(f"Looking for files that changed since {start_time} (epoch seconds)")
    changed_files = [f for f in phy_path.iterdir() if f.is_file() and f.stat().st_mtime > start_time]
    logging.info(f"Found {len(changed_files)} changed files.")

    results_path.mkdir(parents=True, exist_ok=True)
    for f in changed_files:
        copy2(f, results_path)
        logging.info(f"Copied {f} to {results_path}")
