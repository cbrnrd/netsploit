#!/bin/bash

echo -e "Installing shodan"
pip install shodan > /dev/null
echo -e "Done!"
#echo -e "Installing sslize"
#git clone https://github.com/iSECPartners/sslyze > /dev/null
echo -n "What is your shodan API key?"
read key
echo $key > .api_key
