# Person Toolbox

## Tools

### text2audio

通过百度语音合成服务实现文本转语音

**使用说明**:

- 需要自行到百度云管理控制台创建语音技术应用，并将 API key(TTS_AK) 和 Secret key(TTS_SK) 配置到脚本中或环境变量里
- 查看帮助请执行 python text2audio.py --help

**示例**:

```shell
python text2audio.py -t "你好吗" --speedch

python text2audio.py -f README.md --speedch
```
