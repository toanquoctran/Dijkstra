import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, t):
    dist = [INF for _ in range(20001)]
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:
            continue
        if u == t:
            break
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                pq.put(Node(v.id, dist[v.id]))
    return dist[t]

if __name__ == "__main__":
    q = int(input())
    INF = int(1e9)
    for i in range(q):
        graph = [[] for _ in range(20001)]
        n, m, s, t = map(int, input().split())
        for _ in range(m):
            s1, s2, w = map(int, input().split())
            graph[s1].append(Node(s2, w))
            graph[s2].append(Node(s1, w))
        res = Dijkstra(s, t)
        if res != INF:
            print("Case #{}: {}".format(i + 1, res))
        else:
            print("Case #{}: {}".format(i + 1, "unreachable"))