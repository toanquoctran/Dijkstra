import queue

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                pq.put(Node(v.id, dist[v.id]))

if __name__ == "__main__":
    INF = int(1e9)
    graph = [[] for _ in range(100001)]
    dist = [INF for _ in range(100001)]
    visited = [False for _ in range(100001)]
    n = int(input())
    e = int(input())
    t = int(input())
    m = int(input())
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[b].append(Node(a, w))
    Dijkstra(e)
    count = 0
    for i in range(1, n + 1):
        if dist[i] <= t:
            count += 1
    print(count)