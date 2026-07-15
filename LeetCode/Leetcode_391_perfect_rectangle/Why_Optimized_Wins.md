# 391. Perfect Rectangle : Why the Optimized Solution Wins (Benchmarked)

This document exists to answer one question honestly: **why should the
corner-counting solution be used over brute force, and by how much?**
Every number below comes from an actual benchmark run, not an estimate.

---

## 1. The core difference in one line

| | Brute Force (Grid Simulation) | Optimized (Corner Counting) |
|---|---|---|
| Scales with | **Area** of bounding box | **n** = number of rectangles |
| Time Complexity | O((max_x−min_x) × (max_y−min_y)) | O(n) |
| Space Complexity | O(Area) | O(n) |

This is the entire reason one is "better." Brute force's cost depends on
how large the *coordinates* are. Optimized's cost depends only on how many
*rectangles* there are. LeetCode's constraint (`coords up to 10^5`) makes
that difference the deciding factor.

---

## 2. Proof by benchmark : coordinates grow, rectangle count stays fixed

I ran both solutions on the same input pattern: **exactly 4 rectangles**,
tiled into a perfect square, while making the square progressively larger
(mirroring what "large coordinates" actually means on LeetCode).

```
n (rectangle count) fixed at 4 the entire time.

side length    n     brute (sec)   optimized (sec)   speedup
100            4     0.003932      0.00002648         148x
300            4     0.096967      0.00004138         2,343x
600            4     0.466613      0.00004608         10,126x
1000           4     1.158539      0.00004266         27,155x
1500           4     2.076856      0.00004812         43,155x
```

**What this shows:** the input didn't get "harder" in the way that matters
to brute force's design (n stayed at 4) — only the coordinate *values* grew.
Yet brute force slowed down by over 500x (0.004s → 2.08s) while optimized
stayed flat at ~0.00004s the entire time. That gap is not a coincidence —
it's the direct, measurable consequence of O(Area) vs O(n).

Extrapolating to LeetCode's actual constraint (coordinates up to `10^5`,
i.e. side length ~200,000): brute force's runtime would be in the range of
**hours**, while optimized would still run in **well under a second**,
since its cost never depended on coordinate magnitude in the first place.

*(Benchmark script: `Benchmark_Coordinate_Scale.py`, included in this folder for reproducibility.)*

---

## 3. Proof by benchmark : rectangle count grows (unit-size grid)

For completeness, here's the case where `n` itself grows (using unit-size
rectangles, so Area ≈ n for brute force — its best-case scenario):

```
n (rects)   grid size   brute (sec)   optimized (sec)
25          5x5         0.000026      0.000177
100         10x10       0.000168      0.000133
400         20x20       0.000543      0.000405
1600        40x40       0.004954      0.001676
3600        60x60       0.002953      0.003796
```

**Why brute force looks "fine" here:** this is brute force's *most
forgiving* case — small unit rectangles mean Area ≈ n, so its O(Area) cost
temporarily behaves like O(n) too. This is precisely why relying on this
kind of test case to judge an algorithm is misleading — it hides the real
bottleneck. Section 2 above is the honest test, because it isolates the
one variable (coordinate magnitude) that actually breaks brute force under
LeetCode's real constraints.

---

## 4. Why this matters in a FAANG interview (not just for LeetCode's judge)

- Interviewers care less about "does it pass" and more about **whether you
  identified the correct bottleneck variable**. Here, the bottleneck isn't
  `n` — it's coordinate magnitude. Recognizing that is the actual signal
  they're testing for, not memorizing the corner-counting trick.
- The optimized solution demonstrates **turning a geometry problem into a
  hashing problem** (interior corners cancel in pairs) — a reusable pattern
  that shows up in other geometry/interval problems, not just this one.
- Being able to say *"brute force is O(Area) not O(n), and here's the
  measured 43,000x gap at scale"* — with actual numbers, not just Big-O
  notation — is a stronger interview answer than reciting complexity
  classes from memory.

---

## 5. Bottom line

The optimized solution isn't "better" as a vague claim — it's **provably,
measurably faster** on the exact class of input (large coordinates) that
this problem's constraints guarantee you'll encounter. Brute force isn't
wrong — it's a valid stepping stone to show you understand the naive
approach first — but it is not viable for `10^5`-scale coordinates, and the
benchmark above quantifies exactly why.
