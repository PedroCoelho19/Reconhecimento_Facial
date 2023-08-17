import face_recognition as fr

def reconhece_face(url_foto):
    fotos = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(fotos)
    if(len(rostos) > 0):
        return True , rostos

    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    pedro = reconhece_face("./img/pedro2.jpeg")

    if(pedro[0]):
        rostos_conhecidos.append(pedro[1][0])
        nomes_dos_rostos.append("Pedro")

    edivaldo1 = reconhece_face("./img/edivaldo.jpeg")

    if(edivaldo1[0]):
        rostos_conhecidos.append(edivaldo1[1][0])
        nomes_dos_rostos.append("Edivaldo")

    return rostos_conhecidos, nomes_dos_rostos