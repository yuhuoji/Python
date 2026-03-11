"""
华为
"""

import math
import sys

"""input
3
50 25 30
60 15 60 
25 75 90
3
9
50 25 30
30 50 30
60 15 60
25 75 90
100 5 60
26 15 30
32 67.5 90
80 7.5 60 
20 100 90
"""

"""output
35.33 30.00 30.00
80.00 9.17 60.00
25.67 80.83 90.00
"""


def main():
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    ptr = 0

    k = int(lines[ptr])
    ptr += 1

    centers = []
    for _ in range(k):
        x, y, z = map(float, lines[ptr].split())
        centers.append([x, y, z])
        ptr += 1

    iter_num = int(lines[ptr])
    ptr += 1

    m = int(lines[ptr])
    ptr += 1

    samples = []
    for _ in range(m):
        x, y, z = map(float, lines[ptr].split())
        samples.append([x, y, z])
        ptr += 1

    for _ in range(iter_num):
        clusters = [[] for _ in range(k)]
        for sample in samples:
            min_dist = float('inf')
            best_cluster = 0
            for i in range(k):
                # 欧式距离
                dist = math.sqrt(
                    (sample[0] - centers[i][0]) ** 2 +
                    (sample[1] - centers[i][1]) ** 2 +
                    (sample[2] - centers[i][2]) ** 2
                )
                if dist < min_dist:
                    min_dist = dist
                    best_cluster = i
            clusters[best_cluster].append(sample)

        # 聚类中心
        for i in range(k):
            if not clusters[i]:
                # 无样本
                continue
            new_x = sum(s[0] for s in clusters[i]) / len(clusters[i])
            new_y = sum(s[1] for s in clusters[i]) / len(clusters[i])
            new_z = sum(s[2] for s in clusters[i]) / len(clusters[i])
            centers[i] = [new_x, new_y, new_z]

    for center in centers:
        print("{0:.2f} {1:.2f} {2:.2f}".format(center[0], center[1], center[2]))


if __name__ == "__main__":
    main()

    # print("\nMissing_1: 175.81\nMissing_2: 168.12\nMissing_3: 150.08\nMissing_4: 138.62\nMissing_5: 158.61\nMissing_6: 141.85\nMissing_7: 146.87\nMissing_8: 166.18\nMissing_9: 155.56\nMissing_10: 144.75\nMissing_11: 147.16\nMissing_12: 160.65\nMissing_13: 166.72\nMissing_14: 169.88\nMissing_15: 166.19\nMissing_16: 174.53\nMissing_17: 164.11\nMissing_18: 167.63\nMissing_19: 181.34\nMissing_20: 182.15    ")
    #
    # print("Missing_1: 175.81\nMissing_2: 168.12")
