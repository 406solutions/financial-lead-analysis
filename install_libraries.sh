#!/bin/bash

# Update package list and install pip
sudo apt-get update
sudo apt-get install python3-pip -y

# Install pandas and Flask
pip3 install pandas
pip3 install Flask

# Install pykafka
pip3 install pykafka

#install csv 
pip install python-csv

# Install Drools
wget https://download.jboss.org/drools/release/7.54.0.Final/drools-distribution-7.54.0.Final.zip
unzip drools-distribution-7.54.0.Final.zip
rm drools-distribution-7.54.0.Final.zip
