# https://programmers.co.kr/learn/courses/30/lessons/17683

def calculateTime(s, e):
    s1, s2 = map(int, s.split(":"))
    e1, e2 = map(int, e.split(":"))
    return (e1*60 + e2) - (s1*60+s2)


def replaceShap(music):
    music = music.replace("C#", "c").replace("D#", "d").replace(
        "F#", "f").replace("G#", "g").replace("A#", 'a')
    return music


def solution(m, musicinfo):
    m = replaceShap(m)
    music = '(None)'
    for info in musicinfo:
        s, e, title, melody = info.split(",")
        melody = replaceShap(melody)
        tm = calculateTime(s, e)
        melody = melody*(tm // len(melody) + 1)
        if m not in melody[:tm]:
            continue
        if music == '(None)' or music[0] < tm:
            music = (tm, title)
    if music == '(None)':
        return '(None)'
    return music[1]
