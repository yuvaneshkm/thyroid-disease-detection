# importing necessary libraries:
import os
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")


# Creating list of files and folders:
list_of_files = [
    ".github/workflows/.gitkeep",
    # experiments:
    "experiments/dummy_file.txt",
    # source data:
    "source_data/dummy_file.txt",
    # src:
    "src/__init__.py",
    # src------>exception.py:
    "src/exception.py",
    # src------>logging.py:
    "src/logger.py",
    # src------>utils.py:
    "src/utils.py",
    # src/components:
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    # src/pipeline:
    "src/pipeline/__init__.py",
    "src/pipeline/ETL_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    # tests:
    "tests/__init__.py",
    # tests/unit:
    "tests/unit/__init__.py",
    # tests/integration:
    "tests/integration/__init__.py",
    # setup:
    "setup.py",
    "setup.cfg",
    "init_setup.sh",
    # requirements:
    "requirements.txt",
    "requirements_dev.txt",
    # ini file:
    "tox.ini",
    # toml file:
    "pyproject.toml",
    # app:
    "app.py",
    # README.md:
    "README.md",
]


# creating files and folders:
for filepath in list_of_files:
    filepath = Path(filepath)

    # directory name and file name:
    filedir, filename = os.path.split(filepath)

    # creating directory:
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # creating files:
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        f.close()
