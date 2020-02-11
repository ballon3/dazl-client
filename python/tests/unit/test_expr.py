# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from dazl.util.dar import DarFile


@pytest.mark.skip('This API does not really work yet, nor is it finalized')
def test_calculate_signatories(self):
    with DarFile(Pending) as dar:
        store = dar.read_metadata()
        template = next(iter(store.resolve_template('Pending.Counter')))
        actual = template.signatories(store, {'owner': 'Mommy', 'value': 0})
        self.assertEqual(['Mommy'], actual)
