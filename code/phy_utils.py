import os
from pathlib import Path
from shutil import copy2, copytree


def copy_most_files(
    source_path: Path,
    destination_path: Path,
    symlink_file_types: list[str]
):
    """Recursively copy files from source_path to destination_path -- but make symlinks for selected file types."""

    logging.info(f"Copy {source_path} to {destination_path} using symlinks for {symlink_file_types})

    def copy_most(src, dst, *, follow_symlinks=True):
        src_path = Path(src)
        if src_path.suffix in symlink_file_types:
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
    # Currently root is the only user configured for Code Ocean Ubuntu workstation.
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

    params_py = Path(phy_path, "params.py")
    print(f"Running Phy for {params_py}")
    template_gui(params_py)


def copy_changed_files(
    phy_path: Path,
    start_time: float,
    results_path: Path
):
    """Find files within phy_path that have changed since start_time and copy them into results_path."""

    print(f"Looking for Phy files within: {phy_path}")
    print(f"Looking for files that changed since {start_time} (epoch seconds)")
    changed_files = [f for f in phy_path.iterdir() if f.is_file() and f.stat().st_mtime > start_time]
    print(f"Found {len(changed_files)} changed files.")

    for f in changed_files:
        copy(f, destination)
        print(f"Copied {f} to {destination}")
