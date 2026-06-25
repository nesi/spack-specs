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
#     spack install jnv
#
# You can edit this file again by typing:
#
#     spack edit jnv
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Jnv(CargoPackage):
    """jnv is designed for navigating JSON, offering an interactive JSON viewer and jq filter editor."""

    homepage = "https://github.com/ynqa/jnv"
    url = "https://github.com/ynqa/jnv/archive/refs/tags/v0.7.0.tar.gz"

    maintainers("wesharrell")

    license("MIT", checked_by="wesharrell")

    version("0.7.0", sha256="7ac4379a04732c250d5f818f58fbf14adec6db9188157789cd82ba3ea3c555d1")
    version("0.6.2", sha256="767226c67378381d1e71ffe0e631a5b5ffc00e957a05780a9b23b6a65023bb44")

    depends_on("rust")

    #def build(self, spec, prefix):



