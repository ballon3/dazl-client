# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Mapping

from dazl import CreateCommand, ExerciseCommand, CreateAndExerciseCommand, ExerciseByKeyCommand, \
    ContractId
from dazl.protocols.v1.pb_ser_command import ProtobufSerializer
from dazl.protocols.v1 import model as G


def get_identifier(dar_fixture, identifier: str) -> 'Mapping[str, str]':
    tref = dar_fixture.get_template_type(identifier)
    return G.Identifier(
        module_name='.'.join(tref.module.module_name),
        entity_name='.'.join(tref.name),
        package_id=tref.module.package_id)


def test_serialize_create(subtests, dar_fixtures):
    for dar_fixture in dar_fixtures.values():
        with subtests.test(name=dar_fixture.name):
            sut = ProtobufSerializer(dar_fixture.store)

            command = CreateCommand('Account.AccountRequest', dict(owner='SomeParty'))

            expected = G.Command()
            expected.create.template_id.MergeFrom(
                get_identifier(dar_fixture, 'Account.AccountRequest'))
            expected.create.create_arguments.fields.append(
                G.RecordField(label='owner', value=G.Value(party='SomeParty')))
            actual = sut.serialize_command(command)

            assert expected == actual


def test_serialize_exercise(subtests, dar_fixtures):
    for dar_fixture in dar_fixtures.values():
        with subtests.test(name=dar_fixture.name):
            sut = ProtobufSerializer(dar_fixture.store)

            tref = dar_fixture.get_template_type('Account.AccountRequest')
            cid = ContractId('#1:0', tref)
            command = ExerciseCommand(cid, 'CreateAccount', dict(accountId=42))

            expected = G.Command()
            expected.exercise.contract_id = '#1:0'
            expected.exercise.template_id.MergeFrom(
                get_identifier(dar_fixture, 'Account.AccountRequest'))
            expected.exercise.choice = 'CreateAccount'
            expected.exercise.choice_argument.record.fields.append(
                G.RecordField(label='accountId', value=G.Value(int64=42)))
            actual = sut.serialize_command(command)

            assert expected == actual


def test_serialize_exercise_by_key(subtests, dar_fixtures):
    for dar_fixture in dar_fixtures.values():
        with subtests.test(name=dar_fixture.name):
            sut = ProtobufSerializer(dar_fixture.store)

            command = ExerciseByKeyCommand('Account.Counter', 'SomeParty', 'Increment', {})

            expected = G.Command()
            expected.exerciseByKey.template_id.MergeFrom(
                get_identifier(dar_fixture, 'Account.Counter'))
            expected.exerciseByKey.contract_key.party = 'SomeParty'
            expected.exerciseByKey.choice = 'Increment'
            expected.exerciseByKey.choice_argument.record.SetInParent()
            actual = sut.serialize_command(command)

            assert expected == actual


def test_serialize_create_and_exercise(subtests, dar_fixtures):
    for dar_fixture in dar_fixtures.values():
        with subtests.test(name=dar_fixture.name):
            sut = ProtobufSerializer(dar_fixture.store)

            command = CreateAndExerciseCommand(
                'Account.AccountRequest', dict(owner='SomeParty'), 'CreateAccount', dict(accountId=42))

            expected = G.Command()
            expected.createAndExercise.template_id.MergeFrom(
                get_identifier(dar_fixture, 'Account.AccountRequest'))
            expected.createAndExercise.create_arguments.fields.append(
                G.RecordField(label='owner', value=G.Value(party='SomeParty')))
            expected.createAndExercise.choice = 'CreateAccount'
            expected.createAndExercise.choice_argument.record.fields.append(
                G.RecordField(label='accountId', value=G.Value(int64=42)))
            actual = sut.serialize_command(command)

            assert expected == actual
