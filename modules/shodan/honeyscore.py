import shodan
from nsp.core import *

# Uses the shodan api to check if something is a honeypot
# Honeyscore cam range from 0.0-1.0
def honey(api, ip):
    try:
        score = api.labs.honeyscore(ip)
        if score == 1.0:
            print_good("{} is a honeypot!".format(ip))
        elif score > 0.5:
            print "{}[-]{}{ } is probably a honeypot.".format(bcolors.WARN, bcolors.ENDC, ip)
        elif score <= 0.5 and score != 0.0:
            print_msg("{} is probably not a honeypot.".format(ip))
        else:
            print_err("{} is not a honeypot.".format(ip))
        print_msg("{} honeyscore: {}".format(ip, score))
    except Exception as e:
        print_err("Could not determine honeyscore. ({})".format(e))

def help():
    return "Check if an ip is a honeypot or not (0.0 - 1.0)"
