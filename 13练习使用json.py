# -*- coding: utf-8 -*-
#练习使用json
import json
str = '{"name":"盗梦空间"}'
#字符串转字典
obj = json.loads(str)
print('obj:',obj,type(obj))
#字典转字符串
obj_str = json.dumps(obj,ensure_ascii=False)
print('obj_str:',obj_str,type(obj_str))
#把对象保存成文件
json.dump(obj,open('json.txt','w',encoding='utf-8'),ensure_ascii=False)
#把文件转成对象
file_json = json.load(open('json.txt','r',encoding='utf-8'))
print('file_json:',file_json,type(file_json))
