import requests
import re
import json
import os
import pprint # 格式化
import subprocess

def get_response(html_url):
    '''发送请求'''
    headers = {
        'referer': 'https://www.bilibili.com/', # 防盗链
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }

    response = requests.get(url = html_url, headers = headers)
    return response

def get_video_info(html_url):
    resp = get_response(html_url)
    title = re.findall('<title data-vue-meta="true">(.*?)</title>', resp.text)[0]
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)[0] # 正则匹配
    json_data = json.loads(html_data)
    # pprint.pprint(json_data) # 格式化下
    # 403 状态码 没有权限
    # 防盗链的作用：告诉服务器，发送的请求的url，是哪里来的
    # 数据解析
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    title_name = re.sub('\W+', '', title).replace("_", '')
    print(title)
    print(title_name)
    # print('')
    # print(audio_url)
    # print('')
    # print(video_url)
    video_info = [title_name, audio_url, video_url]
    return video_info

def save(title, audio_url, video_url):
    # 保存数据，二进制数据
    # response.content 获取响应体的二级制数据
    audio_content = get_response(audio_url).content
    video_content = get_response(video_url).content
    with open(title+'.mp3', mode='wb') as f:
        f.write(audio_content)
    with open(title + '.mp4', mode='wb') as f:
        f.write(video_content)
    print('保存完毕===》》')

def merge_data(video_name):
    print('数据合并开始', video_name)
    video_name = re.sub('\W+', '', video_name).replace("_", '')
    'ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4'
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
    print(COMMAND)
    subprocess.Popen(COMMAND, shell=True)
    print('视频合成完成----')


url = 'https://www.bilibili.com/video/BV1pi4y1k75A?spm_id_from=333.337.search-card.all.click'

video_info = get_video_info(url)
save(video_info[0], video_info[1], video_info[2])
merge_data(video_info[0])

# print(os.getcwd(), '哈哈哈')