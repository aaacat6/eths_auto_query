# erc-20(ethscription)缺漏查询以及自动铸造.

## 主要文件说明:

**eths_queryMain.py**

### 创建初始输入变量:
   - 输入eths名称
   - 输入要查询的eths开始编号.
   - 输入要查询的eths结束编号.
  
### 创建包含要查询eths代币格式的列表:
   - 通过for循环和range()得到id序列.
   - 通过+=获得长字符串.
   - 通过split()将长字符串分割成列表.
   - 将列表赋值给contents
  
### 主查询函数:
   - 输入contents列表中每个单独的变量content.
   - 将content进行哈希加密并转换位16进制.
   - 通过api将其内容传递到官网.
     - 如果服务器无法连接,函数返回值none,none.
     - 如果服务器已存在该数据,函数返回 none,none
     - 如果服务器不存在该数据,则将content转化为16进制content_hex,函数返回content_hex,与content本身
  
### 程序运行区间,主要为了得到2个json文件:
   - 16进制的eths数据,为了下一步批量打做准备.
   - eths的utf-8数据,为了方便观察对应.
  
  **具体做法**:
   - 通过for循环遍历contents中的每个变量content.
   - 在每次for循环中,将content入主查询函数,函数返回content_hex,content,写入列表.
   - 将列表转换为json文件保存出去.
 
## 额外文件说明

**eths_queryCurMint.py**: 获取当前正在铸造的eths内容,代码内有返回范例.

**eths_queryEths.py**: 获取某单个eths是否铸造,代码内有返回范例.
