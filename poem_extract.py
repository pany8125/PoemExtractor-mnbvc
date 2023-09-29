# -*- coding: utf-8 -*-
# 脚本设置使用utf-8编码

from datetime import datetime
import json
import os
import logging
import hashlib
import schema

# 配置日志记录
logging.basicConfig(
    filename='poem_log_file.log',  # 指定日志文件的名称
    level=logging.WARNING,  # 指定日志级别（INFO、WARNING、ERROR、CRITICAL等）
    format='%(asctime)s [%(levelname)s]: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 日期和时间格式
)    

def process_poem_file(file_path, output_file, start_line):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=start_line):
            this_line = line.strip()
            # 跳过空行
            if len(this_line) == 0:
                continue
            # 对当前行转换为json，如果报错则跳过
            try:
                json_data = json.loads(this_line)
                #用json_data的md5值作为id
                md5 = hashlib.md5(this_line.encode('utf-8')).hexdigest()
                json_str = schema.POEMSchema(file_name, file_size, line_number, md5, json_data['title'], json_data['author'], json_data['content']).to_json()
                output_file.write(json_str + '\n')
            except json.decoder.JSONDecodeError:
                logging.error(f"Line {line_number}, json decode error!")  # json解析失败
                logging.error(f"json str: {this_line}")
                continue
            except KeyError:
                logging.error(f"Line {line_number}, key error!")
                logging.error(f"json str: {this_line}")
                continue
            except Exception as e:
                logging.error(f"Line {line_number}, unknown error!")
                logging.error(f"json str: {this_line}")
                logging.error(e)
                continue
            # 打印迭代信息
            logging.info(f"Line {line_number} processed successfully!")
            logging.info(f"json str: {this_line}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Parse poem text to MNBVC text format.")
    parser.add_argument("source_files",type=str, default="final_data_sample_230706test.json", help="文件名")
    parser.add_argument("-o","--output",type=str, default="POEM",help="output file name (without extension)")
    parser.add_argument("-l","--start_line",type=int,default=1,help="read start line")
    args = parser.parse_args()
    with open(f'{args.output}_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.jsonl', 'w', encoding='utf-8') as of:
        # 调用函数来处理 JSON 文件，默认从第1行开始读取
        process_poem_file(args.source_files, of, args.start_line)