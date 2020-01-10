#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import click
import requests

TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
TEXT2AUDIO_URL = 'http://tsn.baidu.com/text2audio'

GRANT_TYPE = 'client_credentials'
CUID = 'liys87x'

TTS_AK = ''
TTS_SK = ''
if 'TTS_AK' in os.environ:
    TTS_AK = os.environ['TTS_AK']
if 'TTS_SK' in os.environ:
    TTS_SK = os.environ['TTS_SK']


def get_token():
    param = {"grant_type": GRANT_TYPE,
             "client_id": TTS_AK, "client_secret": TTS_SK}
    r = requests.post(TOKEN_URL, params=param)
    if r.status_code == 200:
        return r.json()['access_token']
    else:
        print(r.json())
        raise Exception('Get Token Error!')


def text2audio(text, spd=5, pit=5, vol=5, per=0):
    lst = []
    tok = get_token()
    while text:
        _text, text = text[:2048], text[2048:]
        param = {"tex": _text, "tok": tok, "cuid": CUID, "ctp": "1",
                 "lan": "zh", "spd": spd, "pit": pit, "vol": vol, "per": per}
        r = requests.post(TEXT2AUDIO_URL, params=param)
        if r.status_code == 200 and r.headers['Content-type'] == 'audio/mp3':
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
@click.option('--per', default=0, help='The person. [0,1,3,4]')
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
