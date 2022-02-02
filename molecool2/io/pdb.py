"""
Functions for manipulating pdb files.
"""

def open_pdb(file_location):
    """Open a pdb file and retrieve atom symbols and coordinates.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the pdb file.

    Returns
    -------
    coords : np.array
        The coordinates of the atoms in the pdb file.
    symbols : list
        The atomic symbols of the atoms in the pdb file.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if "ATOM" in line[0:6] or "HETATM" in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)

    return symbols, coords

