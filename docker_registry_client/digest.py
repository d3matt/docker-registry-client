import hashlib


def docker_digest(fpath=None, fobj=None, prepend=True):
    if fobj is None:
        fobj = open(fpath, 'rb')
    hasher = hashlib.sha256()
    for chunk in iter(lambda: fobj.read(8192), b''):
        hasher.update(chunk)
    fobj.seek(0)
    retval = hasher.hexdigest()
    if prepend:
        retval = 'sha256:' + retval
    return retval
