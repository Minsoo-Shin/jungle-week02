# 다익스트라 알고리즘 구현하기

import sys
import heapq

# 노드와 간선의 갯수를 받는다
n ,m = map(int, input().split())
# 시작 노드를 받는다. 
start = int(input())
# 노드와 간선에 대한 정보를 바탕으로 graph를 만든다.
graph = [[] for i in range(n+1)]

for i in range(n+1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
# 최단 거리 테이블을 초기화 한다. 
distance = [[] for i in range(n+1)]
# 다익스트라를 구현한다. 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리와 첫 노드를 넣어준다. 
    while q:
        dist, now = heapq.heappop(q) # 거리가 최소인 노드를 알려준다. 
        if distance[now] < dist: # 방문한 노드인지를 판별하기 위해서 distance table이 갱신되었는지를 판별한다. 
            continue
        for i in graph[now]: # 현재 노드와 인접한 노드들을 확인
            cost = dist + i[0]
            if cost <= distance[i[1]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
                distance = cost
                heapq.heappush(q, (cost, i[0])) 
