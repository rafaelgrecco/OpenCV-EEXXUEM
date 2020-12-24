import cv2 

imagem = cv2.imread('/home/rafael/Documentos/OpenCV/Imagens/Lenna.png')
imgTons_Cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem em Tons de Cinza', imgTons_Cinza)
cv2.imwrite('TonsdeCinza.png', imgTons_Cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()