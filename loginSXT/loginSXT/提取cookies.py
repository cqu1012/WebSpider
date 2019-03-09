# -*- coding: utf-8 -*-
str="UM_distinctid=1690a32de0c7b0-0e9cd9cda31807-6313363-e1000-1690a32de0db7b; 53gid2=10850679857008; 53revisit=1550655240760; zg_did=%7B%22did%22%3A%20%22169471548364c8-0c7ccc39f307a7-1333062-1fa400-169471548375a1%22%7D; PHPSESSID=0dbs36soamra2om45hbeogbdd0; visitor_type=old; 53gid0=10850679857008; 53gid1=10850679857008; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DgUEBy-U_Oa6iOOXmjxQQNS2rNegg5gaTQYjBkj0TZcO%26wd%3D%26eqid%3Dfae18c8400001688000000065c7cb176; 53kf_72085067_land_page=http%253A%252F%252Fwww.sxt.cn%252F; kf_72085067_land_page_ok=1; CNZZDATA1261969808=993143005-1550649659-http%253A%252F%252Fwww.sxt.cn%252F%7C1551684734; zg_c1e08f0fa5e3446d854919ffa754d07f=%7B%22sid%22%3A%201551689704186%2C%22updated%22%3A%201551689705722%2C%22info%22%3A%201551675770945%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%AF%B8%E8%91%9Bio%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.sxt.cn%22%2C%22landHref%22%3A%20%22http%3A%2F%2Fwww.sxt.cn%2F%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D"
cookies = {}
for cookie in str.split(';'):
    #使用等号分割并只分割一次
    key,value = cookie.split('=',1)
    cookies[key] = value
print(cookies)
