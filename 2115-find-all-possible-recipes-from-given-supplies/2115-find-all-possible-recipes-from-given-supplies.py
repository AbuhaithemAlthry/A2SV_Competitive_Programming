class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                incoming[recipes[i]]+=1
        
        queue = deque()
        order = []
        
        for ingredient in supplies:
            queue.append(ingredient)
        
        while queue:
            course = queue.popleft()
            if course in recipes:
                order.append(course)
            
            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        return order