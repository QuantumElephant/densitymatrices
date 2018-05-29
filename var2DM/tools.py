#!/usr/bin/env python3

import os

__all__ = ['get_xyz_path']

def get_xyz_path(fname, test=True):
    """Construct a path to an xyz file.

    Parameters
    ----------
    fname : str
        The name of the xyz file.

    test : bool
        Default of True, which implies the xyz
        file is in var2DM/test/data. False implies
        the input file is in var2DM/data.

    Returns
    -------
    fname_path : str
        The full path of the xyz file.

    """
    tools_path = os.path.dirname(os.path.realpath(__file__))
    if test:
        fname_path = os.path.join(tools_path, 'test/data/', fname)
    else:
        fname_path = os.path.join(tools_path, 'data/', fname)
    return fname_path
