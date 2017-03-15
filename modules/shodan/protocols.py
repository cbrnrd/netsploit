from nsp.core import *
# Shows account specifics about what you can filter for
def protocols(api):
    try:
        prots = api.protocols()

        for name, description in iter(prots.items()):
            print_msg('{0:<30}'.format(name) + description)
    except shodan.APIError as e:
        print_err(str(e))

def help():
    return "Show protocols you can scan"
