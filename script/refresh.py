from pathlib import Path
from subprocess import Popen, PIPE
from argparse import ArgumentParser
from loguru import logger
from utils.constant import *

import os
import sys


def main():
    mc_dir_list = [f.name for f in list(Path("../").glob("*/")) if f.joinpath("pack.toml").exists()]
    parser = ArgumentParser()
    parser.add_argument('-v')
    arg = parser.parse_args()
    if (arg.v is not None) and (arg.v not in mc_dir_list): raise ValueError
    for mc_dir in mc_dir_list:
        if arg.v is not None and mc_dir != arg.v: continue
        logger.remove()
        logger.add(
            sink=sys.stdout,
            format="<green>[{time:HH:mm:ss}]</green> <level>[{level}/(" +mc_dir + ")]</level>: <level>{message}</level>",
            level="DEBUG",
            colorize=True
        )
        process = Popen(
            [PACKWIZ, "refresh"],
            cwd="../{}".format(mc_dir),
            stdout=PIPE,
            text=True,
            bufsize=1
        )
        for e in process.stdout:
            text = e.strip()
            logger.info(text)
        process.wait()


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    os.chdir(script_dir)
    main()