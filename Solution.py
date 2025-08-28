from collections import Counter
import heapq

class Solution(object):
    def partitionArray(self, nums, k):
        if len(nums) % k != 0:
            return False

        freq = Counter(nums)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        groups_needed = len(nums) // k

        for _ in range(groups_needed):
            used = []
            seen = set()
            while heap and len(used) < k:
                count, num = heapq.heappop(heap)
                if num in seen:
                    continue
                seen.add(num)
                used.append((count + 1, num))  # decrement count

            if len(used) < k:
                return False

            for count, num in used:
                if count != 0:
                    heapq.heappush(heap, (count, num))

        return True
