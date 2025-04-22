from pygame import mixer

mixer.init()
mixer.music.load('Mundo 1, 2 e 3/ex021.mp3')
mixer.music.play()
input('Enter para encerrar reprodução!')
print('Programa encerrado!')
