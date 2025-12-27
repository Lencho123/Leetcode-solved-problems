"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(Employee)
        for node in employees:
            _id = node.id
            graph[_id] = node
            
        
        visited = set()
        
        def dfs(_id):
            
            if not graph[_id].subordinates:
                return graph[_id].importance
            
            temp = graph[_id].importance
            
            for nei_id in graph[_id].subordinates:
                temp+=dfs(nei_id)
            return temp
        
        return dfs(id)
            