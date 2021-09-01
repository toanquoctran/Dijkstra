import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, e):
    dist = [INF for _ in range(200001)]
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        if u == e:
            return dist[e]
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                pq.put(Node(v.id, dist[v.id]))
    return dist[e]

if __name__ == "__main__":
    INF = int(1e9)
    s = int(input())
    for _ in range(s):
        graph = [[] for _ in range(200001)]
        n = int(input())
        cities = {}
        for i in range(n):
            name = input()
            cities[name] = i
            p = int(input())
            for _ in range(p):
                nr, cost = map(int, input().split())
                graph[i].append(Node(nr - 1, cost))
        r = int(input())
        for _ in range(r):
            name1, name2 = input().split()
            u = cities[name1]
            v = cities[name2]
            ans = Dijkstra(u, v)
            print(ans)
        input()