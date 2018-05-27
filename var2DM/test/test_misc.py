

from var2DM import misc
import gbasis as gb
import iodata as iod

def test_prep_electron_int():
    test_file = 'data/test/water.xyz'
    # note: coordinates are in bohr not angstroms
    mol = iod.IOData.from_file(test_file)
    misc.prep_electron_int(mol.coordinates, mol.numbers,
                      mol.pseudo_numbers, '3-21G')


if __name__ == "__main__":
    test_prep_electron_int()
