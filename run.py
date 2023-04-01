import argparse
from enum import Enum
import app
import test
import subprocess


class RunningType(Enum):
    MAIN = 'main'
    TEST = 'test'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'type', choices=[RunningType.MAIN.value, RunningType.TEST.value])
    args = parser.parse_args()

    if args.type == RunningType.MAIN.value:
        app.main()
    else:
        subprocess.run(['pytest', 'test.py'])


if __name__ == '__main__':
    main()
