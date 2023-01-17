import re

lista_nombres=['Ana Gómes', 
                'María Martín',
                'Sandra López', 
                'Santiago Martin',
                'Sandra Rodriguez', ]

for e in lista_nombres:
#    if re.findall('^Sandra',e):
#       print  (e)

#    if re.findall('Martin$',e):
#        print (e)

#    if re.findall('Mart[ií]n',e):
#        print (e)

    if re.findall('^[J-Mj-m]',e):
        print (e)