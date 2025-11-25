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

${question.code}

```