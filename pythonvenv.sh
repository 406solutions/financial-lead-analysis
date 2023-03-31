#!/bin/bash

# Install python3-venv package if not installed
sudo apt-get update
sudo apt-get install python3-venv -y

# Create a new directory for the virtual environment
mkdir myenv

# Navigate to the new directory
cd myenv

# Create the virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install required packages, e.g., pandas
pip install pandas

# Deactivate the virtual environment
deactivate
