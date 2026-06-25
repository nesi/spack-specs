# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install broot
#
# You can edit this file again by typing:
#
#     spack edit broot
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Broot(CargoPackage):
    """Broot is a better way to navigate directories, find files, and launch commands, like `tree` with more functionality."""

    homepage = "https://github.com/Canop/broot"
    url = "https://github.com/Canop/broot/archive/refs/tags/v1.56.2.tar.gz"

    maintainers("wesharrell")

    license("MIT", checked_by="wesharrell")

    version("1.56.2", sha256="3e7be4252c76565f6d71b34bd07d26e1444b9ac2e1c8271c724f6e866fe75565")
    version("1.55.0", sha256="3049d055f37bfdc3b2057a3e2186cfdb58b596e1586b6b129698b350a80cfda3")
    version("1.54.0", sha256="92f88c6051c8ed7276d43a4ab45aacfe7b0dd1d65b3503d45ba1f9dad5e95cf1")

    depends_on("rust")


