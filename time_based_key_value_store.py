from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.stored_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stored_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.stored_map:
            record = self.stored_map[key]
            if record[0][0] > timestamp:
                return ""
            left, right = 0, len(record) - 1
            while left <= right:
                mid = (left + right) // 2
                if record[mid][0] == timestamp:
                    return record[mid][1]
                elif record[mid][0] > timestamp:
                    right = mid - 1
                else:
                    left = mid + 1
            return record[right][1]

        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)