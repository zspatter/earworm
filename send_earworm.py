import random
from pathlib import Path

import lyricsgenius
import openpyxl
from notifications import text_myself
from pyshorteners import Shortener, Shorteners


def get_earworm(sheet):
    row = random.randint(2, sheet.max_row)
    title = sheet.cell(row=row, column=1).value.strip()
    artist = sheet.cell(row=row, column=2).value.strip()
    earworm = sheet.cell(row=row, column=3).value.strip()

    return title, artist, earworm


if __name__ == '__main__':
    genius_token = '***'
    genius = lyricsgenius.Genius(genius_token)
    bitly_access = {'bitly_token': '***'}

    wb = openpyxl.load_workbook(Path('./earworms/earworms.xlsx'))
    ws = wb.active

    title, artist, earworm = get_earworm(ws)
    song = genius.search_song(title=title, artist=artist)
    print(song._url)

    shortener = Shortener(Shorteners.BITLY, **bitly_access)
    short_url = shortener.short(song._url)
    print(short_url)

    text_myself(message=f'{earworm}\n{short_url}')
