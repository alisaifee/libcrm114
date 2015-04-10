import glob
import sys

version = sys.version.split(" ")[0]
majorminor = version[0:3]

path = glob.glob("build/lib*-%s" % majorminor)[0]
sys.path.insert(0, path)


