# 找到未加密的参数
# 想办法把参数进行加密，params => encText, encSecKey => encSecKey
# 请求网易，获取热评


# 安装pycrypto   pip install pycrypto
import json

import requests
from Crypto.Cipher import AES
from base64 import b64encode

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

# window.asrsea(JSON.stringify(i7b), bsR5W(["流泪", "强"]), bsR5W(Xp2x.md), bsR5W(["爱心", "女孩", "惊恐", "大笑"]));

# 请求方式是 post

data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_409649817",
    'threadId': "R_SO_4_409649817"
}
# 处理加密过程
d = data
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'mWyRpEll0rl09riw' # 手动固定 -> 原函数中是随机的
# encSecKey  i 固定的时候，encSecKey 固定返回
def get_encSecKey():
    return "bfce8ee4f0652dc1a3c1f63cda7e1b316200c38e939620854aa74e9a1928fe9eda6d1488a2f1c1997b0f05c7d678ca4df083a2cb440da747fd512fbf99277caa2d4c0674dc8e59e7d9fbbfe0d48978135f1c7d160bedbdb7649e9ba4394103ff22c1954fee717728b0662c404b408b4b59726578c00e907a303404e3645acc61"

# encText

# params 获取params 加密的是 data ,加密了两次
def get_params(data): # 默认收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second # 返回的是params

# 转成16的倍数
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data, key): # 加密过程
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC) # 创造加密器
    bs = aes.encrypt(data.encode('utf-8')) # 加密 加密的内容长度必须是16的倍数
    return str(b64encode(bs), 'utf-8') # 返回字符串



'''

function a(a) { # 随机 16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) # 循环 16次
            e = Math.random() * b.length, # 随机数
            e = Math.floor(e), # 取整
            c += b.charAt(e); # 去字符串中的xx的位置
        return c
    }
    function b(a, b) { # a 是要加密的秘钥
        var c = CryptoJS.enc.Utf8.parse(b) # b ?
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") 
          , e = CryptoJS.enc.Utf8.parse(a) # e 是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d, # 偏移量
            mode: CryptoJS.mode.CBC  # 模式 CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d: 数据 e: 010001 f: 
        var h = {}
          , i = a(16); # i是一个16位的随机值
        return h.encText = b(d, g), # g 是秘钥
        h.encText = b(h.encText, i), # params  i 也是秘钥
        h.encSecKey = c(i, e, f), # encSecKey  e 和 f 是固定的，i是变量，此时如果i固定，c就是固定的
        h
    }

'''
# 发送请求获取评论
resp = requests.post(url, data={
    "params":  get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.json())



