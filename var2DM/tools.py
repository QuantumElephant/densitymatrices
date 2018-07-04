#!/usr/bin/env python3

import os
import iodata as iod

__all__ = ['get_xyz_path', 'mol_from_xyz']

def get_xyz_path(fname, test=None):
    """Construct a path to an xyz file.

    Parameters
    ----------
    fname : str
        The name of the xyz file.

    test : bool, NoneType
        Default of None, which means the path is
        relative/absolute to the current working directory.
        True implies the xyz file is in var2DM/test/data.
        False implies the input file is in var2DM/data.

    Raises
    ------
    FileNotFoundError
        If the test input variable is set to None
        and the file cannot be found, then this error
        is raised.

    Returns
    -------
    fname_path : str
        The full path of the xyz file (including file name).

    """
    if test is None:
        if os.path.isfile(fname):
            return os.path.abspath(fname)
        raise FileNotFoundError("No such file could be found.")
    tools_path = os.path.dirname(os.path.realpath(__file__))
    if test:
        return os.path.join(tools_path, 'test/data/', fname)
    else:
        return os.path.join(tools_path, 'data/', fname)

def mol_from_xyz(full_path):
    """Use IOData to make a molecule object using an xyz file.

    Parameters
    ----------
    full_path : str
        Full path and filename to use to make the molecule.
        Should be an xyz file.

    Notes
    -----
    You can get the full path using the get_xyz_path function
    in the tools.py file.

    Returns
    -------
    IOData file object (molecule)

    """
    return iod.IOData.from_file(full_path)
