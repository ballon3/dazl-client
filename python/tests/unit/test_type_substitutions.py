# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.model.types import TypeReference, ModuleRef, dotted_name, RecordType, \
    NamedArgumentList, \
    ListType, TypeVariable, TypeApp, SCALAR_TYPE_TEXT, SCALAR_TYPE_INTEGER, \
    type_evaluate_dispatch_default_error, TypeEvaluationContext, TypeAdjective
from dazl.model.types_store import PackageStoreBuilder


def simple_type_ref(name) -> TypeReference:
    return TypeReference(module=ModuleRef('pkg0', ()), name=dotted_name(name))


def record_type(name: TypeReference, type_args, **fields):
    return RecordType(
        named_args=NamedArgumentList((k, v) for k, v in fields.items()),
        name=name,
        type_args=tuple(map(TypeVariable, type_args)),
        adjective=TypeAdjective.USER_DEFINED)


def list_type(tt):
    return ListType(tt)


def type_var(name):
    return TypeVariable(name)


def test_simple_translate():
    tr = simple_type_ref('Map')
    tt = simple_type_ref('Tuple')

    tuple_type = record_type(tt, 'AB', _1=type_var('A'), _2=type_var('B'))
    map_type = record_type(tr, 'KV', _1=list_type(TypeApp(tt, (type_var('K'), type_var('V')))))

    psb = PackageStoreBuilder()
    psb.add_type(tuple_type.name, tuple_type)
    psb.add_type(map_type.name, map_type)

    test_case_type = TypeApp(tr, (SCALAR_TYPE_INTEGER, SCALAR_TYPE_TEXT))

    def _1(context, actual: RecordType):
        assert 1 == len(actual.named_args)
        type_evaluate_dispatch_default_error(on_list=_2)(context, actual.named_args[0][1])

    def _2(context, inner_list_type: ListType):
        type_evaluate_dispatch_default_error(on_record=_3)(context, inner_list_type.type_parameter)

    def _3(context, inner_tuple_type: RecordType):
        type_evaluate_dispatch_default_error(on_scalar=_4)(context, inner_tuple_type.named_args[0][1])
        type_evaluate_dispatch_default_error(on_scalar=_5)(context, inner_tuple_type.named_args[1][1])

    def _4(context, first_param):
        assert first_param == SCALAR_TYPE_INTEGER

    def _5(context, second_param):
        assert second_param == SCALAR_TYPE_TEXT

    type_evaluate_dispatch_default_error(on_record=_1)(
        TypeEvaluationContext.from_store(psb.build()), test_case_type)
