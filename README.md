# OpenGL Project
## Ye Wang



### data 2020-10

#### Ye Wang

learn openGL using python

* new idea:

>通过emample_9改写加入两个button, 然后开始利用matplotlib画图
此时从子窗口传入的数据直接就是运算好的一组值, 然后点击button开始画图
由于所有方式传入的都为点对, 所以画图可以独立存在

>此时传输数据的框架不变

* 丢弃原pyqt画图painter原因:
>由于painter缓存问题无法确切的刷新每一个数据同时是低级接口缓存的问题出现明显
>此时任然未解决,所以采用第一种方法

-----------------

故此时保留原文件,此时取新的文件来开展new idea,同时采用原idea的框架,虽然这是
一件令人失望的事情

> 由于问题已经解决，所以不存在缓冲区的问题。此时还是使用原框架在原来的painter（）
> 里面继续可以使用，同时使用Qtimer计时刷新



### data 2020-11-08

#### Jiahong Ma

* 加入了椭圆算法的实现

----------
### data 2020-11-09

#### Ye Wang

* 加入了圆形算法的实现

----------
### project：使用pyqt来实现四种算法（DDAline，BRESEHAMline，Circle，Ellipse）

* 文件位置：pyQT5_practice/project
* 运行文件：pyQT5_practice/project/init.py
* 需配置文件：pyQT5

