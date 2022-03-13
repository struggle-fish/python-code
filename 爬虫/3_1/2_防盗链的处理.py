import requests
# 原始url
url = 'https://www.pearvideo.com/video_1753950'
# 1.拿到contId
# 2.拿到videoStatus 返回的json -> srcURL
# 3.srcURL里的内容进行修剪
# 4.下载视频

contId = url.split('_')[1]
videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5611650872724843'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 防盗链 溯源，当前请求的上一级是谁
    'Referer': url
}
resp = requests.get(videoStatusUrl, headers=headers)
# print(resp.json())
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
# 视频真实链接
# https://video.pearvideo.com/mp4/short/20220309/cont-1753950-15837534-hd.mp4
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
# print(srcUrl)

# 下载视频
with open('video/' + contId + '.mp4', mode='wb') as f:
    f.write(requests.get(srcUrl).content)
f.close()




















































