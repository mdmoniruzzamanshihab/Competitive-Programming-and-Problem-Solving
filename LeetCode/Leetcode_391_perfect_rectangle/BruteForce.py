class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
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