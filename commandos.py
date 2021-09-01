import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijsktra(s):
    dist = [INF for _ in range(99999)]
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
    return dist

if __name__ == "__main__":
    INF = int(1e9)
    t = int(input())
    for i in range(t):
        graph = [[] for _ in range(99999)]
        n = int(input())
        r = int(input())
        for _ in range(r):
            u, v = map(int, input().split())
            graph[u].append(Node(v, 1))
            graph[v].append(Node(u, 1))
        s, d = map(int, input().split())
        dist1 = Dijsktra(s)
        dist2 = Dijsktra(d)
        res = 0
        for j in range(n):
            temp = dist1[j] + dist2[j]
            res = max(res, temp)
        print("Case {}: {}".format(i + 1, res))