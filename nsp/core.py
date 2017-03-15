####
#
# This file defines basic functions and imports
# This file is a required import for all new modules
# XXX: I'm not sure if the imports transfer over between FACET_TITLES
# This needs to be tested to make sure everything works nicely
#
####

import re
import os
import sys
import urllib
import socket
import shodan
import threading
from time import sleep
from random import randint
from subprocess import call

class colors:
    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'
    UL       =  '\033[4m'

def print_msg(msg=''):
    print colors.OKBLUE + colors.BOLD + "[*] " + colors.ENDC + msg
def print_err(msg=''):
    print colors.FAIL + colors.BOLD + "[!] " + colors.ENDC + msg
def print_good(msg=''):
    print colors.OKGREEN + colors.BOLD + "[+] " + colors.ENDC + msg
def print_raw(msg=''):
    print msg

def banners():
    banner1 =  colors.FAIL + colors.BOLD + """
                  ____
                 /  @   \==]|[=(]               N E T S P L O I T ! !
                |--------|
                ==========       .  *                                     *
                ==========     .\ * . *.   *                         .    * \  .
               ||||||||||||      \ * ./  *    .   * SYN   ACK   SYN      .  \ \\
              |||||||||| --]%%%%%% .- =--=---=-=-=-=--=-=--=-==-----=-=-=-=-=-=
              [=========\  ]===========(  *         ACK   SYN   ACK     . /  /
             [==============|   / *  \    .                          *  *   /  .
             C| @ @ @ @ @ @ D         *      *                        *
              |              \           .                          *  *
            C| @  @ @  @ @ @  D       .
             |                 \          *                          *
           C| @  @  @  @  @  @  D
            |                    \
          C| @  @  @   @   @   @  D
           |                       \\
          |@@@@@@@@@@@@@@@@@@@@@@@@@|
           -------------------------

\033[0mBy thecarterb <0xCB[at]protonmail.com>
"""

    banner2 = colors.OKBLUE + colors.BOLD + """
                 ____________________________________________________
                /                                                    \\
               |    _____________________________________________     |
               |   |                                             |    |
               |   |  bash$ ./netsploit                          |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |                                             |    |
               |   |_____________________________________________|    |
               |                                                      |
                \_____________________________________________________/
                       \_______________________________________/
                    _______________________________________________
                 _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
              _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
           _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
        _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
     _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
    :-----------------------------------------------------------------------------:
    `---._.-----------------------------------------------------------------._.---'
    """ + colors.ENDC

    banner3 = colors.OKGREEN + """
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
    """ + colors.ENDC

    banner4 = """\033[033m""
    ^+xw*\"\"\"^q_  0 p" F  F _F  p^^"___jM   j  F              F
      _,,__   q x" [  F J_ J  P  w\"\"\"\"_  _,"  9  _m^`"*____x"    _____
 v,,_w"   "M_ @ `, ",_!u_9__L F #  r^""^^"    f j"      "      _*"   "6_
     _,,__  B 9_ "v,_Zp*\"\"\"\"\"^@u# P _m^"^u,a*"  j   ____       9       ""
   _F    `4 A_ "*-ap"            ^Lj" _smu,    _* ,-"   9_   _wf
 ^^"__,,_ jL  -- m<                5j! ____*-*^   &       \"\"\"\"     ___
   p"    9p`^u,av'       {}N E T{}     `,*\"\"\"\"q_   _x" _aa,_        p^\" \"\"u
 ,r  _____!L___,M     {}S P L O I T{}    Lsr--x_"^^`" qP     9      J      `M
   y^    "_    _J                    L_,,_ ?_    _#       ^v- -^"
  _F  __,_`^---"jr                  j___ ""y""^^""_,-r-u_
 r^ j!    ?s_, *"jp                g\"\"\"\"^q_b_    _F     "p      j^^""-w
    L  _,wma_  _x"jN__          __d\"\"\"^c  F  "-^""  _    "c____j'      L
   j" J"    \"\"\"  _F 99Nu______g**L_""s  4 A,    _P\"\"\"^q_    ""         "-
 m^  j_  _-^""mw^" _' # 9"N""L ^, "s  b #   "--^"      0
      @ j"   _v-wa+" ," j  #  p  r j qF "q_   _*-wu_   9,     y^`"^w_
   _,!  0_  f   _m-**" _F _F  L _FjP ?,    "^""    "u    "---^      j
 \"\"\"     # J   j"   p\"\"\"p-^ x^ p" d_   -q__a-mw_    j               `L
        V  `q  #   f   j   4   b   ^,   __      6_  ?,     _,__       "--
 *`^ww-"     F 9L_ b   1   4   `u_   "-^""*,    jh    ^-xm*"   9z
            )    0 `+a_ W__ 9,___"^^"+_     L   0                k
     _x-*v+"     9    0   "b    "_    "p   _0   `&    ___       d_

    {}""".format(colors.ENDC, "\033[033m", colors.ENDC, "\033[033m", colors.ENDC)
    randnum = randint(1, 4)
    if randnum == 1:
        return banner1
    elif randnum == 2:
        return banner2
    elif randnum == 3:
        return banner3
    else:
        return banner4
