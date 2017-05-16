# Netsploit  [![Code Climate](https://codeclimate.com/github/thecarterb/netsploit/badges/gpa.svg)](https://codeclimate.com/github/thecarterb/netsploit)
A security research tool with shodan implementation

***

Netsploit is a python-based security research tool that implements the Shodan API. Netsploit is a growing project and welcomes contributions.


# Installing

#### Note: A Shodan API key is necessary any way you install Netsploit. Sign up for a free one [here](https://account.shodan.io/register)

Building from source is often the best solution:
1. `git clone https://github.com/thecarter/netsploit`
2. `cd netsploit`
3. `./setup.sh`
4. Now just start netsploit: `./netsploit`

The package dependencies for netsploit are as follows:
```
build-essential
cmake
libgmp3-dev
gengetopt
libpcap-dev
flex
byacc
libjson-c-dev
pkg-config
libunistring-dev
tcpdump
```

#### Debian package install:
` sudo apt-get install build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev tcpdump`

#### OS X package install (with `brew`):
`brew install pkg-config cmake gmp gengetopt json-c byacc libdnet libunistring tcpdump`


The main `pip` dependencies are as follows:
```
shodan
sslyze
```

Other program dependencies are (to be placed in the tools directory):

[Impacket](https://github.com/CoreSecurity/impacket)

[c4](https://github.com/turbo/c4)

[mail0wner](https://github.com/thecarterb/mail0wner)

[blacknurse](https://github.com/jedisct1/blacknurse)

[Sublist3r](https://github.com/aboul3la/Sublist3r)

[Slowloris](https://github.com/gkbrk/slowloris)

[Zmap](https://github.com/zmap/zmap)

Happy Hacking!

```
                                NETSPLOIT
          _                      _______                      _
       _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
      dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
      V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
               `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
                `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
           __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
         ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
      _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
     <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>
                  `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
          ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
        ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
       ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
       MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
       YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
        `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
          `'                  `OObNNNNNdOO'                   `'
                                `~OOOOO~'   BLEEG BLERG, ALL YOUR PACKETS ARE BELONG TO US
```
