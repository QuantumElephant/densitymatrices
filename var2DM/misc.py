#!/usr/bin/env python2

# need python2 because horton does not yet support
# python3 ....

"""
Miscellaneous functions for density matrix code.
ROUGH DRAFT
"""

import horton as ht

def collapse_density_matrix(input_matrix):
    """Collapse a density matrix.

    Parameters
    ----------
    input_matrix : np.array(shape=(N, N, N, N))
        The density matrix to collapse.

    Returns
    -------
    output_matrix : np.array(shape=(N^2, N^2))
        The collapsed density matrix.

    """
    pass

def expand_density_matrix(input_matrix):
    """Expand a density matrix.

    Parameters
    ----------
    input_matrix : np.array(shape=(N^2, N^2))
        The collapsed density matrix.

    Returns
    -------
    output_matrix : np.array(shape=(N, N, N, N))
        The expanded density matrix.


    """
    pass


def prep_electron_int(coords, nums, chrgs, basis):
    """Prepare the 1 and 2 electron integrals.

    Parameters
    ----------
    coords : numpy.array(N, 3) 
        float array with Cartesian coordinates (xyz) of the
        atoms, where N is the number of atoms.

    nums : numpy.array(N)
        int vector with length equal to the number of atoms,
        where the values are atomic numbers.

    chrgs : numpy.array(N)
        float array of pseudo-potential core charges.

    basis : str
        basis set to use. Example: 'aug-cc-pvtz'

    """
    # use horton to create a gaussian basis set
    obasis = ht.get_gobasis(coords, nums, basis)
    # use horton to compute the gaussian integrals
    olp = obasis.compute_overlap()
    kin = obasis.compute_kinetic()
    na = obasis.compute_nuclear_attraction(coords, nums, chrgs)
    er = obasis.compute_electron_repulsion()

    # use horton to create alpha orbitals
    a_orbs = ht.Orbitals(obasis.nbasis)

    # use horton to make an initial guess for the electron
    # integrals
    one = kin + na
    print(ht.guess_core_hamiltonian(olp, one, a_orbs))

def make_hamiltonian(el_int1, el_int2):
    """Generate a hamiltonian operator.

    Parameters
    ----------
    el_int1 : np.array(shape=(N, N))
        1 electron integrals matrix for N electrons

    el_int2 : np.array(shape=(N, N, N, N))
        2 electron integrals
        4 indices, N electrons

    Returns
    -------
    hamiltonian : not sure what this looks like

    """
    pass


def get_energy(hamiltonian, density_matrix):
    """Calculate the energy of the density matrix.

    Parameters
    ----------
    hamiltonian : not sure

    density_matrix : np.array(shape=(N^2, N^2))
        The collapsed version of the density matrix.

    Returns
    -------
    energy : float
        The energy of the density matrix with the
        given hamiltonian, as calculated using:
        trace(H*DM) = E

    """
    pass


