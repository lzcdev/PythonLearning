# PythonLearning
**记录学习Python过程中的一些知识**
## Python进阶
[https://www.imooc.com/learn/317](https://www.imooc.com/learn/317)
- 函数式编程(function.py)
- 模块(module.py)
- 面向对象编程(oop.py)
- 类的继承(inherit.py)
- 定制类(custom_class.py)

## Python爬虫学习系列课程
[http://wiki.jikexueyuan.com/project/python-crawler-guide/](http://wiki.jikexueyuan.com/project/python-crawler-guide/)
- urllib库的基本用法
- urllib库的高级用法
- URLError异常处理
- Cookie 的使用
- 正则表达式
- BeautifulSoup用法
## 爬取糗事百科段子
使用方式
本代码在`Python爬虫学习系列课程`文件夹里，即`qsbk_spider.py`
```
cd Python爬虫学习系列课程
python qsbk_spider.py
```
[完整代码](./Python爬虫学习系列课程/qsbk_spider.py)
#### 目标：
抓取糗事百科热门段子，每按一次回车显示一个段子的发布者，年龄，点赞数，段子内容。

`糗事百科地址`[https://www.qiushibaike.com/hot/page/1](https://www.qiushibaike.com/hot/page/1)

采用BeautifulSoup提取HTML中的内容，当然也可以用正则。

## 爬取百度贴吧帖子
使用方式
本代码在`Python爬虫学习系列课程`文件夹里，即`bdtb_spider.py`
```
cd Python爬虫学习系列课程
python bdtb_spider.py
```
[完整代码](./Python爬虫学习系列课程/bdtb_spider.py)
#### 目标：
替换URL可抓取百度贴吧任意帖子，将抓取的内容进行保存。

`要抓取的贴吧demo地址`[https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1](https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1)

继续练习BeautifulSoup提取HTML中的内容。
## 爬取淘宝MM信息（爬取图片失败，其他信息可以）
使用方式
本代码在`Python爬虫学习系列课程`文件夹里，即`tbmm_spider.py`
```
cd Python爬虫学习系列课程
python tbmm_spider.py
```
[完整代码](./Python爬虫学习系列课程/tbmm_spider.py)
#### 目标：
抓取淘宝 MM 的姓名，头像，年龄，地址等信息，把每一个MM的写真图片按照文件夹保存到本地(失败),熟悉文件保存的过程

`要抓取的demo地址`[https://mm.taobao.com/json/request_top_list.htm?page=1](https://mm.taobao.com/json/request_top_list.htm?page=1)

## 爬取猫眼电影Top100
使用方式
```
python maoyanmovie.py
```
[完整代码](./maoyanmovie.py)
#### 目标：
爬取猫眼电影Top100所有的电影，练习requests的使用，打印并保存进txt文件
`要抓取的地址`[http://maoyan.com/board/4?offset=0](http://maoyan.com/board/4?offset=0)
目前总共10页数据，每页10条。
```
spider = Spider()
spider.start()
```

## 爬取极客学院所有课程的封面图片
使用方式
```
python jkxy_course_img.py
```
[完整代码](./jkxy_course_img.py)
#### 目标：
爬取极客学院所有课程的封面图片，练习一下正则表达式的使用，练习文件夹以及文件的操作
`要抓取的地址`[http://www.jikexueyuan.com/course/?pageNum=1](http://www.jikexueyuan.com/course/?pageNum=1)
#### 分析
查看源码可发现目标标签为
```
<img src="https://a1.jikexueyuan.com/home/201803/14/111e/5aa8b685a69eb.jpg" class="lessonimg" title="AWS云计算数据搜索与分析--- Amazon Elasticsearch" alt="AWS云计算数据搜索与分析--- Amazon Elasticsearch">
```
则使用正则表达式<img src="(.*?)" class="lessonimg"可匹配。
目前总共97页数据，暂时爬取5页。若要爬取更多，修改页数即可。
```
spider = Spider()
spider.start(5)
```






