def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    pmf = []
    def count_occurrence(target):
        counter = 0
        for number in samples:
            if number == target:
                counter += 1
        return counter
    
    def already_included(target):
        return target in [pair[0] for pair in pmf]
        
    for number in samples:
        count = count_occurrence(number)
        if not already_included(number):
            pmf.append((number, count/len(samples)))
    
    return pmf

