
## 目录结构

```
├─autorunx.egg-info  # python setup.py sdist
├─build  # python setup.py bdist_wheel
│  ├─bdist.win-amd64
│  └─lib
│      └─lib
│          ├─dataio
│          ├─dataprocess
│          ├─flowcontrol
│          ├─flowfunction
│          └─system
├─cli
│  └─lib
│      └─...
├─dist  # python setup.py sdist, python setup.py bdist_wheel
├─doc
│  ├─config
│  │  ├─xxx.json
│  │  └─...
│  ├─dataio
│  │  ├─dtio-i-bool
│  │  |  ├─config.json  # configuration file
│  │  |  └─dtio-i-bool.md  # instruction readme text
│  │  └─...
│  ├─dataprocess
│  │  ├─dtpc-abs
│  │  |  ├─config.json
│  │  |  └─dtpc-abs.md
│  │  └─...
│  ├─flowcontrol
│  │  ├─ctrl-for
│  │  |  ├─config.json
│  │  |  └─ctrl-for.md
│  │  └─...
│  ├─flowfunction
│  │  ├─func-test-xxxx
│  │  |  ├─config.json
│  │  |  └─func-test-xxxx.md
│  │  └─...
│  │  
│  └─system   # system lib
│      ├─aop
│      ├─data_center
│      ├─log
│      ├─node_center
│      └─...
├─lib
│  ├─dataio
│  │  └─dtio-i-string.py
│  │  └─...
│  ├─dataprocess
│  │  └─dtpc-subtract.py
│  │  └─...
│  ├─flowcontrol
│  │  └─ctrl-start.py
│  │  └─...
│  ├─flowfunction
│  │  └─func-test-xxxxx.py
│  │  └─...
│  └─system
│      └─...
├─log
├─test
│  ├─common
│  └─lib
│      ├─flowcontrol
│      └─system
|      └─...
├─autorunx.py
├─globals.py  # import global file
├─setup.py
|
```

**Notice**: 按照相关规律进行命名，确保`lib`中模块名唯一。


## 关键字&保留字

- .
- autorunx
- arx
- input
- output
- ctrl
- func
- dataio
- dataprocess
- dtpc
- dtio
- node
- data
- globals
- ...






### 其他

**基本图形**

- 起止框
- 处理框
- 流程线
- 判断框
- 输入输出框


**基本结构**

- 顺序结构
- 选择结构
- 循环结构

















