class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list) # key: string, value = [list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.store.get(key, [])

        # binary search
        left, right = 0 , len(value) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if value[mid][1] <= timestamp:
                res = value[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

            

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)