# Cab 
CAB simulation in python

---

### Encountered Problem:

- #### Variables in python class
```
def class:
    def __init__(name = ""):
        self.name = name        # Instance Variable
    
    name = ""                   # Class Variable, like static in Java
```

- #### << in Python has very low priority, even lower than +/-

- #### Delete element in list which meets some condition
```
# Get the sublist, whose elements don't meet the condition
somelist[:] = [x for x in somelist if not determine(x)]
```
