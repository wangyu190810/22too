# python在个人工作中的应用

本来没想写这些的东西，有网友提出了这个问题，所以就简单描述一下python在各种工作中的应用。

[提问思考原文链接](https://github.com/program-in-chinese/overview/issues/20#issuecomment-338254716)

###  接触python原因

[之前简单说明过自己什么选择计算机，选择python](http://www.22too.com/blog/study_python_web_chapter_1)

学习python的时候，最大的动力，就是我很容易写出了一个软件。这样的动力不断的让我觉得编程很简单，
只要自己有好的思路，自己就能使用python快速的实现。

###  python在生活中的应用


####  爬虫和数据处理

通俗来讲就是将一个网站上的页面保存下来，比如很久以前喜欢看煎蛋的无聊图[连接](https://jandan.net/pic),有时候没时间看，
又会错过比较好看的图片，好在煎蛋比较有趣的图片，大家都会点赞。所以只要每天下载安点赞最高的图片，就能保证不错过好看的图片。

程序实现思路：

* 每天晚上12点定时去查看图片点赞比较高的图片
* 下载点赞较高的图片

当然我们还见过特别无耻的行为， 比如把某些网站的图片，直接使用爬虫抓取图片连接，然后将连接发布到自己的网站，我们称之为盗链,
网站的流量还是比较贵的，这样的行为会遭受很大的损失。



在工作中，经常会有一些爬虫任务，当年毕业时候，毕业设计是《抓取拉钩网的招聘职位并且分析招聘数据》


#### 数据分析

当然我们经常经常也会看到，很多帖子:

[我用Python分析了42万字的歌词，为了搞清楚民谣歌手们在唱些什么](https://zhuanlan.zhihu.com/p/25430454)

[我用Python做了六百万字的歌词分析，告诉你中国Rapper都在唱些啥](http://wemedia.ifeng.com/25046178/wemedia.shtml)

分析股票相关信息

之前在微博上，看到有一个博士在搞美股投资，为了测试新浪股票能不能买入，在完全不看新浪财报的情况下，分析新浪微博的发展趋势。

分析方式：
* 每天多个时段，去抓取新浪首页的最热微博
* 将评论数量，点赞数量，转发数量进行记录
* 将数据整理之后，做成统计图，可以看到新浪微博在几个月之内数据活跃性在不断上升。
* 决定买入新浪股票

当然上述方式，需要抓取数据，需要存储数据，需要做成图表。
使用python全部解决，并且不需要过多的计算机知识，你只要知道怎么抓取数据，怎么存储数据，怎么做成图表。
当然别的编程语言，也可以做到。


####  数据展示

折现图，还是饼状图，二维图片，还是三维图。

python写起来都很简单。

并且因为不需要编译，所以加上我们更改了数据，马上再次运行。就能看到更改之后的展示，极大的提高了纠错的效率。

以上三点，不需要太多的计算机知识，就可以做出你想要东西，并且可以完全说和计算机没什么关系，就是采集数据和统计数据。


### 谋生技能

####  web开发

当上免的各种数据抓取、分析结束之后，我们需要展示，这个时候，可以使用python的开发web来展示。同样，也可以不用。web知识过多，
非专业人员，只要做好数据分析就行。

####  游戏开发

最初自己写的一个游戏是使用python的模块，pygame做的游戏，很简单的贪吃蛇。但是我开心了好多天。因为很简单就完成了。成就感特别足。

#### linux服务器处理

现在运维已经大多数必备python技能了，当然他们还是以linux shell技能为主。

#### 大数据开发

都是噱头，没啥好看的，或者好说的。用什么语言都差不多。

