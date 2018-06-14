

from var2DM import misc
from var2DM import tools
import gbasis as gb
import iodata as iod
import os

def test_prep_electron_int():
    tmol = tools.mol_from_xyz(tools.get_xyz_path('water.xyz', True))
    # note: coordinates are in bohr not angstroms
    misc.prep_electron_int(tmol.coordinates, tmol.numbers,
                      tmol.pseudo_numbers, '3-21G')


if __name__ == "__main__":
    test_prep_electron_int()
