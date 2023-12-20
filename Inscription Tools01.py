import asyncio
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

private_key = os.environ.get('account_private_key')
address = os.environ.get('account_address')

# 输入 RPC URL
rpc_url = input('Enter the RPC URL: ')
web3 = Web3(Web3.HTTPProvider(rpc_url))

async def main():
    if not web3.is_connected():
        raise ConnectionError("Failed to connect to the node.")

    print(web3.is_connected())
    print(Web3.from_wei(web3.eth.get_balance(address), 'ether'))

    c = 0

    # 输入 mint 数据
    data = input("Enter the data to mint: ").strip()
    if not data.startswith('0x'):
        data = web3.to_hex(text=data)

    # 输入循环次数
    no_to_mint = int(input("Enter the number of times to mint:"))

    # 循环执行 mint
    for _ in range(no_to_mint):
        nonce = web3.eth.get_transaction_count(address)
        tx = {
            'nonce': nonce,
            'chainId': web3.eth.chain_id,
            'gasPrice': web3.eth.gas_price,
            'value': 0,
            'to': address,
            'from': address,
            'data': data,
        }

        try:
            gas = web3.eth.estimate_gas(tx)
            tx['gas'] = gas
            print(tx)

            signed_tx = web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f"Transaction Hash: {web3.to_hex(tx_hash)}")

            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status == 1:
                c += 1
                print(f"{c} Mint 成功！")

                # 每次成功完成一笔交易后等待5秒
                await asyncio.sleep(5)
        except Exception as e:
            print(f"Error: {e}")

# 运行异步函数
asyncio.run(main())
