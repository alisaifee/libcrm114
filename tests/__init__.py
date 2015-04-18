import glob
import sys
import os
import shutil
version = sys.version.split(" ")[0]
majorminor = version[0:3]
lib = glob.glob("build/lib*-%s/pycrm114/*.so" % majorminor)
out_dir = os.path.join(os.path.dirname(os.path.split(__file__)[0]), 'pycrm114')
if lib:
    shutil.copy(lib[0], out_dir)
