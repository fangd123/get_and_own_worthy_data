# 从中文互联网中获取并存储有用的数据

## 小宇宙 APP 的历史收听记录

### 工具

* 已root的安卓机
* HttpCanary

### 方法

1. 在安卓机上安装 `HttpCanary`
2. 依据文章 [HttpCanary 在 Android 11 上的使用 - 简单逆向分析](https://www.cnblogs.com/ercilan/p/14386362.html) 安装根证书
3. 开启`HttpCanary` 抓包功能
4. 打开`小宇宙`，进入`个人`->`收听历史`，向下滚动页面，直到滚不动为止
5. 关闭`HttpCanary` 抓包功能
6. 在`HttpCanary`的抓包结果页面，搜索`小宇宙`的历史收听记录的请求包
7. 保存历史收听记录的请求包到手机中
8. 开启手机FTP功能，将历史收听记录的请求包传输至电脑上
9. 对响应包进行解析，获取历史收听记录`json`串
10. 将`json`串转换为`excel`格式
11. 根据需要进行数据分析和保存

## 微信公众号文章

### 工具

* 微信公众号搜索导出助手
* HTML 转 Markdown 工具（需要安装PHP以及Composer）
* Markdown 整理优化工具 （需要安装Python）

### 方法

1. 下载 [微信公众号搜索导出助手](https://www.weixinzg.cn/) 并付费
2. 根据 [号内采集自动抓取公众号所有历史文章图文教程](https://www.weixinzg.cn/article/12.html) 找到对应公众号的历史文章链接
3. 使用 `微信公众号搜索导出助手` 采集并导出文章为`html`格式
4. 使用 `HTML 转 Markdown 工具` 将采集的文章转换为 Markdown 格式
5. 使用 `Markdown 整理优化工具` 对 `Markdown` 格式进行整理