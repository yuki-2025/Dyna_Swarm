


# Copyright (c) Microsoft. All rights reserved.
import logging
import os
from time import gmtime, strftime
import sys
sys.path.append("./")

def create_logger(name, silent=False, to_disk=False, log_file=None):
    """Logger wrapper
    """
    # setup logger
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    log.propagate = False
    formatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    if not silent:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        log.addHandler(ch)
    if to_disk:
        # log_file = log_file if log_file is not None else strftime("outputs/logs/%Y-%m-%d-%H-%M-%S.log", gmtime())
        log_file = log_file if log_file is not None else strftime("my_scripts/demo_data_collect/%Y-%m-%d.log", gmtime())
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        log.addHandler(fh)
    return log


LOG = create_logger(
    "gptswarm_icl_2025",
    silent=False,
    to_disk=True,
    log_file=None
)

LOG.info("logger initialized ... ")