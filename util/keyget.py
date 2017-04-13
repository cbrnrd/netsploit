import os

key = input("What is your Shodan API key? ")
with open(os.path.realpath(__file__) + "/../.api_key", 'w') as f:
    f.write(key)
    f.close()
