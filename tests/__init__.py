import glob
import sys
import os
import shutil
version = sys.version.split(" ")[0]
majorminor = version[0:3]
paths = glob.glob("build/lib*-%s" % majorminor)
out_dir = os.path.join(os.path.dirname(os.path.split(__file__)[0]), 'pycrm114')
if paths:
    shutil.copy(os.path.join(paths[0], 'pycrm114', '_binding.so'), out_dir)
