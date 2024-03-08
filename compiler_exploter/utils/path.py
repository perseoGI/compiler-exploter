import os
from shutil import copy2
from compiler_exploter.utils.constants import CACHE_PATH, LOG_FILE
import tempfile


def get_repo_name(url: str) -> str:
    """
    Return a string composed by <org/user_name>_<repo_name>"
    Supports both HTTPS and SSH formats
    """
    parts = url.replace(":", "/").replace(".git", "").split("/")

    # Extract org and repo from parts
    org_name = parts[-2]
    repo_name = parts[-1]

    return f"{org_name}__{repo_name}"


def get_download_path(repo_name: str) -> str:
    return os.path.join(CACHE_PATH, repo_name)


def get_build_path(source_path: str, branch: str) -> str:
    return os.path.join(source_path, "build", branch)


def get_zip_path(name: str, branch: str) -> str:
    return os.path.join(CACHE_PATH, f"{name}_{branch}.zip")


def get_log_file(log_file: str) -> str:
    return copy2(log_file, os.path.join(tempfile.gettempdir(), LOG_FILE))
