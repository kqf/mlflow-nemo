# setup.py
from setuptools import setup, find_packages

setup(
    name="mlflow-nemo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "mlflow"
    ],
    entry_points={
        "console_scripts": ["mlflow-nemo=nemo.cli:cli"],
    },
    description="An MLflow plugin providing the 'nemo' CLI command",
)
