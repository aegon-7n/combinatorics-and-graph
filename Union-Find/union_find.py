class UnionFind:
    def __init__(self, n):
        # Инициализируем родительский массив (каждый элемент сам для себя)
        self.parent = list(range(n))
        # Массив рангов (глубина деревьев)
        self.rank = [0] * n

    def find(self, x):
        # Реализация сжатия пути: если x не является корнем, то рекурсивно находим корень и сжимаем путь
        if self.parent[x] != x:
            # Рекурсивный вызов для поиска корня, при этом сжимаем путь
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Находим корни для обоих элементов
        rootX = self.find(x)
        rootY = self.find(y)

        # Если элементы уже в одном множестве, не нужно их объединять
        if rootX != rootY:
            # Объединяем два множества по рангу
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX  # Прикрепляем дерево меньшей глубины к дереву большего корня
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX  # Если ранги равны, делаем одно дерево корнем другого
                self.rank[rootX] += 1  # Увеличиваем ранг нового корня

    def connected(self, x, y):
        # Проверяем, принадлежат ли элементы x и y одному множеству
        return self.find(x) == self.find(y)


# Пример использования:
n = 10  # Количество элементов
uf = UnionFind(n)

# Объединяем элементы в группы
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)

# Проверка, принадлежат ли элементы к одному множеству
print(uf.connected(1, 3))  # True, потому что 1 и 3 в одном множестве
print(uf.connected(1, 4))  # False, потому что 1 и 4 в разных множествах

# Объединяем множества 1-3 и 4-5
uf.union(3, 4)

# Проверка после объединения
print(uf.connected(1, 5))  # True, теперь 1 и 5 в одном множестве
