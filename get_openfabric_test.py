import http.client
import json
import time

conn = http.client.HTTPSConnection("faucet.openfabric.dev")

coin_address = ["0x1d2d4062F3bF9789bE550F08B7b9Add010EEb5D8", "0x00B2fad42707d1A632f30D8C76e7f43e5337b0c6", "0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd", "0xe71091C7263Cf00D85E18d553c637D76289E21C5"
                , "0x810D48C4553357CebF8F7a025C034449B388e573", "0x57915f3161F7aADDf791333e879F721947D09a77", "0x597758A35BADc465BD8a78E6Be49B25743Db1652", "0xcC12E2Dc0070D6525D4094Ec9EC34345C9C79484", "0xAdc0268cd7bc34022B15DEb406C0D3875Db6fF8f"]

headers = {
  'Content-Type': 'application/json'
}

for address in coin_address:
    payload = json.dumps({
        "address": address
    })
    conn.request("POST", "/api/claim", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print("add coin -------------------------------------\n")
    time.sleep(1)
