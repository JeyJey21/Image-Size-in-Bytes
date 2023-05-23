import requests

def obtener_tamano_imagenes(urls):
    tamanos = []
    for url in urls:
        response = requests.head(url)
        if 'content-length' in response.headers:
            tamano_bytes = int(response.headers['content-length'])
            tamanos.append(tamano_bytes)
        else:
            tamanos.append(None)
    return tamanos

# Ejemplo de uso
lista_imagenes = [
    "https://www.nestleprofessional.com.mx/sites/default/files/styles/np_recipe_detail/public/srh_recipes/f478969e55d40c7a5bf396d198d4fe8d.png?itok=pdAQ0ePt",
    "https://www.nestleprofessional.com.mx/sites/default/files/styles/basic_image_desktop/public/2022-10/maxresdefault_1.png?h=c673cd1c&itok=DGLjnZ1X",
    "https://www.nestleprofessional.com.mx/sites/default/files/styles/np_recipe_detail/public/srh_recipes/4e5934167e03278c03311af6ba51ad9c.png?itok=R0rFLDRF",
    "https://www.nestleprofessional.com.mx/sites/default/files/styles/np_recipe_detail/public/srh_recipes/769a4a2119baee0acadde414c7ab386e.png?itok=cKwBLygy"
]
tamanos = obtener_tamano_imagenes(lista_imagenes)
for i, tamano in enumerate(tamanos):
    if tamano:
        print(f"El tamaño de la imagen {i+1} es de {tamano} bytes.")
    else:
        print(f"No se pudo determinar el tamaño de la imagen {i+1}.")