# Python

TempFilePath:
- windows `[Project Root]/todo`
- macos ` [Project Root]/src`

Code FileName:

```
LC$!velocityTool.deleteWhitespace("${question.frontendQuestionId}${velocityTool.camelCaseName(${question.titleSlug})}")
```


Code Template:

```
"""
${question.frontendQuestionId} ${question.title}
"""
from typing import *
from src.leetcode.lc_utils import *


${question.code}


if __name__ == '__main__':
    
    solution = Solution()
    
    pass
```