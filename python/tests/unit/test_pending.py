# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import sandbox, create, exercise, Network

PARTY = 'Operator'
Counter = 'Pending.Counter'
Account = 'Pending.Account'
AccountRequest = 'Pending.AccountRequest'

OperatorNotification = 'Simple.OperatorNotification'


def test_select_template_retrieves_contracts():
    number_of_contracts = 10

    with sandbox(Pending) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda _: [
            create(Counter, {'owner': PARTY, 'value': 0}),
            *[create(AccountRequest, {'owner': PARTY}) for i in range(number_of_contracts)],
        ])

        @party_client.ledger_created(AccountRequest)
        async def on_account_request(event):
            counter_cid, counter_cdata = await event.acs_find_one(Counter)
            return [
                exercise(event.cid, 'CreateAccount', dict(accountId=counter_cdata['value'])),
                exercise(counter_cid, 'Increment')
            ]

        network.run_until_complete()

        data = party_client.find_active(Account)

    assert len(data) == number_of_contracts
