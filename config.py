from colors import *
info = {}
info['width'] = 1300
info['height'] = 700
info['pause'] = False
info['win'] = False
info['status'] = 1
info['time'] = 1
info['miliseconds'] = 0
info['turno'] = 1
info['carta'] = 1
info['printed_gema'] = False
info['dado'] = None
info['dadoX'] = int((info['width'] - 188) / 2)
info['dadoY'] = int((info['height'] - 177) / 2)

machine = {}
machine['process'] = False
machine['solved'] = False
machine['delay'] = 50