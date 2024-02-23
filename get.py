import http.client
import json

conn = http.client.HTTPSConnection("api.devnet.solana.com")
payload = json.dumps({
  "method": "requestAirdrop",
  "jsonrpc": "2.0",
  "params": [
    "AuwZZwWTVMGxf3VWBo7rGgEoYJSwvzssaC7Tco12z5gr",
    2000000000
  ],
  "id": "c5935154-73a1-4712-9c08-c392d216dd22"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
