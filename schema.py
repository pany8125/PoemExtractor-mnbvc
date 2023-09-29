import json
from datetime import datetime

class POEMSchema:
    def __init__(self, file_name, file_size, line_number, md5, title, author, content):
        self.file_name = file_name
        self.file_size = file_size
        self.line_number = line_number
        self.md5 = md5
        self.title = title
        self.author = author
        self.content = content

    def to_json(self):
        data = {
                "文件名": self.file_name,
                "是否待查文件": False,
                "是否重复文件": False,
                "文件大小": self.file_size,
                "simhash": 0,
                "最长段落长度": 0,
                "段落数": 0,
                "去重段落数": 0,
                "低质量段落数": 0,
                "段落": [
                    {
                    '行号': self.line_number,
                    '是否重复': False,
                    '是否跨文件重复': False,
                    'md5': self.md5, #整行json的md5
                    '标题': self.title, # 对应title
                    '作者': self.author, # 对应author
                    '内容': self.content # 对应content
                    }
                ]
            }
        return json.dumps(data, separators=(",", ":"), ensure_ascii=False)

json_str = POEMSchema("chinese_poems.jsonl",123,2,"afgdsfds","吃方便面想的一些问题222","22200913","\n222方便面快速解决饥饿\n饥饿可以慢慢地减退\n方便面。。。").to_json()
# print(json_str)
