#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import click
import requests
TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token?grant_type={0}&client_id={1}&client_secret={2}'
TEXT2AUDIO_URL = 'http://tsn.baidu.com/text2audio?tex={0}&lan=zh&cuid={1}&ctp=1&tok={2}&spd={3}&pit={4}&vol={5}&per={6}'
GRANT_TYPE = 'client_credentials'
CUID = 'pyandi_ffff'
TTS_AK = ''
TTS_SK = ''


def get_token():
    ak, sk = TTS_AK, TTS_SK
    if 'TTS_AK' in os.environ:
        ak = os.environ['TTS_AK']
    if 'TTS_SK' in os.environ:
        sk = os.environ['TTS_SK']
    url = TOKEN_URL.format(GRANT_TYPE, ak, sk)
    r = requests.post(url)
    if r.status_code == 200:
        return r.json()['access_token']
    else:
        print(r.json())
        raise Exception('Get Token Error!')


def text2audio(text, spd=5, pit=5, vol=5, per=2):
    lst = []
    tok = get_token()
    while text:
        _text, text = text[:1024], text[1024:]
        url = TEXT2AUDIO_URL.format(_text, CUID, tok, spd, pit, vol, per)
        r = requests.post(url)
        if r.headers['Content-type'] == 'audio/mp3':
            lst.append(r.content)
        else:
            print(r.json())
            raise Exception('Text to audio error!')
    return b''.join(lst)


@click.command()
@click.option('--text', '-t', help='The text from stdin.')
@click.option('--from_file', '-f', help='The text from file.')
@click.option('--result', '-r', default='default.mp3', help='The result file.')
@click.option('--speedch/--no-speedch', default=False, help='Speedch or not.')
@click.option('--speedch_app', default='mpv', help='Speedch app, e.g. "mpv".')
@click.option('--spd', default=5, help='The speed. [0-9]')
@click.option('--pit', default=5, help='The pitch. [0-9]')
@click.option('--vol', default=5, help='The volume. [0-9]')
@click.option('--per', default=2, help='The person. [0,1,3,4]')
def run(text, from_file, result, speedch, speedch_app, spd, pit, vol, per):
    if text is None and from_file is None:
        raise Exception("Please give a option text or from_file!")
    if text is None:
        if not os.path.exists(from_file):
            raise Exception('The from file {0} not exists!'.format(from_file))
        text = open(from_file, 'r').read()
    audio = text2audio(text, spd, pit, vol, per)
    with open(result, 'wb') as f:
        f.write(audio)
    if speedch:
        os.system('{0} {1}'.format(speedch_app, result))


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print(ex)
        raise
        sys.exit(1)
