# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import logging
import os
from pathlib import Path
from threading import RLock
from typing import Mapping

# pytest is a test dependency
# noinspection PyPackageRequirements
import pytest

from dazl import setup_default_logger
from dazl.model.types import TypeReference
from dazl.model.types_store import PackageStore
from dazl.util.dar import DarFile
from dazl.util.io import find_free_port
from dazl.util.process import ProcessContext, ProcessWatcher


@pytest.fixture(scope="session")
def sandbox() -> str:
    """
    Use a running Sandbox as a fixture in a test. The yielded value is the string URL where the
    test sandbox can be found.

    If the DAZL_TEST_DAML_LEDGER_URL environment variable is specified, the Sandbox at that URL
    will be used instead of one spun up alongside the tests on a randomized port.
    """
    setup_default_logger(logging.DEBUG)

    external_ledger_url = os.getenv('DAZL_TEST_DAML_LEDGER_URL')
    if external_ledger_url is None:
        port = find_free_port()
        with ProcessWatcher(ProcessContext(args=f'daml sandbox --port {port}'.split(' '))):
            yield f'http://localhost:{port}'
    else:
        yield external_ledger_url


@pytest.fixture(scope="session")
def dar_fixtures() -> 'Mapping[str, DarFixture]':
    """
    Mapping of well-known DAR names to absolute paths for those files.
    """
    dars = {}

    archives_dir = Path(__file__).absolute().parent.parent.parent / '_fixtures' / 'archives'
    for child in archives_dir.iterdir():
        test_dar = child / 'Test.dar'
        if test_dar.exists() and child.name == '0.13.38':
            dars[child.name] = DarFixture(child.name, test_dar)

    if not dars:
        raise AssertionError('Could not find any Test.dar files in the fixtures folder')

    return dars


class DarFixture:
    """
    A test DAR.

    DAR parsing can take several seconds, so we cache instances of them between test runs.
    """
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self._dar_file = None
        self._store = None
        self._lock = RLock()

    @property
    def dar_file(self) -> 'DarFile':
        """
        A lazy-loaded instance of a :class:`DarFile` corresponding to the specified Path.
        """
        self._ensure_loaded()
        return self._dar_file

    @property
    def store(self) -> 'PackageStore':
        """
        A lazy-loaded instance of a :class:`PackageStore` corresponding to the specified Path.
        """
        self._ensure_loaded()
        return self._store

    def get_template_type(self, identifier: str) -> 'TypeReference':
        templates = self.store.resolve_template(identifier)
        for template in templates:
            return template.data_type.name

        raise AssertionError(f'Unknown template name: {identifier!r}')

    def _ensure_loaded(self):
        if self._dar_file is None:
            with self._lock:
                if self._dar_file is None:
                    logging.info('Reading metadata for SDK test package %s', self.name)
                    self._dar_file = DarFile(self.path)
                    self._dar_file.get_package_provider()
                    self._store = self._dar_file.read_metadata()
                    logging.info('Finished reading metadata for SDK test package %s', self.name)
