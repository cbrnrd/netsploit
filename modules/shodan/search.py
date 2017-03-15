import shodan
from nsp.core import *
# Do a basic shodan search
def search(api, content, outfile=False, filename=''):
    print_msg("Searching for {}".format(content))
    if outfile:
        print_msg("Outputting to \'{}\'".format(filename))
    else:
        print_msg("Printing to STDOUT")
    results = api.search(content)  # Search shodan
    if outfile:
        with open(filename, 'w') as outf:
            for result in results['matches']:
                outf.write(result['ip_str'] + "\n")
    else:
        for result in results['matches']:
            print_good(result['ip_str'])

def help():
    return "Do a basic shodan search"
