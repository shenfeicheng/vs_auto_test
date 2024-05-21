import shutil
import pytest
import os

if __name__ == "__main__":
    test_files = [
        "test_area.py",
        "test_store.py",
    ]
    if os.path.exists("../Report/newxml"):
        shutil.rmtree("../Report/newxml")
    pytest_args = ["-vs"] + test_files + ["--alluredir", "../Report/newxml"]
    pytest.main(pytest_args)
