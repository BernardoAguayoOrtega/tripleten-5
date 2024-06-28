import os
import subprocess
import sys

# Define the required packages
required_packages = [
    "pandas",
    "plotly-express",
    "streamlit",
    "jupyter"
]

# Function to create a virtual environment
def create_virtualenv(venv_name):
    subprocess.check_call([sys.executable, "-m", "venv", venv_name])

# Function to install packages in the virtual environment
def install_packages(venv_name, packages):
    pip_executable = os.path.join(venv_name, "bin", "pip")
    for package in packages:
        subprocess.check_call([pip_executable, "install", package])

# Main initialization process
def main():
    venv_name = "venv"
    print(f"Creating virtual environment '{venv_name}'...")
    create_virtualenv(venv_name)
    print(f"Virtual environment '{venv_name}' created successfully!")

    print("Installing required packages...")
    install_packages(venv_name, required_packages)
    print("Packages installed successfully!")

    # Create a basic notebook
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

    with open("example_notebook.ipynb", "w") as f:
        f.write(notebook_content)
    
    print("Example Jupyter Notebook created successfully!")

if __name__ == "__main__":
    main()
