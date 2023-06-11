import argparse
import os
from enum import Enum
import app
import subprocess


class RunningType(Enum):
    MAIN = "main"
    TEST = "test"
    UNIT = "unit"
    UI = "ui"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "type",
        choices=[
            RunningType.MAIN.value,
            RunningType.TEST.value,
            RunningType.UNIT.value,
            RunningType.UI.value,
        ],
    )
    args = parser.parse_args()

    if args.type == RunningType.MAIN.value:
        subprocess.run(["py", "app.py"])
    elif args.type == RunningType.UNIT.value:
        subprocess.run(["pytest", "test_unit.py"])
    elif args.type == RunningType.UI.value:
        subprocess.run(["pytest", "test_ui.py"])
    else:
        subprocess.run(["pytest", "test.py"])


if __name__ == "__main__":
    os.environ["QT_SCALE_FACTOR"] = "2.0"
    main()
