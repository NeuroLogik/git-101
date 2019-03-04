SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    """ Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes

    Return: string
    """
    multiple = 1024

    for suffix in SUFFIX:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')    # un numero troppo grande non torna mai (perchè l'if non diventa mai true)