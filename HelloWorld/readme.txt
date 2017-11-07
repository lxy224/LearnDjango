    url 函数 可以接受四个参数
regex和view两个必须选参数  kwargs和name两个可选参数

regex：正则表达式，与之匹配的URL会执行第二个view参数
view： 用于执行与正则表达式匹配的URL请求
kwargs：视图使用的字典类型的参数
name： 用来反向获取URL