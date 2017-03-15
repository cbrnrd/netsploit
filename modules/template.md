## Creating your own module

We all get curious, it's in our nature. If you want to add your own splash of flavor to netsploit, go ahead.

___However___, in order for your creativity to work properly (sounds kind of contradicting right?), you need to format your module correctly.

Here is the basic template:

```python
# Your imports here (Try to stay away from external modules, but if you really need it I might make an exception)
import shodan # NOTE: Use this if making a shodan module, you will also need the api as a parameter in run()
import nsp.core  # This is needed

def module_name(opts):
    # Do stuff here

def help():
    return "Short help message here"


```
