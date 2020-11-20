""" Script to extract data from source. """
import os
import subprocess
import zipfile

import dotenv

import scripts.etl.constants as const


def load_kaggle_envars():
    dotenv.load_dotenv(os.path.join(const.ENVARS_DIR, "kaggle.env"))


def download_dataset_from_kaggle_as_zip():
    cwd = subprocess.check_output("pwd").decode("utf-8").strip("\n")
    subprocess.run(
        [
            const.VENV_KAGGLE_BIN,
            "datasets",
            "download",
            "-d",
            "olistbr/brazilian-ecommerce",
            "-p",
            const.DATA_DIR,
        ],
        cwd=cwd,
    )


def unzip_dataset():
    with zipfile.ZipFile(f"{const.DATA_DIR}/brazilian-ecommerce.zip", "r") as zip:
        zip.extractall(const.DATA_DIR)

    os.remove(f"{const.DATA_DIR}/brazilian-ecommerce.zip")
