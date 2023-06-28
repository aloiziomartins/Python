import cv2
import sqlite3


WebCamera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Consultas
def consultar_name(id):
    try:
        connect = sqlite3.connect('base.db')
        cursor = connect.cursor()
        cursor.execute("select name from users WHERE id = ?", (id,))
        l_pessoas = cursor.fetchone()
        if l_pessoas:
            return (l_pessoas[0])
        else:
            return 'Desconhecido'
    except: 
        print('Erro, tente novamente')
    finally:
        connect.close()
    
def coletarimagens(name):
    cont = 1
    total_img = 25
    while True:
        status, img = WebCamera.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        facedetect = classificador.detectMultiScale(img_gray, scaleFactor=1.5, minSize=(150, 150))

        for (x, y, l, a) in facedetect:
            cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                img_face = cv2.resize(img_gray[y:y + a, x:x + l], (220, 220))
                cv2.imwrite(f"Fotos/{name}/" + str(cont) + ".jpg", img_face)
                print(f"[Fotos/{name}/" + str(cont) + " capturada com sucesso]")
                cont += 1
        cv2.imshow("WebCam", img)
        cv2.waitKey(1)
        if total_img < cont:
            break
    print("Faces capturadas com sucesso")
    WebCamera.release()
    #cv2.destroyAllWindows()



def conhecer():
    reconhecedor = cv2.face.LBPHFaceRecognizer_create()
    reconhecedor.read('classificadorLBPH_V1.yml')
    while True:

        status, img = WebCamera.read()
        img_gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faceDetectadas = classificador.detectMultiScale(img_gray2, scaleFactor=1.5)

        for (x, y, l, a) in faceDetectadas:
            cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
            id, confianca = reconhecedor.predict(img_gray2)
            name = consultar_name(id)               
            cv2.putText(img, name,  (x, y + (a + 30)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

        cv2.imshow("Face", img)
        if cv2.waitKey(1) == ord('q'):
            break

    WebCamera.release()
    cv2.destroyAllWindows()