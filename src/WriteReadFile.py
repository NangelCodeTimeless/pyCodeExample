from tqdm import tqdm
import subprocess

p_read = "C:\\Users\\Nahum\\Desktop\\Respirar.mp4"
p_write = "C:\\Users\\Nahum\\Desktop\\PyProject\\Respirar2.mp4"

try:
    input_file = open(p_read, mode="rb")
    output_file = open(p_write, mode="wb")
except OSError:
    print("El Archivo no se puede abrir...")
else:
    list_bytes = list(input_file)
    progress_bar = tqdm(list_bytes)
    for byte in progress_bar:
        progress_bar.set_description("Copy file")
        j = output_file.write(byte)
    '''ABRIR LA CARPETA DONDE SE UBICA EL ARCHIVO'''
    subprocess.Popen(f'explorer /select, "{p_write}"')
    input_file.close()
    output_file.close()







