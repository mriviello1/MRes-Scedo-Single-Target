# Comparative modeling by the automodel class
from modeller import *
from modeller.automodel import *    # Load the automodel class

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']


# Read in HETATM records from template PDBs
env.io.hetatm = True

a = dopehr_loopmodel (env,
              alnfile =('hetero_BLK.ali'),     # alignment filename
              knowns =('3u2o','6oc0','2wv8'),    # codes of the templates
              sequence= ('A0A0J5PZ55_ASPFM'),  # code of the target
loop_assess_methods = assess.DOPE)

a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.md_level = None                   # No refinement of model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 1           # Last loop model
a.loop.md_level       = refine.slow # Loop model refinement level

a.make()                            # do comparative modeling



