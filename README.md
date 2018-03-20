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
[完整代码](https://github.com/lzcdev/PythonLearning/blob/master/Python%E7%88%AC%E8%99%AB%E5%AD%A6%E4%B9%A0%E7%B3%BB%E5%88%97%E8%AF%BE%E7%A8%8B/qsbk_spider.py)
#### 目标：
抓取糗事百科热门段子，每按一次回车显示一个段子的发布者，年龄，点赞数，段子内容。

`糗事百科地址`[https://www.qiushibaike.com/hot/page/1]()

采用BeautifulSoup提取HTML中的内容，当然也可以用正则。





