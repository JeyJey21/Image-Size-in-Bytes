# Image-Size-in-Bytes
Code used for SEO, to get the size of the images in bytes 

To install the 'requests' module, you can use the following command in your command prompt or terminal:

pip install requests

Make sure you have Python and pip (Python package installer) installed on your system, and that they are properly configured in your system's environment variables. After executing the command, pip will download and install the 'requests' module from the Python Package Index (PyPI).
Note: If you're using a virtual environment, make sure it is activated before running the command to ensure that the module is installed within the correct environment.

The code you provided is a Python script that utilizes the 'requests' module to obtain the size of images from a list of URLs.

Here's a breakdown of how the code works:

  1. The first line imports the 'requests' module, which is a popular third-party library used for making HTTP requests in Python.
  2. The obtener_tamano_imagenes(urls) function takes a list of URLs as input and returns a list of sizes (in bytes) corresponding to each URL.
  3. Inside the function, a loop iterates over each URL in the urls list.
  4. For each URL, the script sends an HTTP HEAD request using requests.head(url). The HEAD method retrieves the response headers without retrieving the entire content of the URL.
  5. The response object is stored in the response variable.
  6. The code checks if the 'content-length' header is present in the response headers using the condition 'content-length' in response.headers.
  7. If the 'content-length' header is found, it means that the size of the image is provided in the response.
     The code extracts the value of the 'content-length' header using response.headers['content-length'] and converts it to an integer using int(). 
  9. The size of the image in bytes is then appended to the tamanos list using tamanos.append(tamano_bytes).
  10. If the 'content-length' header is not present in the response headers, the code appends None to the tamanos list, indicating that the size of the image could not be determined.
  11. After iterating through all the URLs, the tamanos list is returned from the function.
  12. The code provides an example usage by creating a list of image URLs (lista_imagenes) and calling the obtener_tamano_imagenes function with this list.
  13. The returned list of sizes is stored in the tamanos variable.
  14. Finally, a loop iterates over the tamanos list using enumerate() to access both the index (i) and the size (tamano) of each image.
      It prints the size of each image if it was determined or a message indicating that the size couldn't be determined if it is None.

Overall, this script retrieves the sizes of images from a list of URLs using the 'requests' module and provides information about the size of each image.
