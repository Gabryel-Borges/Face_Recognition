import cv2
import face_recognition as fr

lista_moradores = [
    {'nome':'jeff bezzos', 'img':'img/bezzos.jpeg', 'encodings':''},
    {'nome':'bill gates', 'img':'img/bill.jpg', 'encodings':''},
    {'nome':'leonardo', 'img':'img/leonardo.webp', 'encodings':''},
    {'nome':'elon musk', 'img':'img/musk.webp', 'encodings':''},
    {'nome':'obama', 'img':'img/obama.jpg', 'encodings':''},
    {'nome':'paola oliveira', 'img':'img/paola.jpg', 'encodings':''},
    {'nome':'paula fernandes', 'img':'img/paula.jpeg', 'encodings':''},
    {'nome':'sandra bullock', 'img':'img/Sandra.webp', 'encodings':''},
    {'nome':'zeze di camargo', 'img':'img/zeze.webp', 'encodings':''}
]

def gerar_encode():
    for morador in lista_moradores:
        morador['encodings'] = fr.face_encodings(fr.load_image_file(morador['img']))[0]

def compare_faces(encode):
    for morador in lista_moradores:
        result = fr.compare_faces([morador['encodings']], encode)

        if result[0]:
            return morador['nome']

    return 'desconhecido'

def insert_morador():
    ok, foto = video.read()

    nome = input('Digite o nome do morador: ')
    cv2.imwrite(f'img/{nome}.jpg', foto)

    novo_morador = {'nome':f'{nome}', 'img':f'img/{nome}.jpg', 'encodings':''}
    novo_morador['encodings'] = fr.face_encodings(fr.load_image_file(novo_morador['img']))[0]
    lista_moradores.append(novo_morador)


gerar_encode()

video = cv2.VideoCapture(1)

while True:
    ok, frame = video.read()

    try:
        bboxes = fr.face_locations(frame)[0]
        cv2.rectangle(frame, (bboxes[3], bboxes[0]), (bboxes[1], bboxes[2]), (0, 255, 0), 2)

        encode_recognition = fr.face_encodings(frame)[0]
        name = compare_faces(encode_recognition)

        cv2.putText(frame, name, (bboxes[3], bboxes[0] - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 1)

    except:
        cv2.imshow('live', frame)

    cv2.imshow('live', frame)
    keyCode = cv2.waitKey(1)
    if keyCode == 27:
        break
    elif keyCode == 105:
        print('Aproxime o seu rosto da camera')
        insert_morador()


cv2.destroyAllWindows()
