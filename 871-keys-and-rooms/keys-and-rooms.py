class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()

        def dfs(room_idx):
            visited.add(room_idx)
            for key in rooms[room_idx]:
                if key not in visited:
                    dfs(key)

      
        dfs(0)

        return len(visited) == len(rooms)