# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import create, Network

SOME_PARTY = 'SomeParty'
PUBLISHER = 'Publisher'
ALL_PARTY = '000'
PrivateContract = 'Visibility.PrivateContract'
PublicContract = 'Visibility.PublicContract'


def test_some_party_receives_public_contract(sandbox, dar_fixtures):
    some_party_cids = []
    publisher_cids = []

    network = Network()
    network.set_config(url=sandbox, party_groups=[ALL_PARTY], dar_files=[dar_fixtures['0.13.38']])

    some_client = network.aio_party(SOME_PARTY)
    some_client.add_ledger_ready(lambda _: create(PrivateContract, {'someParty': SOME_PARTY}))

    publisher_client = network.aio_party(PUBLISHER)
    publisher_client.add_ledger_ready(lambda _: create(PublicContract, {'publisher': PUBLISHER, 'allParty': ALL_PARTY}))

    some_client.add_ledger_created(PublicContract, lambda e: some_party_cids.append(e.cid))
    some_client.add_ledger_created(PrivateContract, lambda e: some_party_cids.append(e.cid))

    publisher_client.add_ledger_created(PublicContract, lambda e: publisher_cids.append(e.cid))
    publisher_client.add_ledger_created(PrivateContract, lambda e: publisher_cids.append(e.cid))

    network.run_until_complete()

    logging.debug(f'got to the end with some_party contracts: {some_party_cids} and publisher contracts: {publisher_cids}')

    assert len(some_party_cids) == 2
    assert len(publisher_cids) == 1
