# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RCorrplot(RPackage):
    """Visualization of a Correlation Matrix.

    Provides a visual exploratory tool on correlation matrix that supports
    automatic variable reordering to help detect hidden patterns among
    variables."""

    cran = "corrplot"

    version('0.92', sha256='e8c09f963f9c4837036c439ebfe00fa3a6e462ccbb786d2cf90850ddcd9428bd')
    version('0.84', sha256='0dce5e628ead9045580a191f60c58fd7c75b4bbfaaa3307678fc9ed550c303cc')
    version('0.77', sha256='54b66ff995eaf2eee3f3002509c6f27bb5bd970b0abde41893ed9387e93828d3')
