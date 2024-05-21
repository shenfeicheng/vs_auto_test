import shutil
import pytest
import os

if __name__ == "__main__":
    test_files = [
        "test_01.py",
        "test_02.py",
        "test_31.py",
        "test_32.py",
        "test_33.py",
        "test_34.py",
        "test_41.py",
        "test_42.py",
        "test_52.py",
    ]
    if os.path.exists("../Report/newxml"):
        shutil.rmtree("../Report/newxml")
    pytest_args = ["-vs"] + test_files + ["--alluredir", "../Report/newxml"]
    pytest.main(pytest_args)
