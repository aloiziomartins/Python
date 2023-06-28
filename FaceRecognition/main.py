from simple_term_menu import TerminalMenu
import cv2
import numpy as np
import os
import sqlite3
from Camera import conhecer
from basedados import adduser

###Consutas
def consultar_id(name):
    try:
        connect = sqlite3.connect('base.db')
        cursor = connect.cursor()
        cursor.execute("select * from users")

        l_pessoas = cursor.fetchall()
        for id, l_name in l_pessoas:
            if l_name == name: 
                return id
    except:
        print('Erro ao consultar')

    finally:
        connect.close()


#treinar
lbph= cv2.face.LBPHFaceRecognizer_create()
def treinar():
    if (os.path.exists('./classificadorLBPH_V1.yml')) == False:
        lbph.write('classificadorLBPH_V1.yml')
    else:
        lbph.read('classificadorLBPH_V1.yml')

    diretorio = 'Fotos'
    diretorio = os.path.join('Fotos/')

    if os.path.exists(diretorio):
        lista_subdir =  []

        for subdir in os.listdir(diretorio):
            lista_subdir.append(subdir)
        faces = []
        ids = []
        for name in lista_subdir:
            for imagem_face in os.listdir('Fotos/'+ name):

                img_face = cv2.cvtColor(cv2.imread('Fotos/'+ name +'/' + imagem_face), cv2.COLOR_BGR2GRAY)
                ids.append(consultar_id(name))
                faces.append(img_face)
        array_ids = np.array(ids)
        lbph.train(faces, array_ids)
        lbph.write('classificadorLBPH_V1.yml')
    else:
        return print('Diretórios inesistente!')
    
    print('Treinamento concluído')

def exibe_menu():
    menu_title = "Escolha uma opção: "
    menu_items = ["Adcionar um usuário", "Treinar Reconhecimento Facial", "Detectar a face de um usuário", "Sair"]
    menu =  TerminalMenu(menu_items)

    while True:
        selected_index =  menu.show()
        if selected_index == 0:
            adduser()
        elif selected_index == 1:
            treinar()
        elif selected_index == 2:
            conhecer()
        else:
            break

exibe_menu()


