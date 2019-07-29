# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from dataclasses import dataclass
from typing import Sequence, Union

from semver import VersionInfo

from ..util.process import ProcessContext


@dataclass
class PackageOptions:
    """
    Options that control how DAML packages are constructed.
    """
    files: 'Sequence[str]'
    output_path: str
    extra_args: 'Sequence[str]'


def package(options: 'PackageOptions', version: 'Union[None, str, VersionInfo]' = None) -> 'ProcessContext':
    args = ['daml', 'package', *_damlc_package_options(options)]
    return ProcessContext(args, logger=logging.getLogger('damlc'))


def _damlc_package_options(options: 'PackageOptions') -> 'Sequence[str]':
    if options.extra_args:
        return ['package', *options.files, *options.extra_args, 'package-name', '-o', options.output_path]
    else:
        return ['package', *options.files, 'package-name', '-o', options.output_path]
