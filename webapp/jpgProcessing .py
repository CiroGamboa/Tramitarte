from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
def print_primer_apellido(text,role):
    if role=="comprador":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((90, 798),text,(0,0,0),font=font)
    if role=="propietario":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((90, 530),text,(0,0,0),font=font) 
def print_segundo_apellido(text,role):
    if role == "comprador":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((314, 798),text,(0,0,0),font=font) 
    if role == "propietario":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((314, 530),text,(0,0,0),font=font)    
def print_nombres(text,role):
    if role == "comprador":        
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((585, 798),text,(0,0,0),font=font)   
    if role ==  "propietario":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((585, 530),text,(0,0,0),font=font)    
def doc_type(text,role):
    if role == "comprador":        
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)
        if(text=="CC"):
            draw.text((90, 856),"X",(0,0,0),font=font)
    if role == "propietario":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)
        if(text=="CC"):
            draw.text((90, 580),"X",(0,0,0),font=font)    
def doc_number(text,role):
    if role == "comprador":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((675, 866),text,(0,0,0),font=font)
    if role == "propietario":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
        draw.text((675, 590),text,(0,0,0),font=font)
def marca(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((817, 201),text,(0,0,0),font=font)
    
def linea(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((990, 201),text,(0,0,0),font=font)

def combustible(tipo):
    if tipo == "GASOLINA":
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
        draw.text((1190, 213),"X",(0,0,0),font=font)
def colores(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((830, 260),text,(0,0,0),font=font)
def modelo(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((1354, 260),text,(0,0,0),font=font)
def cilindrada(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((1475, 260),text,(0,0,0),font=font)
def tipo_carroceria(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((820, 425),text,(0,0,0),font=font)

def n_motor(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((1242, 380),text,(0,0,0),font=font)

def n_chasis(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((1242, 424),text,(0,0,0),font=font)

def n_serie(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((1242, 481),text,(0,0,0),font=font)


    
def print_data(rol):
    if rol == "carro":
        marca(data[rol]["marca"])        
        linea(data[rol]["linea"])
        combustible(data[rol]["combustible"])
        colores(data[rol]["colores"])
        modelo(data[rol]["modelo"])
        cilindrada(data[rol]["cilindrada"])
        tipo_carroceria(data[rol]["tipo_carroceria"])
        n_motor(data[rol]["n_motor"])
        n_chasis(data[rol]["n_chasis"])
        n_serie(data[rol]["n_serie"])
        
    else:
        print_primer_apellido(data[rol]["primer_apellido"],rol)
        print_segundo_apellido(data[rol]["segundo_apellido"],rol)
        print_nombres(data[rol]["nombres"],rol)
        doc_type(data[rol]["tipo_doc"],rol)
        doc_number(data[rol]["num_doc"],rol)

def save_image(path):
    img.save(path)

with open('/home/cirogam22/Desktop/Tramitarte/webapp/config.json') as f:
    data = json.load(f)

img = Image.open("/home/cirogam22/Desktop/Tramitarte/webapp/traspaso.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
rol="propietario"
print_data(rol)
rol="comprador"
print_data(rol)
rol="carro"
print_data(rol)
save_image('/home/cirogam22/Desktop/Tramitarte/webapp/output/traspaso.jpg')

