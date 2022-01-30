import shutil
from pathlib import Path
import json
from xpinyin import Pinyin
import re

def convert(input_folder, output_folder):
    """
    对md文件进行优化和整理
    :param input_folder:
    :param output_folder:
    :return:
    """
    files = Path(input_folder).glob('*.md')
    p = Pinyin()
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # 提取元信息，作为hugo文章的front-matter
            title = lines[0].strip()
            date = file.stem.split('_')[1]
            tags = []
            category = file.stem.split('_')[0]
            slug = p.get_pinyin(title.replace('#', '').replace('%', ''))

            contents =[]

            # 前15行为无用行，从第16行开始为正文
            for line in lines[15:]:
                # 添加标签
                if r"\#" in line:
                    tag = line.split('#')[1].split(' ')[0]
                    tags.append(tag)
                elif "收录于话题" in line:
                    continue
                # 图片链接替换
                elif "![](图片" in line:
                    path = re.search(r'!\[\]\((.*)\)', line).group(1)
                    pic_file = Path(path).name
                    final_path = line.replace(path, '/pic/'+pic_file)
                    contents.append(final_path)
                # 去除评论头像图片
                elif "http://wx.qlogo.cn" in line:
                    continue
                # 去除评论后边的“赞”数量
                else:
                    line = re.sub(r'赞\s\d+\n', '\n', line)
                    contents.append(line)

            info = {"categories":[category], "tags":tags,"date":date,"title":title,"slug": slug}

        with open(Path(output_folder, file.name.replace('#', '').replace('%', '')), 'w', encoding='utf-8') as fw:
            fw.write('---\n')
            fw.write(json.dumps(info, ensure_ascii=False,indent=2)+'\n')
            fw.write('---\n')
            fw.writelines(contents)

def pic_extract(input_folder, output_folder):
    """
    将图片提取到同级的文件夹中
    去除封面图片文件
    :param input_folder:
    :param output_folder:
    :return:
    """
    files = Path(input_folder).glob('./**/*')
    for file in files:
        if file.is_file() and "封面图片" not in file.name:
            shutil.copy(file, Path(output_folder, file.name))

if __name__ == '__main__':
    convert()
    pic_extract()