import http.client
import json
import time
import sys

conn = http.client.HTTPSConnection("faucet.testnet.tenet.org")

coin_address = ["0x1d2d4062F3bF9789bE550F08B7b9Add010EEb5D8", "0x00B2fad42707d1A632f30D8C76e7f43e5337b0c6"
           , "0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd"]

body = {
    "jsonrpc": "2.0",
    "method": "requestTenet",
    "id": 1,
    "params": {
        "address": "0x7bA0f41AFb392f647e7E64dDad8912fa6F7a76bd",
        "captcha": "03AFcWeA5PVY34Jvlvmmy3C8i8FVloO6L8A_2SD56IJyeoYd5LwtxIk_vIA2jiFrUJZ7WYBUhPI-U-8rt-Dtlz-Fy56V8zHjdOYxVUtNMqZ8orh5dZkfbxrbCmH8Od_g2DIEn2IOEAyLqOQKfA6riJVidg3Y0LjYZa3gy2sZKX0Pn_nkMsbkAm5LBTxup6wRKxdd8KihNEMLvfdsoWxGkhQHifJonjRjiPlemPSqdvxMS6WQz5UWgmvkpO0_BnaLl83cRVEbx2fE7yKwjBBknmp5VaHWwj_h0m8d2fSLVxlvYlIfHCt6g-o1pD_Bn3RPHRYPymOoO9BBg4nAcrepYdgYmMvXGKVVkiKa_1Jcwqc919VRXYAOWPFlmSDZqx2-YzewX6wGQyZoE1t_14BrHFtmFl7Z6fDo0XB8VRLhonqHR_PkGIQKX3XYgrZcKIWd67_0Mug7uvkFEJosdHcdAcH_ew8hJ9N0tftpFtX4uHpGdcoHe7GBCwuVxade8XEQ7Xw5FcN10dWKHW4SpGh7FPrsr0NwrloJvkxZvbMvLkmuiv0W67JE0b1rP4QdiRBqw-IFkTWdpVwHvVnwn4P0cMon3OrakX1jlj9d4SS_OMoZHfAcpMpn8kkn02hWn41J9-Y125MBrbEgY_ROHXr0gq8rF6BN90Sm9txuu6l2jbEmrDnpnIgpbdXQZgXZ2DDNloZcA74rMfEoKH49KkGgT7tNkJhsFUhcaAQujNBGDNuX9zSMrOpPh5ySOoHJpDZrWDRdYuTz_m7MoHNua6NG3uwZ5bFfGiTyCJt_3-j_59rCZ7iQoT26COMvphMeJPB6nUrO4xFsRXcHsfTD6ZjWM_Ru6VCtCnKvqZ4_IhldjX1T121ezIpLikUu8gyJZC41AUBKUjLoXOZDx9-LNNaTgYLC8JmUnC3pVimNnBpvZ4LdOCoFFXp0aA1lbQSxrauQgbyHPIHCO6U8il0VXoFQXNwjExKKi97tmBQ1ocYHCPdl_PvfG2x-6EqA24aS-RpSDglYEWMPMPKmfPCVmWatSdth5ukUgDVPv9CehYbSVLQR840RmMtaeJTkhicKCFxomvvCfTsjTCoJqVSFTruJXozxJNMgU6lTfHfGTaqdFQDGTw3Qzat14NbKI6xhK-eK5UrG0uDPwQ6yYUJbecZLTaCLZ-5JsvXqh1BD45NxkeqbW-NtMeYfUnsbTKCRjRaYr_718I_HZxepK3Okq289jfRxN6IwAcB92KDdeartv2qhqGBd-Jmtzk8o9D-1LknNX7kEcIcPUDe4fQjpxXcStgYFD6M5jTq-XHqRNGPY2BriWFmlQc5qnTgKhD4xlHh0dAtaz5brNB81Nn22jo-nlk2pDl7cZgHFJ5m4VzdH5Rs3hd4n8IgiWE-ZxkzI0EjaUkOoayx33Z-7QYKAnyh3Jtq2-PhlNjWqdTLIxG5Y7-CoLTSpYtV2HBeMSmWyJXi9zyaKPiFmBZ8V5ZJvvt07bkXzClSulasN5lfJFDRPU7q8ZD_2SBNgd7PSDzPcNiXH6OHPcY2lZ9hmzCinJ3cgvyYp301YpF3UnrF_uflTYuppeqcLb3P7shHG5WpVWdBm67rhl2WotBBAqtOE1QPysOPYcO-xss0FbN2HOQlnkLO70rWXuXpKUOVx09rLD8ZvZ3Pc7c9ZxW13YMCg-EnNNhImltVaG4q7zVv8KyqiTov-Lz30LQVm8k4bULEOpyR8ghezDJCpieGrrEHq5WXbOI12pgm4zdLr2baRwxl4W95eNZzzPX1mP8tTF67zzcJFNHFvLfoZNN2XHV9nlqsNtP8ijBRY-yv4qa5QPN4IJrgT6pVXjuj-o4ee86UuBUuikZmbRu-QaHN0i0jdaJqT5AFij-Z2dvdOoRtHR6IhSwOiKuzhGSZfz6WhcUH7ZyJCrHdxruI1qxyRnafwIiPQsUjCT8SFQQfO6LecSzcDH2ZjWvd0KmFA09qqzd7Va7bI-CK2fSoSnqAbaL"
    }
}

headers = {
  'Content-Type': 'application/json'
}

for address in coin_address:
    body['params']['address'] = address
    payload = json.dumps(body)
    conn.request("POST", "/rpc", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("address "+ address +"-------------------------------------\n")
    print(data.decode("utf-8"))
    time.sleep(2)
