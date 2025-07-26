class TimeMap():
    def __init__(self):
        self.store = {}

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.store:
            return result

        arr = self.store[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            t, v = arr[mid]

            if t < timestamp:
                l = mid + 1
                result = v
            elif t > timestamp:
                r = mid - 1
            else:
                result = v
                break

        return result

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        arr = self.store[key]
        arr.append((timestamp, value))


t = TimeMap()
t.set("love", "high", 10)
t.set("love", "low", 20)
t.get("love", 5)
t.get("love", 10)
t.get("love", 15)
t.get("love", 20)
t.get("love", 25)
