# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that CLI commands work properly.
"""
from pathlib import Path

from dazl import sandbox
from dazl.cli import _main

DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'


def test_simple_ls():
    with sandbox(daml_path=DAML_PATH) as proc:
        exit_code = _main(f'dazl ls --url {proc.url} --parties=Alice'.split(' '))

    assert exit_code == 0


def test_simple_ls_two_parties():
    with sandbox(daml_path=DAML_PATH) as proc:
        exit_code = _main(f'dazl ls --url {proc.url} --parties=Alice,Bob'.split(' '))

    assert exit_code == 0


def test_env_ls():
    import os
    with sandbox(daml_path=DAML_PATH) as proc:
        os.environ['DAML_LEDGER_URL'] = proc.url
        os.environ['DAML_LEDGER_PARTY'] = 'Alice'
        exit_code = _main('dazl ls'.split(' '))

    assert exit_code == 0
