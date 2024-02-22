import requests
 
header = {'Content-Type': 'application/json'}
 
r2 = requests.post(f'https://api.devnet.solana.com',data='{"method": "requestAirdrop", "jsonrpc": "2.0", "params": ["AuwZZwWTVMGxf3VWBo7rGgEoYJSwvzssaC7Tco12z5gr", 2000000000], "id": "c5935154-73a1-4712-9c08-c392d216dd22"}', headers=header,verify=False,proxies={ 'http':'http://127.0.0.1:8080/','https':'http://127.0.0.1:8080/'} )
 
print(r2.content);
