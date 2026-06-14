from typing import *
from collections import deque

class Graph:
    
    def __init__(self):
        self.nodes: Dict[int, List] = {} 

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.nodes:
            self.nodes[src] = []
        if dst not in self.nodes:
            self.nodes[dst] = []
        
        self.nodes[src].append(dst)
    
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.nodes or dst not in self.nodes:
            return False
        
        self.nodes[src].remove(dst)
        
        return True 

    def hasPath(self, src: int, dst: int) -> bool:
        visited: Set[int] = set()
        queue: Deque = deque()
        
        queue.append(src)
        
        while queue:
            vertex = queue.popleft()
            if vertex == dst:
                return True
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            for nei in self.nodes[vertex]:
                if nei not in visited:
                    queue.append(nei)
                    
        return False