import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
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
        if visited[u]:
            continue
        else:
            visited[u] = True
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                pq.put(Node(v.id, dist[v.id]))
                path[v.id] = u

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    graph = [[] for _ in range(1000)]
    dist = [INF for _ in range(1000)]
    path = [-1 for _ in range(1000)]
    visited = [False for _ in range(1000)]
    for _ in range(n):
        a, b, w = map(int, input().split())
        graph[a].append(Node(b, w))
        graph[b].append(Node(a, w))
    u = int(input())
    Dijkstra(u)
    q = int(input())
    for _ in range(q):
        v = int(input())
        if not visited[v]:
            print("NO PATH")
        else:
            print(dist[v])