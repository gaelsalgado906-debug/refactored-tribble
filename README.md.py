from PIL import Image, ImageDraw, ImageFont
import colorsys

def create_rainbow_gif(text_lines, filename="rainbow_gael.gif"):
    # Configuración de la imagen
    width, height = 800, 300
    frames = []
    num_frames = 30 # Cuadros para la animación
    
    # Intentar cargar una fuente, si no usa la básica
    try:
        font = ImageFont.truetype("arial.ttf", 35)
    except:
        font = ImageFont.load_default()

    print("Generando cuadros del arcoíris...")
    
    for f in range(num_frames):
        # Fondo oscuro estilo GitHub
        img = Image.new('RGB', (width, height), color='#0d1117')
        draw = ImageDraw.Draw(img)
        
        # Posición inicial del texto
        y_text = 60
        
        for i, line in enumerate(text_lines):
            # Calcular el color arcoíris basado en el frame y la línea
            hue = (f / num_frames + i / len(text_lines)) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 1, 1)
            color = tuple(int(c * 255) for c in rgb)
            
            # Dibujar cada línea de tu mensaje
            draw.text((50, y_text), line, font=font, fill=color)
            y_text += 60 # Espaciado entre líneas
            
        frames.append(img)

    # Guardar como GIF animado
    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        duration=100, # Velocidad (ms)
        loop=0
    )
    print(f"¡Listo! Archivo '{filename}' creado.")

# Tus frases personalizadas
my_messages = [
    "Hello! This is my website to say to you:",
    "Gael is busy, creating something too long...",
    "I'm going to school only after Friday!"
]

create_rainbow_gif(my_messages)
