def handle_uploaded_file(image, name):
    with open('/media/images/' + name, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)