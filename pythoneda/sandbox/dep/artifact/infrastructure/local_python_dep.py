"""
rydnr/sandbox/dep/artifact/infrastructure/local_python_dep.py

This file defines LocalPythonDep

Copyright (C) 2023-today rydnr's pythoneda-sandbox/python-dep-artifact

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
from pythoneda import listen
from pythoneda.shared.artifact import LocalArtifact
from pythoneda.shared.artifact.events import (
    CommittedChangesPushed,
    CommittedChangesTagged,
    StagedChangesCommitted,
    TagPushed,
)
from pythoneda.shared.nix_flake import (
    FlakeUtilsNixFlake,
    License,
    NixosNixFlake,
    PythonedaSharedPythonedaBannerNixFlake,
)
from pythoneda.shared.nix_flake.licenses import Gpl3


class LocalPythonDep(LocalArtifact):

    """
    A locally-cloned PythonDep.

    Class name: LocalPythonDep

    Responsibilities:
        - Represent the PythonDep artifact.

    Collaborators:
        - pythoneda.shared.artifact.Artifact: Common logic for Artifacts.
        - pythoneda.sandbox.dep.artifact.application.PythonDepApplication: To initialize this class.
    """

    _singleton = None

    def __init__(self, folder: str):
        """
        Creates a new LocalPythonDep instance.
        :param folder: The folder with the python-dep repository.
        :type folder: str
        """
        flake_utils = FlakeUtilsNixFlake.default()
        nixos = NixosNixFlake.default()
        banner = PythonedaSharedPythonedaBannerNixFlake.default()
        inputs = [flake_utils, nixos, banner]
        version = self.find_out_version(folder)
        super().__init__(
            "pythoneda-sandbox-python-dep",
            self.find_out_version(folder),
            self.url_for,
            inputs,
            "pythoneda",
            "pythoneda-sandbox Python-Dep package",
            "https://github.com/pythoneda-sandbox/python-dep",
            License.from_id(
                Gpl3.license_type(),
                "2023",
                "rydnr",
                "https://github.com/pythoneda-sandbox/python-dep",
            ),
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
            folder,
        )

    @classmethod
    def initialize(cls, folder: str):
        """
        Initializes the singleton.
        :param folder: The repository folder.
        :type folder: str
        """
        cls._singleton = LocalPythondDep(folder)

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: Ports
        """
        result = cls._singleton
        if result is None:
            LocalPythonDep.logger().error(
                "LocalPythonDep not yet bound to a local folder. "
            )
        return result

    def url_for(self, version: str) -> str:
        """
        Retrieves the url for given version.
        :param version: The version.
        :type version: str
        :return: The url.
        :rtype: str
        """
        return f"https://github.com/pythoneda-sandbox/python-dep-artifact/{version}?dir=python-dep"

    @classmethod
    @listen(StagedChangesCommitted)
    async def listen_StagedChangesCommitted(
        cls, event: StagedChangesCommitted
    ) -> CommittedChangesPushed:
        """
        Gets notified of a StagedChangesCommitted event.
        :param event: The event.
        :type event: pythoneda.shared.artifact.events.StagedChangesCommitted
        :return: An event notifying the commit has been pushed.
        :rtype: pythoneda.shared.artifact.events.CommittedChangesPushed
        """
        return await cls.instance().commit_push(event)

    @classmethod
    @listen(CommittedChangesPushed)
    async def listen_CommittedChangesPushed(
        cls, event: CommittedChangesPushed
    ) -> CommittedChangesTagged:
        """
        Gets notified of a CommittedChangesPushed event.
        :param event: The event.
        :type event: pythoneda.shared.artifact.events.CommitedChangesPushed
        :return: An event notifying the changes have been pushed.
        :rtype: pythoneda.shared.artifact.events.CommittedChangesTagged
        """
        return await cls.instance().commit_tag(event)

    @classmethod
    @listen(CommittedChangesTagged)
    async def listen_CommittedChangesTagged(
        cls, event: CommittedChangesTagged
    ) -> TagPushed:
        """
        Gets notified of a CommittedChangesTagged event.
        Pushes the changes and emits a TagPushed event.
        :param event: The event.
        :type event: pythoneda.shared.artifact.events.CommittedChangesTagged
        :return: An event notifying the changes have been pushed.
        :rtype: pythoneda.shared.artifact.events.TagPushed
        """
        return await cls.instance().tag_push(event)
