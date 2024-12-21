from collections import deque


def bfs_shortest_paths(graph, start):
    """
    Алгоритм поиска кратчайших путей на графе с единичными длинами рёбер.

    :param graph: Словарь смежности графа {вершина: [сосед1, сосед2, ...]}
    :param start: Начальная вершина
    :return: Словарь расстояний от start до каждой вершины
    """
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph}  # Все расстояния бесконечность
    distances[start] = 0  # Расстояние до начальной вершины - 0
    queue = deque([start])  # Очередь для BFS

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):  # Если сосед ещё не был посещён
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


# Пример использования
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }
    start_vertex = 0
    result = bfs_shortest_paths(graph, start_vertex)
    print("Кратчайшие пути от вершины", start_vertex, ":", result)
