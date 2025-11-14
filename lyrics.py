import time
import sys

def print_lyrics():
    lyrics= [
        "Mien ab kyun hosh may ataa nai?",
        "Sukon ye dil kyun pataa nahi?",
        "kyun tarrun khud se ja thay waaday",
        "Ke ab yeh ishq nibhaana nahi?",
        "Mein morrun tum se jo ye chehra",
        "Dobaara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nhi?",
        "Soniyaa yun tera sharmaana.."]
    
    delays= [
        0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8,0.4,
    ]

    print ("* * *Pal Pal* * *\n")
    time.sleep(1.2)

    for i , line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i<len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(8.8)

print_lyrics()