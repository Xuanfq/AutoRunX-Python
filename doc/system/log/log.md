

## Introduce

log：日志，记录。

本框架中，用于记录日志。

可用于代码调试等。



## Method

### init()

**必须参数**


**可选参数**

- COMMON_LOG_FILE: common log文件, 所有的log都在该文件内。
- FUNC_LOG_FILE: lib/flowfunction/下的模块的日志都输出到该日志文件。


**用法**

模块初始化时调用
```python
init(COMMON_LOG_FILE="log/common.log",FUNC_LOG_FILE="log/func.log")
```


### comon_log()

**必须参数**
- msg: log信息


**可选参数**


**用法**

开发者不应调用该方法，应通过func_log()等方法触发，触发过程详见func_log()源码。



### func_log()

**必须参数**

- msg: log信息


**可选参数**

- second_log_file: 除FUNC_LOG_FILE外，日志消息也将被记录到这个文件。


**用法**
```python
func_log(msg="func test start...")
```



## Example Code

```python
# init
init(COMMON_LOG_FILE="log/common.log",FUNC_LOG_FILE="log/func.log")
```

```python
# func log
func_log(msg="func test start...")
```











