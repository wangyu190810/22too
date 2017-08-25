# python是否符合你的理想

### 符合人类语言习惯的代码

我们回顾上一章节提出的问题

比如如下逻辑:

卫生间是分男女： 如果是男人，那么就进入男厕，如果是女人那就进入女厕，如果不能判断性别，那就让不让进。

用简单的英文标识就是 if propel is man will in man toilet , if propel is woman with in woman toilet , if propel is not man 
or woman with not in toilet  

用python语言表示上面对的逻辑：
```python 
propel = input("输入性别:")
if propel is "man":
    print("will in man toilet")
elif propel is "woamn":
    print("will in woman toilet")
else:
    print("will not in every toilet")
```
使用伪代码说明一下:

    propel = 用户输入值
    如果 propel 是 "man":
        执行打印 “ will in man toilet”
    如果 propel 不是 "man" 而是 "woman":
        执行打印 “ will in woman toilet”
    如果 propel 既不是 "nam" 也不是 "woman"
        执行打印 "will not in every toilet"

是不是感觉代码就和伪代码一样清晰，只要自己逻辑是清晰的。那我们就能写好代码

### 使用python画图

```python 

# 使用matplotlib 库，画图
import matplotlib.pyplot as plt
# 定义坐标点
plt.plot([1,2,3,4], [1,4,9,16])
# 展示绘制图形
plt.show()

```
![折线图](http://tools.22too.com/static/upload/1503676899.png)

是不是和简单，当你需要更加复杂或者强大的功能时候，[请参看教程](http://matplotlib.org/users/pyplot_tutorial.html#controlling-line-properties)


### 同样其他有意思的都可以做

你想要什么，我们就去实现什么

