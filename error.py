try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")