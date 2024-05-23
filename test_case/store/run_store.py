import shutil
import pytest
import os

if __name__ == "__main__":
    test_files = [
        "test_store.py",
    ]
    pytest_args = ["-vs"] + test_files + ["--alluredir", "../../Report/newxml"]
    pytest.main(pytest_args)
