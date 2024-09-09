import argparse

from flare_metrics.config import DATA_PATH
from flare_metrics.flare_metrics_ftso import flare_metrics_ftso
from flare_metrics.sys_explorer_ftso import sys_explorer_ftso


def main():
    parser = argparse.ArgumentParser(description='Collect FTSO data.')
    parser.add_argument('source', type=str, help='Source for collecting data.')
    parser.add_argument('network', type=str, help='Network of choice: flr or sgb.')

    args = parser.parse_args()

    if args.source == 'flare-metrics':
        flare_metrics_ftso(args.network)
    elif args.source == 'sys-explorer':
        if args.network != 'sgb':
            print('Network not supported.')
        else:
            sys_explorer_ftso()