# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = './:../atom_files'
# Read in HETATM records from template PDBs
env.io.hetatm = True

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # 10 residue insertion 
        return selection(self.residue_range('1', '446'))

m = MyLoop(env,
           inimodel='A0A0J5PZ55_ASPFM.B99990035.pdb', # initial model of the target
           sequence='A0A0J5PZ55_ASPFM')          # code of the target

m.loop.starting_model= 1           # index of the first loop model 
m.loop.ending_model  = 1          # index of the last loop model
m.loop.md_level = refine.slow # loop refinement method; this yields
                                   # models quickly but of low quality;
                                   # use refine.slow for better models

m.make()

