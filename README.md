# word cloud

爬取新浪微博，生成词云

请自行添加 utils/config.py 并配置

```python
COOKIES = {
    "SUBP": "",
    "SCF": "",
    "SUB": "",
    "_T_WM": "",
}

HOMEPAGE = f"https://weibo.cn/{your_uid}/profile"

PAGE = 1
```