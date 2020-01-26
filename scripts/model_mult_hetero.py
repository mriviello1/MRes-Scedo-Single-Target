from modeller import *
from modeller.automodel import *


env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True


a = automodel(env, alnfile='hetero_BLK.ali',
              knowns=('3u2o','6oc0','2wv8'), sequence='A0A0J5PZ55_ASPFM') 


a.starting_model = 1
a.ending_model = 5

a.make()


