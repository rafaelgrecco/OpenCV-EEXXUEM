import cv2 

imagem = cv2.imread('/home/rafael/Documentos/OpenCV/Imagens/fruta.jpg')
cv2.imshow('Imagem', imagem)

print(imagem.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

