# 3-3
import math

def dist(x1, y1, x2, y2):
    return 6370.01 * math.acos(math.sin(math.radians(x1)) *
                        math.sin(math.radians(x2)) +
                        math.cos(math.radians(x1)) *
                        math.cos(math.radians(x2)) *
                        math.cos(math.radians(y1 - y2)))

def triangle(d1, d2, d3):
    s = (d1 + d2 + d3) / 2
    return (s*(s-d1)*(s-d2)*(s-d3))**0.5

Gwangju = 35.1768201, 126.7735892
Busan = 35.1645701, 129.0015892
Gangneung = 37.7637326, 128.8824475
Seoul = 37.565289, 126.8491259

Gw_Bu = dist(*Gwangju, *Busan)
Bu_Ga = dist(*Busan, *Gangneung)
Ga_Gw = dist(*Gangneung, *Gwangju)

Gw_Se = dist(*Gwangju, *Seoul)
Se_Ga = dist(*Seoul, *Gangneung)

answer = triangle(Gw_Bu, Bu_Ga, Ga_Gw) + triangle(Gw_Se, Se_Ga, Ga_Gw)
print("면적:", answer)
