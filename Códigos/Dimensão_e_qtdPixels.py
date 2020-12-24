import cv2 

img = cv2.imread('/home/rafael/Documentos/OpenCV/Imagens/fruta.jpg')
print(img.shape)

"""
Para essa imagem vamos ter como resultado (403, 665, 3)
403 é referente a altura da imagem
665 é referente a largura da imagem
O número 3 se refere a quantidade de canais, são 3 pois estamos trabalhando com uma imagem RGB
Canais (Vermelho(red), Verde(Green), Azul(Blue))
"""