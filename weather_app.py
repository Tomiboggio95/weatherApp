from tkinter import *
import requests

#2e81d77fcdc4e56b53c55b8ad9f065e4
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Se hace una peticion al servidor_ la respuesta se recive en formato JSON que es parecido a Python
def mostrar_respuesta (clima):
    try:
        nombre_ciudad = clima ['name']
        desc = clima ['weather'][0]['description']
        temp = clima ['main']['temp']

        ciudad ['text'] = nombre_ciudad
        temperatura ['text']= str (int (temp)) + '°C'
        descripcion ['text'] = desc
    except:
        ciudad ['text'] = 'Intenta nuevamente'


def clima_json (ciudad):
    try:
        API_key = '2e81d77fcdc4e56b53c55b8ad9f065e4'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        parametros = {'APPID': API_key, 'q': ciudad, 'units': 'metric', 'lang':'es'}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        mostrar_respuesta (clima)

    except:
        print ('Error')

    #Acceso al indice 0 porque solo se precisa un elemento de Weather]

ventana = Tk()
ventana.title('Aplicación del Clima')
ventana.geometry ('350x550')

texto_ciudad = Entry (ventana, font = ('courier', 20, 'normal'), justify = 'center')
texto_ciudad.pack (padx = 30, pady = 30)

obtener_clima = Button(ventana, text = 'Obtener clima', font = ('Courier', 20, 'normal'), command = lambda: clima_json (texto_ciudad.get()))
obtener_clima.pack ()

ciudad = Label (font = ('courier', 20, 'normal'))
ciudad.pack (padx = 20, pady = 20)

temperatura = Label (font = ('courier', 20, 'normal'))
temperatura.pack (padx = 30, pady = 30)

descripcion = Label (font = ('courier', 15, 'normal'))
descripcion.pack (padx = 10, pady = 10)


ventana.mainloop()
