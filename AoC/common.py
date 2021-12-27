def get_input(datatype=str, sample=False):
    filename = 'sample_input.txt' if sample else 'input.txt'
    with open(filename) as datafile:
        data = datafile.readlines()
    data = [datatype(d.strip()) for d in data]
    return data
