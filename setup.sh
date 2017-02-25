#!/bin/bash

# As of now, this script only works on Debian and OSX, but that's
# just because of the package managers installing zmap

os=uname
echo -e "Detected $os"
echo -e "Installing shodan"
pip install shodan > /dev/null 2>&1
echo -e "Done!"
mkdir tools
cd tools
echo ""
echo -e "Installing additional tools"
pip install sslyze > /dev/null 2>&1
git clone https://github.com/gkbrk/slowloris > /dev/null 2>&1
cd slowloris
python setup.py install > /dev/null 2>&1
cd ..

# c4 auto-execution script
echo "#!/bin/bash"                                      >> c4.sh
echo "os=uname"                                         >> c4.sh
echo "if [ \$os == \"Darwin\" ]; then"                     >> c4.sh
echo "  open \$(curl -Ls git.io/c4 | gshuf | head -n1)"  >> c4.sh
echo "else"                                             >> c4.sh
echo "  open \$(curl -Ls git.io/c4 | shuf | head -n1)"   >> c4.sh
echo "fi"                                               >> c4.sh
chmod +x c4.sh

# include some of my own tools as well
git clone https://github.com/thecarterb/mail0wner.git > /dev/null 2>&1
cd mail0wner
bash install.sh > /dev/null 2>&1
cd ..
git clone https://github.com/thecarterb/hb-test-copy heartbleed > /dev/null 2>&1
cd ..
#blacknurse router attack
git clone https://github.com/jedisct1/blacknurse > /dev/null 2>&1
cd blacknurse
make
cd ..
wget http://pastebin.com/raw/kGQ6qquB
mv kGQ6qquB cf-resolve.py

if [ $os == "Darwin" ]; then
  echo -e "Installing zmap"
  brew install zmap > /dev/null 2>&1
  echo -e "Installing coreutils"
  brew install coreutils > /dev/null 2>&1
  echo -n "Would you like to install tcpdump? (recommended) (y/n) "
  read ans
  if [ $ans == "y" ]; then
    echo "Installing tcpdump"
    brew install tcpdump > /dev/null 2>&1
  fi
else
  echo -e "Installing zmap"
  apt-get install -y zmap > /dev/null 2>&1
  echo -n "Would you like to install tcpdump? (recommended) (y/n) "
  read ans
  if [ $ans == "y" ]; then
    echo "Installing tcpdump"
    brew install tcpdump > /dev/null 2>&1
  fi
fi

cd ..
echo -n "What is your shodan API key? "
read key
echo $key > .api_key
chmod +x netsploit
