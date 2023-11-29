"""
pythoneda/shared/artifact/infrastructure/cli/python_dep_repository_folder_cli.py

This file defines the PythonDepRepositoryFolderCli.

Copyright (C) 2023-today rydnr's pythoneda-sandbox-artifact-def/python-dep

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.artifact.infrastructure.cli import RepositoryFolderCli


class PythonDepRepositoryFolderCli(RepositoryFolderCli):

    """
    A PrimaryPort used to gather the repository folder information.

    Class name: PythonDepRepositoryFolderCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the repository folder.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new PythonDepRepositoryFolderCli instance.
        """
        super().__init__()


print("loaded!")
