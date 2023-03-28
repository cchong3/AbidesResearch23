import pandas as pd
pd.set_option('display.max_rows', None)

from sys import argv

if len(argv) > 1:
    log_file = argv[1]
    df = pd.read_pickle(argv[1])
    print (df)
else:
    print ("Usage: python dave_log_dump.py <path_to_log_file>")
