# Inscription Tools-支持EMV兼容链的自动Mint铭文工具

## 概述
`EVM_inscription`是一个使用 Python编写的脚本，意在简化Mint铭文繁琐且效率过低的问题，通过此脚本自动高效批量创建铭文，兼容EVM区块链


## 安装依赖项：
1. **使用此工具前，请确保您已安装Python**: 以作者版本为列:Python 3.11.6
   ```
   pip install web3==6.11.3
   pip install -r requirements.txt
   pip install python-dotenv==1.0.0
   ```
 ## 设置
1. 在.env文件中写入地址和私钥
2. 运行脚本:Inscription Tools.py
3. 填入RPC_url:推荐[ChainList](https://chainlist.org/)
4. 填入铭文格式：data:,{"p":"src-20","op":"mint","tick":"RYSH","amt":"1000"}
5. 填入需要的张数
![GBwG9RFbQAAHhHR](https://github.com/inmetx/inscriptionEVM/assets/38844751/863acd7d-5459-40e1-94b6-3375d6f9a158)

## 温馨提示：
- 如果您发现任何问题或有改进建议，请随时提出问题或创建拉取请求
- 始终确保您的私钥安全存储，关注您正在交互的区块链汽油费和网络状况，以避免意外成本
