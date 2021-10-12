from word_cloud import get_weibo, gen_cloud

if __name__ == "__main__":
    weibos = get_weibo.get_weibo()
    words = gen_cloud.split_text(weibos)
    gen_cloud.gen_cloud(words)