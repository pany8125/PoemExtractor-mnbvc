# PoemExtractor-mnbvc

## 项目描述

- 本项目目的是将诗歌清洗为MNBVC的标准文本格式
- 原文件和目标文件均为jsonl格式，每行对应一首诗歌，源格式和目标详细格式附后。

## 环境

1. 下载本项目
```
git clone PoemExtractor-mnbvc
```
2. 进入目录并安装依赖
```
cd PoemExtractor-mnbvc
pip install -r requirements.txt
```

## 用法

通过以下命令将FILE文件转化并输出到以`POEM`为名称的结果文件中。
```shell
python poem_extract.py FILE
```

以上命令将输出时间戳结果文件例子`POEM_2023-07-17-00-30-43.jsonl`。

## 代码说明

- `poem_extract.py` 入口程序

## 原始文件示例

```json
{"title": "吃方便面想的一些问题222", "author": "22200913", "content": "\n222方便面快速解决饥饿\n饥饿可以慢慢地减退\n方便面。。。"}
```

## 输出jsonl文件格式

```json
{
    "文件名": "chinese_poems.jsonl",
    "是否待查文件": False,
    "是否重复文件": False,
    "文件大小": 3333333333333, # 单位为字节
    "simhash": 0,
    "最长段落长度": 0,
    "段落数": 0,
    "去重段落数": 0,
    "低质量段落数": 0,
    "段落": [
        {
          '行号': 2,
          '是否重复': False,
          '是否跨文件重复': False,
          'md5': aabc, #整行json的md5
          '标题':"吃方便面想的一些问题222", # 对应title
          '作者': "22200913", # 对应author
          '内容': "\n222方便面快速解决饥饿\n饥饿可以慢慢地减退\n方便面。。。" # 对应content
        }
    ]
}
```

## 结果示例

```json
{
    "文件名": "chinese_poems.jsonl",
    "是否待查文件": False,
    "是否重复文件": False,
    "文件大小": 3333333333333,
    "simhash": 0,
    "最长段落长度": 0,
    "段落数": 0,
    "去重段落数": 0,
    "低质量段落数": 0,
    "段落": [
        {
          '行号': 2,
          '是否重复': False,
          '是否跨文件重复': False,
          'md5': [内容]文字的md5,
          '标题':"吃方便面想的一些问题222",
          '作者': "22200913",
          '内容': "\n222方便面快速解决饥饿\n饥饿可以慢慢地减退\n方便面。。。"
        }
    ]
}
```

**补充说明：上面的格式方便查看，最终输出到文件仍然为jsonl的规范。**

## 相关项目

[MNBVC](https://github.com/esbatmop/MNBVC)
[WikiHowQAExtractor-mnbvc](https://github.com/wanicca/WikiHowQAExtractor-mnbvc)
[ShareGPTQAExtractor-mnbvc](https://github.com/pany8125/ShareGPTQAExtractor-mnbvc)
[deduplication_mnbvc](https://github.com/aplmikex/deduplication_mnbvc)
