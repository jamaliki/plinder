# Copyright (c) 2024, Plinder Development Team
# Distributed under the terms of the Apache License 2.0
import pytest

from plinder.core import scores


def test_query_index(read_plinder_mount):
    df = scores.query_index(columns=["system_id"])
    assert len(df.index) == 10


def test_query_protein_similarity(read_plinder_mount):

    df = scores.query_protein_similarity(
        search_db="holo",
        filters=[
            ("metric", "==", "pocket_lddt"),
            ("similarity", ">=", 90),
        ]
    )
    assert df is not None
    assert len(df.index)


def test_query_protein_similarity_empty(read_plinder_mount):
    with pytest.raises(ValueError):
        scores.query_protein_similarity(
            search_db="holo",
            filters=[],
        )


def test_query_protein_similarity_removes_search_db(read_plinder_mount):
    df = scores.query_protein_similarity(
        search_db="holo",
        filters=[
            ("search_db", "==", "holo"),
            ("metric", "==", "pocket_lddt"),
            ("similarity", ">=", 90),
        ],
    )
    assert df is not None
    assert len(df.index)


def test_query_protein_similarity_raises(read_plinder_mount):
    with pytest.raises(ValueError):
        scores.query_protein_similarity(
            search_db="test",
            filters=[
                ("search_db", "==", "holo"),
                ("metric", "==", "pocket_lddt"),
                ("similarity", ">=", 90),
            ],
        )


def test_query_ligand_similarity(read_plinder_mount):

    df = scores.query_ligand_similarity(
        filters=[
            ("query_ligand_id", "<", "100"),
        ]
    )
    assert df is not None
    assert len(df.index)


def test_query_ligand_similarity_empty(read_plinder_mount):
    with pytest.raises(ValueError):
        scores.query_ligand_similarity(
            filters=[]
        )


def test_query_links(read_plinder_mount):
    system_id = "4dd7__1__1.A__1.B"
    df = scores.query_links(filters=[("query_system", "==", system_id)])
    assert len(df.index)
