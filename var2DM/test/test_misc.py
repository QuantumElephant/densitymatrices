

from var2DM import misc
from var2DM import tools
import gbasis as gb
import iodata as iod
import numpy as np
import numpy.testing as npt
import os


def test_diag_first_dm():
    """Test that the diagonal of the first order density matrix adds to
       the number of electrons.

    """
    nelec = 8
    norb = nelec + 10
    first_dm = misc.first_dm_hf(norb, nelec)
    trace = np.trace(first_dm)
    msg = "Diagonal of first order DM does not equal N"
    exp_trace = nelec
    npt.assert_allclose(trace, exp_trace, err_msg=msg)


def test_diag_second_dm():
    """Test that the diagonal of the second order density matrix adds to
       the N*(N-1).

    """
    nelec = 8
    norb = nelec + 10
    first_dm = misc.first_dm_hf(norb, nelec)
    second_dm = misc.second_dm_hf(first_dm, norb, nelec)
    trace = np.trace(second_dm)
    msg = "Diagonal of second order DM does not equal N * (N - 1)"
    exp_trace = nelec * (nelec - 1)
    npt.assert_allclose(trace, exp_trace, err_msg=msg)


def test_prep_electron_int():
    tmol = tools.mol_from_xyz(tools.get_xyz_path('water.xyz', True))
    # note: coordinates are in bohr not angstroms
    mol = iod.IOData.from_file(test_file)
    misc.prep_electron_int(mol.coordinates, mol.numbers,
                           mol.pseudo_numbers, '3-21G')
    misc.prep_electron_int(tmol.coordinates, tmol.numbers,
                      tmol.pseudo_numbers, '3-21G')


if __name__ == "__main__":
    test_prep_electron_int()
