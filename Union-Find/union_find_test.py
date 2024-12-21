import pytest
from union_find import UnionFind


def test_initialization():
    uf = UnionFind(5)
    # Каждый элемент должен быть сам себе родителем
    for i in range(5):
        assert uf.find(i) == i

def test_union_and_find():
    uf = UnionFind(5)
    uf.union(1, 2)  # Объединяем 1 и 2
    assert uf.find(1) == uf.find(2)

    uf.union(3, 4)  # Объединяем 3 и 4
    assert uf.find(3) == uf.find(4)

    # Проверка, что 1 и 4 в разных множествах
    assert uf.find(1) != uf.find(3)

def test_multiple_unions():
    uf = UnionFind(5)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)

    # Проверяем, что все элементы от 1 до 4 в одном множестве
    assert uf.find(1) == uf.find(4)
    assert uf.find(2) == uf.find(4)
    assert uf.find(3) == uf.find(4)

def test_path_compression():
    uf = UnionFind(5)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)

    # Путь к корню для элемента 4 должен быть сжат, т.е. parent[2] должен указывать на корень
    uf.find(4)
    assert uf.parent[2] == uf.find(2)

def test_connected():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    # Проверка connected
    assert uf.connected(0, 2)  # 0 и 2 должны быть в одном множестве
    assert not uf.connected(0, 4)  # 0 и 4 должны быть в разных множествах
    assert uf.connected(3, 4)  # 3 и 4 должны быть в одном множестве

def test_disjoint_sets():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)

    # Проверка независимости множеств
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) == uf.find(3)
    assert uf.find(4) == uf.find(5)

    assert uf.find(0) != uf.find(2)
    assert uf.find(2) != uf.find(4)

# Запуск тестов
if __name__ == '__main__':
    pytest.main()
