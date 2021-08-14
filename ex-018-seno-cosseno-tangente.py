import math
an = float(input('Digite um ângulo:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}' .format(an, sen, cos, tan))