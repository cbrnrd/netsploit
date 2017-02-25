#!/bin/bash

# As of now, this script only works on Debian and OSX, but that's
# just because of the package managers installing zmap

os = uname
echo -e "Detected $os"
echo -e "Installing shodan"
pip install shodan > /dev/null
echo -e "Done!"
mkdir tools
cd tools
echo ""
echo -e "Installing additional tools"
pip install sslyze > /dev/null
git clone https://github.com/gkbrk/slowloris > /dev/null
cd slowloris
python setup.py install > /dev/null
cd ..

echo "#!/bin/bash"                                      >> c4.sh
echo "os=uname"                                         >> c4.sh
echo "if[\$os == \"Darwin\"]; then"                     >> c4.sh
echo "  open $(curl -Ls git.io/c4 | gshuf | head -n1)"  >> c4.sh
echo "else"                                             >> c4.sh
echo "  open $(curl -Ls git.io/c4 | shuf | head -n1)"   >> c4.sh
echo "fi"                                               >> c4.sh
chmod +x c4.sh
# include some of my own tools as well
git clone https://github.com/thecarterb/mail0wner.git > /dev/null
cd mail0wner
bash install.sh > /dev/null
cd ..
git clone https://github.com/thecarterb/hb-test-copy heartbleed > /dev/null
cd ..

if [$os == "Darwin"]; then
  echo -e "Installing zmap"
  brew install zmap > /dev/null
else
  echo -e "Installing zmap"
  apt-get install -y zmap > /dev/null
fi

echo -n "What is your shodan API key? "
read key
echo $key > .api_key
chmod +x netsploit
