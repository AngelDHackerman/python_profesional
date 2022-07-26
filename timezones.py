from datetime import datetime
import pytz  # ? Este nos permite trabajar con zonas horarias de diferentes paises

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)  # ? Si no se pasa 'bogota_timezone' como parametro, nos devuelve nuestra zona horaria o la hora universal
print(f'Bogota: {bogota_date.strftime("%d/%m/%Y, %H:%M:%S")}')