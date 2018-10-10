import base64

def main():

    output = img_to_string("pinkGuy.jpg")

    print(output)

    string_to_img(output, 'jpg')


def img_to_string(imagePath):
    with open(imagePath, 'rb') as imageFile:
        return str(base64.b64encode(imageFile.read()))

    raise IOError

def string_to_img(string, fileType):

    with open('output.' + fileType, 'wb') as file:

        file.write(base64.b64decode(string))

        return file

    raise IOError


if __name__ == '__main__':main()