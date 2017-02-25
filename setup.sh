#!/bin/bash

CURRENT_DIR=pwd
echo -e "Installing shodan"
pip install shodan > /dev/null
echo -e "Done!"
mkdir tools
cd tools
echo -e "Installing additional tools"
pip install sslyze > /dev/null
git clone https://github.com/gkbrk/slowloris > /dev/null
cd slowloris
python setup.py install
cd ../..
echo -n "What is your shodan API key?"
read key
echo $key > .api_key
chmod +x netsploit
