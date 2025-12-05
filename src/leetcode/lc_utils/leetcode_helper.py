# python
import json
import re
import collections
from typing import List, Optional

# ==========================================
# 基础数据结构定义 (对应 TreeNode.java / ListNode.java)
# ==========================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # 方便打印调试，覆盖默认的 object 打印
        return f"ListNode({self.val})"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# ==========================================
# 辅助转换方法 (对应 LeetCodeHelper.java)
# ==========================================

class LeetCodeHelper:

    @staticmethod
    def string_to_integer(input_str):
        return int(input_str)

    @staticmethod
    def string_to_integer_array(input_str):
        """将 "[1,2,3]" 转换为 [1, 2, 3]"""
        return json.loads(input_str)

    @staticmethod
    def string_to_2d_integer_array(input_str):
        """将 "[[1,2],[3,4]]" 转换为 [[1, 2], [3, 4]]"""
        return json.loads(input_str)

    @staticmethod
    def string_to_char_array(input_str):
        """将 "[\"a\",\"b\"]" 转换为 ["a", "b"]"""
        return json.loads(input_str)

    @staticmethod
    def string_to_list_node(input_str):
        """将 "[1,2,3]" 转换为 1->2->3"""
        # 使用 json 库直接解析数组字符串
        nums = json.loads(input_str)
        if not nums:
            return None

        dummy = ListNode(0)
        curr = dummy
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    @staticmethod
    def list_node_to_string(node):
        """将链表转换为 "[1, 2, 3]" 格式字符串"""
        if not node:
            return "[]"
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return json.dumps(result)

    @staticmethod
    def string_to_tree_node(input_str):
        """将 "[1,null,2,3]" 转换为二叉树对象"""
        input_str = input_str.strip()
        if not input_str or input_str == "[]":
            return None

        # 1. 解析字符串为列表，注意处理 null
        # LeetCode 的输入通常是 json 格式，但在 python 中 null 是 None
        # 如果输入是 raw string "[1, null, 2]"，json.loads 会报错，需替换 null -> null (JSON标准)
        # 或者如果是 Python 风格 "[1, None, 2]"
        # 简单起见，我们假设输入是标准的 JSON 格式 (LeetCode 复制出来的都是标准 JSON)
        try:
            values = json.loads(input_str)
        except:
            # 容错：如果不是标准JSON，可能是 Python list string
            return None

        if not values:
            return None

        root = TreeNode(values[0])
        queue = collections.deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 处理左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # 处理右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    @staticmethod
    def tree_node_to_string(root):
        """将二叉树对象转换为 "[1, null, 2, 3]" 格式"""
        if not root:
            return "[]"

        output = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                output.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                output.append(None)

        # 移除末尾多余的 None (null)
        while output and output[-1] is None:
            output.pop()

        return json.dumps(output).replace("null", "null")  # JSON 标准输出

    @staticmethod
    def pretty_print(val):
        """通用打印方法"""
        print(val)