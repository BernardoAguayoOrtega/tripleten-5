import os
import subprocess
import sys

# Function to read the requirements.txt file
def read_requirements(filename="requirements.txt"):
    with open(filename, "r") as file:
        return file.read().splitlines()

# Function to create a virtual environment
def create_virtualenv(venv_name):
    subprocess.check_call([sys.executable, "-m", "venv", venv_name])

# Function to install packages in the virtual environment
def install_packages(venv_name, packages):
    if sys.platform == "win32":
        pip_executable = os.path.join(venv_name, "Scripts", "pip")
    else:
        pip_executable = os.path.join(venv_name, "bin", "pip")
    for package in packages:
        subprocess.check_call([pip_executable, "install", package])

# Main initialization process
def main():
    venv_name = "venv"
    print(f"Creating virtual environment '{venv_name}'...")
    create_virtualenv(venv_name)
    print(f"Virtual environment '{venv_name}' created successfully!")

    print("Reading required packages from requirements.txt...")
    required_packages = read_requirements()
    print("Installing required packages...")
    install_packages(venv_name, required_packages)
    print("Packages installed successfully!")

    # Create the notebooks directory if it doesn't exist
    notebooks_dir = "notebooks"
    if not os.path.exists(notebooks_dir):
        os.makedirs(notebooks_dir)
        print(f"Directory '{notebooks_dir}' created successfully!")

    # Create a basic notebook
    notebook_path = os.path.join(notebooks_dir, "EDA.ipynb")
    notebook_content = """\
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary libraries\\n",
    "import pandas as pd\\n",
    "import plotly.express as px\\n",
    "import streamlit as st"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""

    with open(notebook_path, "w") as f:
        f.write(notebook_content)
    
    print(f"Notebook '{notebook_path}' created successfully!")

if __name__ == "__main__":
    main()
