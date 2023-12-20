Inscription Tools---支持EMV兼容链的自动Mint铭文工具
##使用此工具前，请确保您已安装Python,制作者版本为例：
-Python 3.11.6
-Web3 6.11.3
-dotenv
## 安装

1. 克隆版本库：

```bash
git clone https://github.com/your-username/inscription-tools.git
cd inscription-tools
##安装依赖项：
pip install -r requirements.txt
##设置您的环境变量： 
创建一个 .env在项目根目录中创建文件并添加以下内容
account_private_key=your_private_key
account_address=your_account_address
代替 your_private_key和 your_account_address使用您的实际私钥和帐户地址。
##运行脚本：
python inscription_tools.py

欢迎贡献！  如果您发现任何问题或有改进建议，请随时提出问题或创建拉取请求。
