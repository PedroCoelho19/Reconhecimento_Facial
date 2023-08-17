import cv2 #opencv
import mediapipe as mp

#inicializando o opencv e o mediapipe

webcam =cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True: 
    #Ler as informações da webCam
    verificador , frame = webcam.read()

    if not verificador: 
        break
    #Reconhecer os rostos

    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #desenhar os rostos na imagen
            desenho.draw_detection(frame , rosto)
    cv2.imshow("Rostos na webCam", frame)   

    #quando aperta ESC, para o loop
    if cv2.waitKey(5) == 27:
        break
webcam.release()