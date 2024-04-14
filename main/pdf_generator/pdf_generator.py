from PIL import Image, ImageDraw, ImageFont
import os 
import random 

class Main: 
    def make_pdf(self,name, code): #генерирует сертификат в пнг
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        image = Image.open(BASE_DIR + "\pdf_generator\A4.png")
        drawer = ImageDraw.Draw(image)
        name_font = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Medium.ttf",47)
        code_font = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Regular.ttf",15)
        name_font_1 = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Medium.ttf",44)
        name_font_2 = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Medium.ttf",39)
        name_font_3 = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Medium.ttf",35)
        name_font_4 = ImageFont.truetype(BASE_DIR + "\pdf_generator\Montserrat-Medium.ttf",32)
        

        if len(name) < 14:

            drawer.text((330-(20*len(name)), 510), name.upper(), font= name_font, fill="white")
        
        elif len(name) == 14 or len(name) == 15: 
            drawer.text((355-(20*len(name)), 510), name.upper(), font= name_font_1, fill="white")

        elif len(name) == 16:
            drawer.text((350-(20*len(name)), 510), name.upper(), font= name_font_1, fill="white")

        elif len(name) == 17:
            drawer.text((365-(20*len(name)), 510), name.upper(), font= name_font_1, fill="white")

        elif len(name) == 18 or len(name) == 19: 
            drawer.text((410-(20*len(name)), 520), name.upper(), font= name_font_2, fill="white")

        elif len(name) == 20: 
            drawer.text((440-(20*len(name)), 520), name.upper(), font= name_font_3, fill="white")

        elif len(name) == 20 or len(name) == 21: 
            drawer.text((440-(20*len(name)), 520), name.upper(), font= name_font_3, fill="white")
        
        elif len(name) == 22: 
            drawer.text((480-(20*len(name)), 520), name.upper(), font= name_font_4, fill="white")

        print(len(name))
        drawer.text((85, 772), code, font=code_font, fill = 'white')
        image = image.convert('RGB')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/filedownload/' + code + '.png'
        image.save(filepath)

    def generate_code(self):  #генерирует код для сертификата
        res = ''
        for i in range(20): 
            res += str(random.randint(0,9))
        return res