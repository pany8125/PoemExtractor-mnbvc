# ShareGPTQAExtractor-mnbvc

## 项目描述

- 本项目目的是将诗歌清洗为MNBVC的标准文本格式
- 原文件和目标文件均为jsonl格式，每行对应一首诗歌，源格式和目标详细格式附后。

## 环境

1. 下载本项目
```
git clone POEMExtractor-mnbvc
```
2. 进入目录并安装依赖
```
cd POEMExtractor-mnbvc
pip install -r requirements.txt
```

## 用法

通过以下命令将FILE文件转化并输出到以`POEM`为名称的结果文件中。
```shell
python sharepoem_extract.py FILE
```

以上命令将输出时间戳结果文件例子`sharePOEM_2023-07-17-00-30-43.jsonl`。

## 注意

1. 

## 代码说明

- `sharepoem_extract.py` 入口程序

## 原始文件示例（一行）

```json
{
  "title": "一个过程的小细节",
  "author": "00913",
  "content": "\n请把这把尖刀放回盒子里\n已经生锈了，它追随你的欲望\n它是一件记念的物品\n而你就是它尚未剖腹而生的婴儿\n\n已经习以为常，一群悒郁的病毒\n你擦干的刀刃，另一面切伤了手指\n在你的血流滴滴的那会儿\n你如此镇静地包扎有点职业化\n\n请把你的镜子彻底裸体地照出自己\n用白皙地肤色平息性感的挑逗\n你熟练地削一片柠檬地时候\n却解说了这是必要的生活\n\n让我摸一摸你的刀，可是你\n收起来了，而一个身体的智慧\n是将我构成了你无所畏忌的呢称\n你贸然的偷袭，这就堵住了我呼吸"
}
```

## 输出jsonl文件格式

1. 对于每一首诗歌数据，其最高层次结构如下。
```json
{
    '文件名': '文件.txt',
    '是否待查文件': False,
    '是否重复文件': False,
    '文件大小': 1024,
    'simhash': 0,
    '最长段落长度': 0,
    '段落数': 0,
    '去重段落数': 0,
    '低质量段落数': 0,
    '段落': []
}
```
2. 在json中，将每一行为一个段落，段落的json结构层次示例如下：
```json
{
    '行号': line_number,
    '是否重复': False,
    '是否跨文件重复': False,
    'md5': md5,
    '内容': line
}
```

## 结果示例

```json
{
    "文件名": "一个过程的小细节",
    "是否待查文件": False,
    "是否重复文件": False,
    "文件大小": 1024,
    "simhash": 0,
    "最长段落长度": 0,
    "段落数": 0,
    "去重段落数": 0,
    "低质量段落数": 0,
    "段落": [
        {
          '行号': 1,
          '是否重复': False,
          '是否跨文件重复': False,
          'md5': md5,
          '内容': line
        },
        {
          '行号': 2,
          '是否重复': False,
          '是否跨文件重复': False,
          'md5': md5,
          '内容': line
        },
        ...
    ]
}
```

**补充说明：上面的格式方便查看，最终输出到文件仍然为jsonl的规范。

## 相关项目

[MNBVC](https://github.com/esbatmop/MNBVC)
[WikiHowQAExtractor-mnbvc](https://github.com/wanicca/WikiHowQAExtractor-mnbvc)
[ShareGPTQAExtractor-mnbvc](https://github.com/pany8125/ShareGPTQAExtractor-mnbvc)
