#!/bin/bash

CURRENT_DIR=pwd
echo -e "Installing shodan"
pip install shodan > /dev/null
echo -e "Done!"
mkdir $CURRENT_DIR/tools
cd tools
echo -e "Installing additional tools"
wget https://downloads.sourceforge.net/project/sslscan/sslscan/sslscan-1.8.2.tgz
tar xzf sslscan-1.8.2.tgz -C sslscan > /dev/null
git clone https://github.com/gkbrk/slowloris
cd slowloris
pip install -r requirements.txt
python setup.py install
cd ../..
echo -n "What is your shodan API key?"
read key
echo $key > .api_key
