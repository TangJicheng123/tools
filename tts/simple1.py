from gtts import gTTS
import os

# 设置要转换的文本（中文）
text = "你好，我是汤继承"

# 创建 TTS 对象，指定语言为中文（zh-cn）
tts = gTTS(text, lang='zh-cn')

# 保存语音到文件
tts.save('output.mp3')

# 播放语音
os.system('mpg321 output.mp3')  # 需要安装 mpg321 播放器
