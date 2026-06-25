# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# them, you can save this file and test your package like this:
#
#     spack install zellij
#
# You can edit this file again by typing:
#
#     spack edit zellij
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Zellij(CargoPackage):
    """Terminal Workspace with Batteries Included.  Zellij is a workspace aimed at developers, ops-oriented people and anyone who loves the terminal. 
    Similar programs are sometimes called Terminal Multiplexers. """

    homepage = "https://zellij.dev/"
    url = "https://github.com/zellij-org/zellij/archive/refs/tags/v0.44.0.tar.gz"

    maintainers("wesharrell")

    license("MIT", checked_by="wesharrell")

    version("0.44.0", sha256="be413dc49d7bff1be6502a1998664b015b77ad55636d72e0497cfc66d4a4cdf6")
    version("0.43.1", sha256="e9fd24190869be6e9e8d731df2ccd0b3b1dd368ae9dbb9d620ec905b83e325ec")

    depends_on("rust")


