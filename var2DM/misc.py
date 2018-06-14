#!/usr/bin/env python3

# switching to using gbasis and iodata modules
# from horton (thus using python3)

"""
Miscellaneous functions for density matrix code.

ROUGH DRAFT
"""

import gbasis as gb
import iodata as iod
import numpy as np

__all__ = ['first_dm_hf', 'second_dm_hf', 'prep_electron_int']


def first_dm_hf(norb, nelec):
    """Calculate fist order density matrix for HF.

    Parameters
    ----------
    norb : integer
        Total number of molecular orbitals.
    nelec : integer
        Total number of electrons or occupied molecular orbitals.

    Returns
    -------
    first_dm : np.array(shape=(norb, norb))
        The first order density matrix.

    """
    first_dm = np.zeros((norb, norb))
    for i in range(0, nelec):
        first_dm[i, i] = 1

    return first_dm


def second_dm_hf(first_dm, norb, nelec):
    """Calculate second order density matrix for HF.

    Parameters
    ----------
    first_dm : np.array(shape=(norb, norb))
    norb : integer
        Total number of molecular orbitals.
    nelec : integer
        Total number of electrons or occupied molecular orbitals.

    Returns
    -------
    second_dm : np.array(shape=(norb^2, norb^2))
        The second order density matrix.

    """
    second_dm = np.zeros((norb**2, norb**2))
    for i in range(0, nelec):
        for j in range(0, nelec):
            idx_a = i*nelec + j
            for k in range(0, nelec):
                for l in range(0, nelec):
                    idx_b = k*nelec + l
                    second_dm[idx_a, idx_b] = first_dm[i, k] * first_dm[j, l]
                    second_dm[idx_a, idx_b] -= first_dm[i, l] * first_dm[j, k]

    return second_dm


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
    obasis = gb.get_gobasis(coords, nums, basis)
    # use horton to compute the gaussian integrals
    olp = obasis.compute_overlap()
    kin = obasis.compute_kinetic()
    na = obasis.compute_nuclear_attraction(coords, chrgs)
    er = obasis.compute_electron_repulsion()

    print(olp.shape)
    print(kin.shape)
    print(na.shape)
    print(er.shape)

    # use horton to create alpha orbitals
    # doesn't work
    # a_orbs = gb.load_orbsa_coeffs(obasis)
    # a_orbs = gb.Orbitals(obasis.nbasis)

    # use horton to make an initial guess for the electron
    # integrals
    one = kin + na
    # print(ht.guess_core_hamiltonian(olp, one, a_orbs))


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
