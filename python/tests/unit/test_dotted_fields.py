# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import simple_client


def test_record_dotted_fields_submit(sandbox):
    with simple_client(url=sandbox, party='Test') as client:
        client.ready()
        client.submit_create('Address.American', {
            'person': 'Test',
            'address.address': '1 Test Place',
            'address.city': 'Somewhere',
            'address.state': 'ZZ',
            'address.zip': '99999'
        })
        print(client.find_active('DottedFields.American'))


def test_variant_dotted_fields_submit(sandbox):
    with simple_client(url=sandbox, party='Test') as client:
        client.ready()
        client.submit_create('Address.Person', {
            'person': 'Test',
            'address.US.address': '1 Test Place',
            'address.US.city': 'Somewhere',
            'address.US.state': 'ZZ',
            'address.US.zip': '99999',
            'address.UK.address': '',
            'address.UK.locality': '',
            'address.UK.city': '',
            'address.UK.state': '',
            'address.UK.postcode': '',

        })
        print(client.find_active('Address.Person'))
