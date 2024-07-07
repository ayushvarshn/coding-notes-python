
def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
      # create adjList
      adjList = {}
      for i in range(n):
          adjList[i] = []

      for i,edge in enumerate(edges):
          adjList.get(edge[0]).append( (succProb[i], edge[1] ) )
          adjList.get(edge[1]).append( (succProb[i], edge[0] ) )
      
      #dist array
      dist = [0] * n

      # create priority queue
      pq = [( -1,start_node)]
      dist[start_node] = 1

      while pq:

          _, node = heapq.heappop(pq)

          for w, neigh in adjList.get(node):
              if dist[neigh] < dist[node] * w:
                  dist[neigh] = dist[node] * w
                  heapq.heappush(pq, ( - dist[neigh], neigh))

      return dist[end_node] 
