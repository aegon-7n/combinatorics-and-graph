import pytest
from bellman_ford import Graph  # Предположим, что код алгоритма Беллмана-Форда находится в файле bellman_ford.py


def test_empty_graph():
    """Тест для пустого графа (без рёбер)"""
    g = Graph(3)
    distances = g.bellman_ford(0)
    assert distances == [0, float("inf"),
                         float("inf")], "Кратчайшее расстояние должно быть бесконечным для всех вершин кроме источника."


def test_single_edge():
    """Тест для графа с одним ребром"""
    g = Graph(2)
    g.add_edge(0, 1, 5)
    distances = g.bellman_ford(0)
    assert distances == [0, 5], "Расстояние от 0 до 1 должно быть 5."


def test_graph_with_positive_and_negative_weights():
    """Тест для графа с положительными и отрицательными весами"""
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    distances = g.bellman_ford(0)
    assert distances == [0, -1, 2, -2, 1], "Рассчитайте кратчайшие расстояния от 0 до остальных вершин."


def test_negative_cycle():
    """Тест для графа с отрицательным циклом"""
    g = Graph(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 0, -1)
    distances = g.bellman_ford(0)
    assert distances is None, "Граф содержит отрицательный цикл, и результат должен быть None."


def test_disconnected_graph():
    """Тест для графа с не связанными вершинами"""
    g = Graph(4)
    g.add_edge(0, 1, 2)
    g.add_edge(2, 3, 3)
    distances = g.bellman_ford(0)
    assert distances == [0, 2, float("inf"),
                         float("inf")], "Для отсоединённой вершины должны быть расстояния бесконечными."


if __name__ == '__main__':
    pytest.main()
