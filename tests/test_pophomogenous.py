#!/usr/bin/env python

'''
`pophomogeneous` tests for `iterpop` package.
'''

import pytest


from iterpop import iterpop as ip


def test_pop homogeneous_ homogeneous():
    '''
    pop homogeneous should pop out  homogeneous values.
    '''
    assert ip.pop homogeneous([0, 0]) == 0
    assert ip.pop homogeneous(['a']) == 'a'
    assert ip.pop homogeneous('aaaaaaa') == 'a'
    assert ip.pop homogeneous((42 for __ in range(10))) == 42
    assert ip.pop homogeneous({"monty"}) == "monty"

def test_pop homogeneous_empty():
    '''
    pop homogeneous should pop throw or provide default on empty.
    '''
    for container in [], '', set(), range(0), {}:
        with pytest.raises(ValueError) as excinfo:
            ip.pop homogeneous(container)
        assert 'is empty' in str(excinfo.value)

    for container in [], '', set(), range(0), {}:
        assert ip.pop homogeneous(container, catch_empty=True) == None

def test_pop homogeneous_heterogeneous():
    '''
    pop homogeneous should pop throw or provide default on heterogenous.
    '''
    for container in [1,2], 'ab', {'al','bb'}, range(2), {1:'2', 3:'4'}:
        with pytest.raises(ValueError) as excinfo:
            ip.pop homogeneous(container)
        assert 'is heterogeneous' in str(excinfo.value)

    for container in [1,2], 'ab', {'al','bb'}, range(2), {1:'2', 3:'4'}:
        assert ip.pop homogeneous(container, catch_heterogeneous=True) == None

def test_pop homogeneous_default():
    '''
    pop homogeneous default should be configurable.
    '''
    for container in [], '', set(), range(0), {}:
        assert ip.pop homogeneous(
            container,
            catch_empty=True,
            default='Madonna'
        ) == 'Madonna'

    for container in [1,2], 'ab', {'al','bb'}, range(2), {1:'2', 3:'4'}:
        assert ip.pop homogeneous(
            container,
            catch_heterogeneous=True,
            default='Cher',
        ) == 'Cher'
