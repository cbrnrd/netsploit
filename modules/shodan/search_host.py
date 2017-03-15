import shodan
from nsp.core import *

# http://bit.ly/2lThKgm
def search_host(api, hostname, outfile=False, filename=''):
    domains = [".com", ".org", ".net", ".io"] #NOTE: not tested yet, mainly added for syntactic sugar
    if domains in hostname:
        hstip = socket.gethostbyname(hostname)
        print_msg("Searching shodan for {}({})...".format(hstip, hostname))
        host = api.host(hstip)
    else:
        print_msg("Searching for {}".format(hostname))
        host = api.host(hostname)
    if outfile:
        print_msg("Outputting results to: %s" % filename)
    else:
        print_msg("Outputting results to STDOUT")

    if outfile:
        with open(filename, 'w') as outf:
            outf.write("IP: %s\n" % host['ip_str'])
            outf.write("Organization: %s\n" % host.get('org', 'n/a'))
            outf.write("Operating System: %s\n" % host.get('os', 'n/a'))
            for item in host['data']:
                outf.write("Port: %s\n" % item['port'])
                outf.write("Banner: %s\n" % item['data'])

    # print general information about host
    print_good("IP: %s" % host['ip_str'])
    print_good("Organization: %s" % host.get('org', 'n/a'))
    print_good("Operating System: %s" % host.get('os', 'n/a'))

    for item in host['data']:
        print """
                Port: %s
                Banner: %s
        """ % (item['port'], item['data'])

def help():
    return "Search shodan for a given host"
