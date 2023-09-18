

## Introduce

engine：引擎。

本框架是一个程序流程图的执行框架，本框架定义了一套程序流程图，主由节点(node)和边(edge)组成。边主要用于链接节点，无实际代码需执行，一切代码都在节点中。

在lib中，除system目录外皆为节点目录，包含data和flow两大类节点，data包括dataio(数据输入输出，数据定义)以及dataprocess(数据处理)，flow包括flowcontrol(流程控制)以及flowfunction(流程功能)。data类节点是数据相关，无需介入流程控制，由算法进行扫描并执行数据处理。flow类节点是流程相关，控制程序执行流程按照程序流程图走，需进行流程控制。flowcontrol是流程走向控制的关键，一般不需要添加或修改该代码库。开发者一般需要修改的代码库是flowfunction。





## Method




## Example Code

```python
```
