from django.core.files.uploadedfile import SimpleUploadedFile


test_image = SimpleUploadedFile(
    'test_image.jpg', 
    content= open('test_jpg.jpg', 'rb').read(), 
    content_type='image/jpeg'
)