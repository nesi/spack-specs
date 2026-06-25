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
#     spack install micro
#
# You can edit this file again by typing:
#
#     spack edit micro
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *
import os
import shutil


class Micro(GoPackage):
    """micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the capabilities of modern terminals."""

    homepage = "https://github.com/micro-editor/micro"
    url = "https://github.com/micro-editor/micro/archive/refs/tags/v2.0.15.tar.gz"

    maintainers("wesharrell")

    license("MIT", checked_by="wesharrell")

    version("2.0.15", sha256="612c775321c268c8f9e1767505ff378bca9b9ab66f5c41b69ecb2464ecf15084")
    version("2.0.14", sha256="40177579beb3846461036387b649c629395584a4bbe970f61ba7591bd9c0185a")
    version("2.0.13", sha256="a96fff974ed6bd9a1dd58a33e54ff23b78783bbb3571b86d5c37d787b1e0e4be")

    depends_on("gmake")
    depends_on("go", type="build")

    phases = ["build", "install"]

    
    def build(self, spec, prefix):
        make("build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        shutil.copy("micro", prefix.bin)
