import time
from typing import List

class Solution:
    def isRectangleCoverBrute(self, rectangles: List[List[int]]) -> bool:
        min_x = min(r[0] for r in rectangles)
        min_y = min(r[1] for r in rectangles)
        max_x = max(r[2] for r in rectangles)
        max_y = max(r[3] for r in rectangles)
        total_area = (max_x - min_x) * (max_y - min_y)
        covered = set()
        area_sum = 0
        for x1, y1, x2, y2 in rectangles:
            area_sum += (x2 - x1) * (y2 - y1)
            for x in range(x1, x2):
                for y in range(y1, y2):
                    if (x, y) in covered:
                        return False
                    covered.add((x, y))
        return area_sum == total_area and len(covered) == total_area

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        min_x = float("inf"); min_y = float("inf")
        max_x = float("-inf"); max_y = float("-inf")
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x = min(min_x, x1); min_y = min(min_y, y1)
            max_x = max(max_x, x2); max_y = max(max_y, y2)
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
        expected_area = (max_x - min_x) * (max_y - min_y)
        if area != expected_area:
            return False
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corners == expected_corners

sol = Solution()


print("Scenario: n stays tiny, but coordinate magnitude grows (mirrors real constraints)")
print(f"{'side length':<15}{'n (rects)':<12}{'brute (sec)':<15}{'optimized (sec)':<18}{'speedup'}")
print("-" * 75)

for side in [100, 300, 600, 1000, 1500]:

    half = side // 2
    rects = [
        [0, 0, half, half],
        [half, 0, side, half],
        [0, half, half, side],
        [half, half, side, side],
    ]
    n = len(rects)

    t0 = time.perf_counter()
    sol.isRectangleCoverBrute(rects)
    t1 = time.perf_counter()
    brute_time = t1 - t0

    t0 = time.perf_counter()
    sol.isRectangleCover(rects)
    t1 = time.perf_counter()
    opt_time = t1 - t0

    speedup = brute_time / opt_time if opt_time > 0 else float('inf')
    print(f"{side:<15}{n:<12}{brute_time:<15.6f}{opt_time:<18.8f}{speedup:.0f}x")

print("\nNote: n (rectangle count) stays fixed at 4 the whole time.")
print("Brute force time explodes because it scales with AREA (side^2), not n.")
print("Optimized time stays flat because it only scales with n.")
