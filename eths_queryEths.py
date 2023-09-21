'''
测试返回数据类型
{
    "result": true,
    "ethscription": {
        "transaction_hash": "0x33f299e75bca6cfa120b74f54dccc3c1327942543665b36b44452c6dc089b359",
        "current_owner": "0x92e53cc329a606fe248ec6356c7457dceeedcdaf",
        "creator": "0x92e53cc329a606fe248ec6356c7457dceeedcdaf",
        "creation_timestamp": "2023-09-14T15:17:11.000Z",
        "ethscription_number": 1201919,
        "previous_owner": null,
        "mimetype": "text/plain",
        "content_taken_down_at": null,
        "transaction_index": 45,
        "initial_owner": "0x92e53cc329a606fe248ec6356c7457dceeedcdaf",
        "event_log_index": null,
        "block_confirmations": 74,
        "min_block_confirmations": 74,
        "overall_order_number_as_int": "18135344000045000000",
        "image_removed_by_request_of_rights_holder": false,
        "content_uri": "data:,{\"p\":\"erc-cash\",\"op\":\"mint\",\"tick\":\"ESH\",\"id\":\"18958\",\"amt\":\"1000\"}"
    }
}
'''

import hashlib
import requests
import binascii
import json

def query_content():
    content = 'data:,{"p":"erc-20","op":"mint","tick":"swap","id":"19055","amt":"1000"}'
    # 使用 SHA-256 哈希函数计算哈希
    content_hash = hashlib.sha256()
    # 使用update更新content_hash变量内容-既导入content值到上述运算
    content_hash.update(content.encode('utf-8')) 
    # 获取十六进制content_hash的哈希值
    content_hex = content_hash.hexdigest()
    # 从eths官网获取当前链上信息,官网链接:https://docs.ethscriptions.com/api-docs/ethscriptions-endpoints
    url = f"https://api.ethscriptions.com/api/ethscriptions/exists/{content_hex}"

    try:
        response = requests.get(url) # response:回复
        result = response.json()
        print(json.dumps(result, indent=4)) # 漂亮打印,indent可设置行的缩放数量

        response.raise_for_status()  # 检查HTTP请求是否成功
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:  # 包含JSONDecodeError
        print(f"Invalid JSON received: {response.text}")

query_content()