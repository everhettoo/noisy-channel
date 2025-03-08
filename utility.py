def datafile(name, sep='\t'):
    """Read key,value pairs from file."""
    with open(name, 'r') as file:
        # file = open(name)
        for line in file:
            yield line.split(sep)
