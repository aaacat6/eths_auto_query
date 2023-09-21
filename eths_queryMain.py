import hashlib
import requests
import binascii
import json

# 1.创建初始输入变量.
eths_tick = input("请输入要查询的eths名称:")
start_num = input("输入开始编号:")
end_num = input("输入结束编号:")
start_num = int(start_num)  # input为字符串格式,此处转换为整数格式.
end_num = int(end_num)  # input为字符串格式,此处转换为整数格式.

# 2.创建列表变量contents,包含start_num到end_num数字id范围的eths格式字符串.
input = ""  # 循环外部创建该变量,不然每次循环该变量会重新回归原始状态.
for nums in range(start_num, end_num):  # 注意此处num变量只在该循环中有用.
    input += 'data:,{"p":"erc-20","op":"mint","tick":"' + \
        (eths_tick) + '","id":"' + str(nums) + '","amt":"1000"}/'
# rstrip()为删除该字符串最后一位/.删除之后再使用split()拆分,否则会得到一个空的列表元素.
contents = input.rstrip('/').split("/")

# 3.创建遍历列表函数
def query_content(content):
    # 从内容字符串中提取id.
    # split('"id":"')为将字符串分为两段,分别是"id":左右.注意,这两段字符串都不包括"id":
    # split('"id":"')[1]为选取第二段字符串.
    # split('"id":"')[1].split('"')将第二段字符串再分成2段,以"为分隔符.
    # split('"id":"')[1].split('"')[0]为选取第二段字符串的第一段.
    nums = content.split('"id":"')[1].split('"')[0]

    content_hash = hashlib.sha256()  # 使用 SHA-256 哈希函数计算哈希
    content_hash.update(content.encode('utf-8')) # 使用update更新content_hash变量内容
    content_hex_check = content_hash.hexdigest()  # 获取十六进制content_hash的哈希值

    # 从eths官网获取当前链上信息,官网链接:https://docs.ethscriptions.com/api-docs/ethscriptions-endpoints
    url = f"https://api.ethscriptions.com/api/ethscriptions/exists/{content_hex_check}"
    response = requests.get(url)  # response:回复

    if response.status_code == 200:  # 检查请求是否成功（HTTP状态码为200）
        result = response.json()  # 讲获得的json转化成python列表对象
        if result["result"]:  # 如果网站有数据,则会返回true
            print(f'erc20:{eths_tick},id:{nums}已被铸造')
            return None, None
        else:  # 如果网站未返回数据,则说明还未铸造
            content_hex = binascii.hexlify(content.encode()).decode()  # 将content转为16进制
            print(f'erc20:{eths_tick},id:{nums}可铸造')
            return content_hex, content
    else:
        print(f"无法连接网络,错误代码: {response.status_code}")
        return None, None

# 4.运行函数
contents_hex = []  # 创建将要转换为json的列表元素
contents_str = []  # 创建将要转换为json的列表元素

for content in contents:  # 遍历contents列表中的内容
    # 运行query_content函数,该函数导入content,输出2个值赋予content_hex, content_str
    content_hex, content_str = query_content(content)
    if content_hex and content_str:  # 如果query_content函数返回值不为none
        contents_hex.append(content_hex)  # 将query_content函数返回值添加到列表
        contents_str.append(content_str)  # 将query_content函数返回值添加到列表
with open(f'{eths_tick}_hex.json', 'w', encoding='utf-8') as file:  # 创建新的json文件,w可写入模式,编码模式utf-8
    # 通过json模块的dump()将数据写入,ensure_ascii=False确保能显示中文,indent能让json文件有换行和缩进
    json.dump(contents_hex, file, ensure_ascii=False, indent=4)
with open(f'{eths_tick}_str.json', 'w', encoding='utf-8') as file:  # 创建新的json文件,w可写入模式,编码模式utf-8
    # 通过json模块的dump()将数据写入,ensure_ascii=False确保能显示中文,indent能让json文件有换行和缩进
    json.dump(contents_str, file, ensure_ascii=False, indent=4)

print('查询结束')
