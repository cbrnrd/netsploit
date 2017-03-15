import shodan
from nsp.core import *
# http://bit.ly/2lTq3su
def facets(api, query):
    # The list of properties we want summary information on
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',

        # We only care about the top 5 countries, this is how we let Shodan know to return 5 instead of the
        # default 10 for a facet. If you want to see more than 10, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 5),
    ]

    FACET_TITLES = {
        'org': 'Top 10 Organizations',
        'domain': 'Top 10 Domains',
        'port': 'Top 10 Ports',
        'asn': 'Top 10 Autonomous Systems',
        'country': 'Top 5 Countries',
    }

    try:
        # Generate a query string out of the params
        query = ' '.join(query)

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = api.count(query, facets=FACETS)

        print 'Shodan Summary Information'
        print 'Query: %s' % query
        print 'Total Results: %s\n' % result['total']

        # Print the summary info from the facets
        for facet in result['facets']:
            print FACET_TITLES[facet]

            for term in result['facets'][facet]:
                print '%s: %s' % (term['value'], term['count'])

            # Print an empty line between summary info
            print ''
    except Exception as e:
        print_err("Error: {}".format(str(e)))

def help():
    return "Gets top ports, services, companies, etc."
