from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od


env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True


a = automodel(env, alnfile='hetero_BLK.ali',
              knowns=('3u2o','6oc0','2wv8'), sequence='A0A0J5PZ55_ASPFM', 
assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))


a.starting_model = 1
a.ending_model = 1

a.make()

