import http.client
import json
import time

conn = http.client.HTTPSConnection("faucet.testnet.inco.org")
payload1 = json.dumps({
    "address": "0x1d2d4062F3bF9789bE550F08B7b9Add010EEb5D8"
})

payload2 = json.dumps({
    "address": "0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd"
})

payload3 = json.dumps({
    "address": "0x00B2fad42707d1A632f30D8C76e7f43e5337b0c6"
})

arrays = [payload1, payload1, payload2 , payload2, payload3, payload3]

headers = {
  'Content-Type': 'application/json'
}

for payload in arrays:
  conn.request("POST", "/api/get-faucet", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  print("-------------------------------------\n")
  time.sleep(2)
