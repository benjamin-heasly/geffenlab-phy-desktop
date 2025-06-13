import sys
from argparse import ArgumentParser
from typing import Optional, Sequence, Any
import logging
from pathlib import Path
import time

from phy_utils import copy_most_files, run_phy, copy_changed_files


def set_up_logging():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


def capsule_main(
    data_path: Path,
    results_path: Path,
    phy_pattern: str,
    temp_path: Path,
    symlink_file_types: list[str]
):
    # Locate Phy files.
    logging.info(f"Looking for input data: {data_path}")
    logging.info(f"Looking for Phy dir matching: {phy_pattern})
    phy_path = list(data_path.glob(phy_pattern))[0]
    logging.info(f"Found Phy dir: {phy_path})

    # Copy Phy files to a writable location.
    # Use symlinks for large binary files.
    phy_temp_path = Path(temp_path, phy_path.relative_to(data_path))
    logging.info(f"Copying Phy dir: {phy_temp_path})
    copy_most_files(phy_path, phy_temp_path, symlink_file_types)

    # Run Phy.
    # Note the starting time, so we can find files that changed during curation.
    start_time = time.time()
    run_phy(phy_temp_path)

    # Copy files that changed during curation to a results dir.
    copy_changed_files(phy_temp_path, start_time, results_path)


def main(argv: Optional[Sequence[str]] = None) -> int:
    set_up_logging()

    parser = ArgumentParser(description="Launch Phy and copy files that changed during curation.")

    parser.add_argument(
        "--data-root", "-d",
        type=str,
        help="Where to find and read input data files. (default: %(default)s)",
        default="/data"
    )
    parser.add_argument(
        "--results-root", "-r",
        type=str,
        help="Where to write output result files. (default: %(default)s)",
        default="/results"
    )
    parser.add_argument(
        "--phy-pattern", "-p",
        type=str,
        help="Glob pattern to locate a phy/ dir (that contains params.py) within DATA_ROOT. (default: %(default)s)",
        default="ecephys*/phy/block0_imec0.ap_recording1"
    )
    parser.add_argument(
        "--temp-root", "-t",
        type=str,
        help="Where to write temporary, writable copies of phy files found within DATA_ROOT. (default: %(default)s)",
        default="/tmp"
    )
    parser.add_argument(
        "--symlink_file_types", "-s",
        type=str,
        nargs="*",
        help="List of file types to symlink, instead of copy, when copying read-only files out of DATA_ROOT. (default: %(default)s)",
        default=['.bin', '.dat']
    )

    cli_args = parser.parse_args(argv)
    data_path = Path(cli_args.data_root)
    results_path = Path(cli_args.results_root)
    temp_path = Path(cli_args.temp_root)
    try:
        capsule_main(
            data_path=data_path,
            results_path=results_path,
            phy_pattern=cli_args.phy_pattern,
            temp_path=temp_path,
            symlink_file_types=cli_args.symlink_file_types
        )
    except:
        logging.error("Error running Phy.", exc_info=True)
        return -1


if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
