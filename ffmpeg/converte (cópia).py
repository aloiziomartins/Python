'''
Objetivo listar arquivos, e converter ou otimizar arquivos de vídeo de um diretório de origem para um diretorio

Vamos usar ffmpeg para otimizar ou converter vídeo.
Instalar ubuntu 22.04
#sudo apt install ffmpeg
Veificar instalação
#ffmpeg -version

Obs: É extremamamente necessário verificar a documentação ffmpeg e testar as definições
de vídeo e converssão.

Objetivo pricipal é tornar o tamanho de arquivo menor, é possíve com a documentação
converter formatos do arquivo.

'''
import os


#Definições de vídeo para conversão
comado_ffmpeg = 'ffmpeg'
codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 128k'
quadros = '-r 30'

#Diretórios
origem = os.path.join('origem')
destino = os.path.join('destino')
#Script
def converter():
    if os.path.isfile(origem):
       for files in os.listdir(origem):
            completo = origem+'/'+files
            saida = destino+'/'+files
            commando = f'{comado_ffmpeg} -i {completo} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {saida}'
            os.system(commando)
    else:
        print('Diretório não possui arquivos!')

converter()