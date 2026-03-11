"""
常见的输入输出用法

"""

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
import sys
from typing import *
import math


class Solution:
    # 核心功能实现函数
    # def function(self) -> Optional[int]:
    # 核心功能实现：K-Means聚类（接收解析后的参数，处理业务逻辑）
    def function(self, k: int, centers: List[List[float]], iter_num: int, m: int, samples: List[List[float]]) -> List[
        List[float]]:
        """
        K-Means聚类核心逻辑
        :param k: 聚类中心数量
        :param centers: 初始聚类中心列表 [[x1,y1,z1], [x2,y2,z2], ...]
        :param iter_num: 迭代次数
        :param m: 样本数量
        :param samples: 样本列表 [[x1,y1,z1], [x2,y2,z2], ...]
        :return: 最终聚类中心列表
        """
        # 迭代更新聚类中心
        for _ in range(iter_num):
            # 初始化聚类容器：每个聚类对应一个空列表
            clusters = [[] for _ in range(k)]

            # 步骤1：分配样本到最近的聚类中心
            for sample in samples:
                min_dist = float('inf')
                best_cluster = 0
                for i in range(k):
                    # 计算欧式距离
                    dist = math.sqrt(
                        (sample[0] - centers[i][0]) ** 2 +
                        (sample[1] - centers[i][1]) ** 2 +
                        (sample[2] - centers[i][2]) ** 2
                    )
                    if dist < min_dist:
                        min_dist = dist
                        best_cluster = i
                clusters[best_cluster].append(sample)

            # 步骤2：更新聚类中心（取每个聚类的均值）
            for i in range(k):
                if not clusters[i]:  # 该聚类无样本，跳过更新
                    continue
                # 计算三维坐标的均值
                new_x = sum(s[0] for s in clusters[i]) / len(clusters[i])
                new_y = sum(s[1] for s in clusters[i]) / len(clusters[i])
                new_z = sum(s[2] for s in clusters[i]) / len(clusters[i])
                centers[i] = [new_x, new_y, new_z]

        # 返回最终聚类中心
        return centers

    # ACM风格：读取输入并调用numIslands
    def acm_function(self):
        lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]  # 关键ACM读取输入
        ptr = 0  # 指针控制读取位置

        # 步骤1：解析聚类中心数量k + 初始聚类中心
        k = int(lines[ptr])
        ptr += 1
        centers = []
        for _ in range(k):
            x, y, z = map(float, lines[ptr].split())
            centers.append([x, y, z])
            ptr += 1

        # 步骤2：解析迭代次数iter_num + 样本数量m
        iter_num = int(lines[ptr])
        ptr += 1
        m = int(lines[ptr])
        ptr += 1

        # 步骤3：解析样本数据
        samples = []
        for _ in range(m):
            x, y, z = map(float, lines[ptr].split())
            samples.append([x, y, z])
            ptr += 1

        # 步骤4：调用核心函数（参数传递）
        final_centers = self.function(k, centers, iter_num, m, samples)

        # 步骤5：按格式输出最终聚类中心（保留2位小数）
        for center in final_centers:
            print("{0:.2f} {1:.2f} {2:.2f}".format(center[0], center[1], center[2]))

        return final_centers


if __name__ == "__main__":
    solution = Solution()
    # print(solution.acm_function())
    ans = solution.acm_function()
