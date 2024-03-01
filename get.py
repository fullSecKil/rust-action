import http.client
import json
import time

conn = http.client.HTTPSConnection("api.devnet.solana.com")
payload1 = json.dumps({
  "method": "requestAirdrop",
  "jsonrpc": "2.0",
  "params": [
    "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
    2000000000
  ],
  "id": "c5935154-73a1-4712-9c08-c392d216dd22"
})

payload2 = json.dumps({
  "jsonrpc": "2.0",
  "id": "96dec5c4-4e6e-447e-bcf3-2bdebf9d282d",
  "method": "requestAirdrop",
  "params": [
    "5Q4hmzMSKjLdjpKsqn8KLxiHxUmrNUGmSYbbWNJH2PYj",
    2000000000
  ]
})

arrays = [payload1, payload1, payload2, payload2]

headers = {
  'Content-Type': 'application/json'
}

for payload in arrays:
  conn.request("POST", "/", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  print("-------------------------------------\n")
  time.sleep(2)

