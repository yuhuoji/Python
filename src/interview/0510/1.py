class Solution:
    def solve(self, N: int, S: str, K: int) -> int:
        """
        :param N: 服务器节点数量
        :param S: 长度为 N 的 01 字符串
        :param K: 最大传播轮数，-1 表示无限制
        :return: 最少初始接收消息的服务器数量
        """

        one_blocks = []  # 记录每段连续 1 的起点、终点和长度

        pos = 0
        while pos < N:
            if S[pos] == '0':
                pos += 1
                continue

            start = pos
            while pos < N and S[pos] == '1':
                pos += 1

            end = pos - 1
            block_size = end - start + 1
            one_blocks.append((start, end, block_size))

        if not one_blocks:
            return 0

        if K == -1:
            allowed_round = N
        else:
            allowed_round = K

        for start, end, block_size in one_blocks:
            left_blocked = start > 0
            right_blocked = end < N - 1

            if left_blocked and right_blocked:
                round_limit = (block_size - 1) // 2
            elif left_blocked or right_blocked:
                round_limit = block_size - 1
            else:
                round_limit = N

            allowed_round = min(allowed_round, round_limit)

        single_source_cover = 2 * allowed_round + 1

        result = 0
        for _, _, block_size in one_blocks:
            result += (block_size + single_source_cover - 1) // single_source_cover

        return result


if __name__ == '__main__':
    sol = Solution()

    print(sol.solve(5, "11111", -1))
    # 输出：1

    print(sol.solve(6, "110011", -1))
    # 输出：2

    print(sol.solve(7, "1111111", 2))
    # 输出：2