from word_cloud import get_weibo, gen_cloud

import json

if __name__ == "__main__":
    weibos = get_weibo.get_weibo()
    # with open ("results/result.json", "w", encoding="utf-8") as f:
    #     json.dump(weibos, f, ensure_ascii=False, indent=4)
    words = gen_cloud.split_text(weibos)
    gen_cloud.gen_cloud(words, "results/word_cloud.png")