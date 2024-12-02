import Imagem as im

I1 = im.ImagemPGM("ferrari.pgm")
I1.brilho("saida01.pgm",150)
I1.espelha("saida02.pgm")
I1.rotaciona90("saida03.pgm")


I2 = im.ImagemPPM("house.ppm")
I2.espelha("saida01.ppm")
I2.rotaciona90("saida02.ppm")
I2.brilha("saida03.ppm", 100)
