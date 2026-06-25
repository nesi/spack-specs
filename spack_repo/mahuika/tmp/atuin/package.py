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
#     spack install atuin
#
# You can edit this file again by typing:
#
#     spack edit atuin
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Atuin(CargoPackage):
    """Atuin replaces your existing shell history with a SQLite database, and records 
    additional context for your commands. With this context, Atuin gives you faster 
    and better search of your shell history.  Additionally, Atuin (optionally) 
    syncs your shell history between all of your machines. Fully end-to-end encrypted, 
    of course."""

    homepage = "https://axputin.sh"
    url = "https://github.com/atuinsh/atuin/archive/refs/tags/v18.10.0.tar.gz"

    version("18.10.0", sha256="02228929976142f63b4464a35b8b29b29155e1814cf03e99c95381954c5d9e37")


    maintainers("wesharrell")

    license("MIT", checked_by="wesharrell")


    depends_on("rust", type="build")

    def build(self, spec, prefix):
        cargo("build")

    def install(self, spec, prefix):
        install_tree("atuin", prefix)
