SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    multiple = 1024

    for suffix in SUFFIX:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')    # un numero troppo grande non torna mai (perchè l'if non diventa mai true)