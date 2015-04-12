import glob
import sys
import os
version = sys.version.split(" ")[0]
majorminor = version[0:3]

paths = glob.glob("build/lib*-%s" % majorminor)
if paths:
    sys.path.insert(0, os.path.abspath(paths[0]))
