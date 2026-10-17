#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####



class Roomgraph:

    def __init__(self) -> None:
        self._graph: dict = dict()

    def add_connection(self, r1: int, r2: int) -> None:
        if r1 == r2:
            print("Can not connect room to self")
            return
        d: dict = self._graph
        if r1 not in d:
            d[r1] = list()
        if r2 not in d:
            d[r2] = list()
        if r1 in d[r2] or r2 in d[r1]:
            print("This connection already exists")
            return
        d[r1].append(r2)
        d[r2].append(r1)

    def del_connection(self, r1: int, r2: int) -> None:
        d: dict = self._graph
        if r1 not in d[r2] or r2 not in d[r1]:
            print("Connection does not exist")
        self._del_uid(r1, d[r2])
        self._del_uid(r2, d[r1])
        if len(d[r1]) < 1:
            del d[r1]
        if len(d[r2]) < 1:
            del d[r2]

    def del_r(self, r1: int) -> None:
        pass

    def is_connected(self, r1: int, r2: int) -> bool:
        d: dict = self._graph
        if r1 in d[r2] and r2 in d[r1]:
            return True
        else:
            return False

    def connections(self, r1: int) -> list[int]:
        d: dict = self._graph
        res: list = list()
        if r1 not in d or len(d[r1]) < 1:
            return res
        else:
            return d[r1]
    
    def _del_uid(self, uid: int, r: list[int]) -> None:
        if len(r) < 1:
            print(f"tried to remove a room uid from a graph list that was empty, uid {uid} from list {r}")
            return
        found: bool = False
        for i in range(len(r)):
            if r[i] == uid:
                found = True
                del r[i]
                break  
        if not found:
            print(f"The uid that was supposed to be removed does not exist in this list, uid {uid} from list {r}")



    def show_info(self) -> None:
        for key in self._graph.keys():
            print(f"Room {key} connects to: {self._graph[key]}")





def test() -> None:

    graph1: Roomgraph = Roomgraph()

    graph1.add_connection(1, 1)
    graph1.add_connection(1, 2)
    graph1.add_connection(3, 15)
    graph1.add_connection(3, 1)
    graph1.add_connection(3, 5)
    graph1.add_connection(4, 5)
    graph1.show_info()

    graph1.del_connection(5, 3)
    graph1.del_connection(1, 2)
    graph1.show_info()

    print(graph1.is_connected(2, 1))
    print(graph1.is_connected(3, 15))
    print(graph1.is_connected(1, 1))

    for i in range(1, 10):
        print(graph1.connections(i))




if __name__ == "__main__":
    test()

    