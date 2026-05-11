from typing import List

class Solution:
    def solve(self, n: int, ops: List[List[int]]) -> int:
        max_correct = 0
        
        # 1. 枚举小球的5种初始可能位置 (1, 2, 3, 4, 5)
        for initial_pos in range(1, 6):
            current_pos = initial_pos
            current_correct = 0
            
            # 2. 模拟 N 次操作过程
            for a, b, g in ops:
                # 步骤一：交换杯子 (如果小球在 a 或 b 下面，则跟着转移)
                if current_pos == a:
                    current_pos = b
                elif current_pos == b:
                    current_pos = a
                
                # 步骤二：验证观众猜测
                if current_pos == g:
                    current_correct += 1
            
            # 3. 统计并更新所有初始可能性中的最大猜对次数
            max_correct = max(max_correct, current_correct)
            
        return max_correct

# ================= 测试入口 =================
if __name__ == "__main__":
    # 题目给定的测试用例
    # n: 操作次数
    # ops: 每次操作的列表，格式为 [交换杯子a, 交换杯子b, 观众猜测g]
    n = 3
    ops = [[1, 2, 1], [3, 4, 2], [2, 5, 2]]
    
    expected_output = 1
    
    # 实例化并调用
    solution = Solution()
    actual_output = solution.solve(n, ops)
    
    # 打印测试结果
    print("------- 测试开始 -------")
    print(f"输入数据: n = {n}, ops = {ops}")
    print(f"预期输出: {expected_output}")
    print(f"实际输出: {actual_output}")
    print("------------------------")
    
    if actual_output == expected_output:
        print("✅ 测试通过！(Test Passed)")
    else:
        print("❌ 测试失败！(Test Failed)")