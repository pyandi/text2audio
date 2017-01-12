# text2audio
通过百度语音合成服务实现文本转语音

---

## 使用说明
> 需要自行到 http://yuyin.baidu.com/app 创建应用，开通语音合成服务，并将 API key(TTS_AK) 和 Secret key(TTS_SK) 配置到脚本中或环境变量里
> 查看帮助请执行 python text2audio.py --help

## 依赖说明
- click: 用于实现命令行调用
- requests: 用于调用 RESTFUL API

## 示例
> python text2audio.py -t "你好吗" --speedch
