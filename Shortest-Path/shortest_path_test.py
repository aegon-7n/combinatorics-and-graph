import pytest
from shortest_path import bfs_shortest_paths


# Тесты с использованием pytest

def test_simple_graph():
    graph_data = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
    assert result == expected_result


def test_isolated_vertices():
    graph_data = {
        0: [],
        1: [],
        2: []
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: float('inf'), 2: float('inf')}
    assert result == expected_result


def test_disconnected_components():
    graph_data = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: 1, 2: float('inf'), 3: float('inf')}
    assert result == expected_result


def test_single_vertex():
    graph_data = {
        0: []
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0}
    assert result == expected_result


def test_multiple_paths():
    graph_data = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: 1, 2: 1, 3: 2}
    assert result == expected_result


def test_long_chain():
    graph_data = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    assert result == expected_result


def test_complex_graph():
    graph_data = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2],
        5: [6],
        6: [5]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph_data, start_vertex)
    expected_result = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: float('inf'), 6: float('inf')}
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
