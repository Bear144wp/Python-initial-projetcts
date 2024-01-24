car_velocity = 101 #km/h
car_local = 159 #km que o carro está

limite_radar = 100
local_radar = 159
range_radar = 2

parametro1 = car_velocity > limite_radar
parametro2 = car_local >= local_radar - range_radar and car_local <= local_radar + range_radar

if parametro1 and parametro2:
    print('Voce foi multado')

else: 
    print('Voce nao foi multado')