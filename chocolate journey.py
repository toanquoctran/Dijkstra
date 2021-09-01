import heapq

def Dijkstra(s):
    dist = [INF for _ in range(100001)]
    pq = [(0, s)]
    dist[s] = 0
    while len(pq) > 0:
        w, u = heapq.heappop(pq)
        if w > dist[u]:
            continue
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

if __name__ == "__main__":
    INF = int(1e9)
    graph = [[] for _ in range(100001)]
    n, m, k, x = map(int, input().split())
    chocolateCities = map(int, input().split())
    for _ in range(m):
        u, v, d = map(int, input().split())
        graph[u].append((d, v))
        graph[v].append((d, u))
    a, b = map(int, input().split())
    dist1 = Dijkstra(a)
    dist2 = Dijkstra(b)
    res = INF
    for city in chocolateCities:
        if dist2[city] < x:
            temp = dist1[city] + dist2[city]
            res = min(res, temp)
    if res == INF:
        print(-1)
    else:
        print(res)