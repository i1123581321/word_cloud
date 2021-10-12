'''
File Created: 2021/10/12 11:44:10
Author: ZhengxuanQian (zhengxuanqian@smail.nju.edu.cn)
-----
Last Modified: 2021/10/12 11:47:45
Modified By: ZhengxuanQian (zhengxuanqian@smail.nju.edu.cn>)
'''


import jieba
import wordcloud

with open("static/stopwords.txt", "r", encoding="utf=8") as f:
    stopwords = f.readlines()
    stopwords = {x.strip() for x in stopwords}
    stopwords |= {" ", "\n", "\u200b", "&", "gt", ";"}

def split_text(text_list: list[str]) -> list[str]:
    result = []
    for sentence in text_list:
        temp = jieba.lcut(sentence)
        temp = [x for x in temp if x not in stopwords]
        result.extend(temp)
    return result

def gen_cloud(words: list[str], dest: str):
    w = wordcloud.WordCloud(width=1200, height=800, background_color="white", font_path="static/FZLTHJW.TTF", prefer_horizontal=1)
    w.generate(" ".join(words))
    w.to_file(dest)

if __name__ == "__main__":
    pass
