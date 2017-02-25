#!/bin/bash

echo -e "Installing shodan"
pip install shodan > /dev/null
echo -e "Done!"
mkdir tools
cd tools
echo -e "Installing additional tools"
pip install sslyze > /dev/null
git clone https://github.com/gkbrk/slowloris > /dev/null
cd slowloris
python setup.py install > /dev/null
cd ..
# include some of my own tools as well
git clone https://github.com/thecarterb/mail0wner.git > /dev/null
cd mail0wner
bash install.sh > /dev/null
cd ..
git clone https://github.com/thecarterb/hb-test-copy heartbleed > /dev/null
cd ..
echo -n "What is your shodan API key? "
read key
echo $key > .api_key
chmod +x netsploit
