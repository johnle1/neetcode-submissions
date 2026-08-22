class Solution:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, strs: List[str]) -> str:
        key = tuple(strs)

        if key not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[key] = shortUrl
            self.decodeMap[shortUrl] = strs

        return self.encodeMap[key]

    def decode(self, s: str) -> List[str]:
        return self.decodeMap[s]