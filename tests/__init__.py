import glob
import sys

try:
    import pycrm114
except ImportError:
    version = sys.version.split(" ")[0]
    majorminor = version[0:3]

    path = glob.glob("build/lib*-%s" % majorminor)[0]
    sys.path.insert(0, path)


