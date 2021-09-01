import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, graph):
    dist = [INF for _ in range(n)]
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:
            continue
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                pq.put(Node(v.id, dist[v.id]))
    return dist

if __name__ == "__main__":
    INF = int(1e9)
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        graph = [[] for _ in range(n)]
        cost = [INF for _ in range(n)]
        graphS = [[] for _ in range(n)]
        graphD = [[] for _ in range(n)]
        costS = [INF for _ in range(n)]
        costD = [INF for _ in range(n)]
        s, d = map(int, input().split())
        for _ in range(m):
            u, v, p = map(int, input().split())
            graphS[u].append(Node(v, p))
            graphD[v].append(Node(u, p))
        costS = Dijkstra(s, graphS)
        costD = Dijkstra(d, graphD)
        minCost = costS[d]
        for u in range(n):
            for node in graphS[u]:
                v = node.id
                w = node.dist
                if costS[u] + w + costD[v] != minCost:
                    graph[u].append(Node(v, w))
        cost = Dijkstra(s, graph)
        if cost[d] == INF:
            print(-1)
        else:
            print(cost[d])