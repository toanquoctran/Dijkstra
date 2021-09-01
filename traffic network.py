import queue

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(graph, start, dist):
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    dist[start] = 0
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
    ds = int(input())
    for _ in range(ds):
        distS = [INF for _ in range(100001)]
        distT = [INF for _ in range(100001)]
        graphS = [[] for _ in range(100001)]
        graphT = [[] for _ in range(100001)]
        n, m, k, s, t = map(int, input().split())
        for _ in range(m):
            d, c, l = map(int, input().split())
            graphS[d].append(Node(c, l))
            graphT[c].append(Node(d, l))
        distS = Dijkstra(graphS, s, distS)
        distT = Dijkstra(graphT, t, distT)
        minCost = distS[t]
        for _ in range(k):
            u, v, q = map(int, input().split())
            temp1 = distS[u] + q + distT[v]
            temp2 = distS[v] + q + distT[u]
            minCost = min(temp1, temp2, minCost)
        if minCost == INF:
            minCost = -1
        print(minCost)