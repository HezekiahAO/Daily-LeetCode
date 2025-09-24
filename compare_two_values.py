class Solution:
    def compareVersion(self, version1: str, version2: str):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))

        for a, b in zip(v1, v2):
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0

sol = Solution()
print(sol.compareVersion('1.2', '1.11'))
print(sol.compareVersion('1.8', '1.4'))
print(sol.compareVersion('1.25478', '1.1333'))