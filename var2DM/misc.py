#!/usr/bin/env python3

"""
Miscellaneous functions for density matrix code.
ROUGH DRAFT
"""

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


def make_hamiltonian(1e_int, 2e_int):
    """Generate a hamiltonian operator.

    Parameters
    ----------
    1e_int : np.array(shape=(N, N))
        1 electron integrals matrix for N electrons

    2e_int : np.array(shape=(N, N, N, N))
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


