class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0

        min_x = float("inf")
        min_y = float("inf")
        max_x = float("-inf")
        max_y = float("-inf")

        for x1, y1, x2, y2 in rectangles:

            area += (x2 - x1) * (y2 - y1)

            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        expected_area = (max_x - min_x) * (max_y - min_y)

        if area != expected_area:
            return False

        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return corners == expected_corners