class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []    # Список рёбер (u, v, вес)

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))  # Добавление рёбер в граф

    def bellman_ford(self, src):
        # Шаг 1: Инициализация всех расстояний как бесконечность
        distances = [float("inf")] * self.V
        distances[src] = 0

        # Шаг 2: Рассчитываем кратчайшие пути
        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Шаг 3: Проверка на наличие отрицательных циклов
        for u, v, weight in self.graph:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Граф содержит отрицательный цикл")
                return None

        return distances


# Пример использования
if __name__ == "__main__":
    # Создаём граф с 5 вершинами
    g = Graph(5)

    # Добавляем рёбра (u, v, вес)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # Получаем кратчайшие расстояния от вершины 0
    distances = g.bellman_ford(0)

    if distances is not None:
        print("Кратчайшие расстояния от источника 0:")
        for i in range(len(distances)):
            print(f"Вершина {i}: {distances[i]}")
