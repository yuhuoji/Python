# Python

TempFilePath:
- windows `[Project Root]/src`
- macos ` [Project Root]/src`

Code FileName:

```
LC$!velocityTool.deleteWhitespace("${question.frontendQuestionId}${velocityTool.camelCaseName(${question.titleSlug})}")
```
eg: `LC1TwoSum.py`


Code Template:

```
"""
${question.frontendQuestionId} ${question.title}
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


${question.code}


if __name__ == '__main__':
    
    solution = Solution()
    
    pass
```