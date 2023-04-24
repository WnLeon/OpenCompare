from flask import Blueprint
from flask import jsonify
from module.storage.db import opencompare

gallery = Blueprint("images_display", __name__)

def get_images(tb):
    # Query the database to get the image URLs
    images = tb.query.all()
    # urls = [{image.title: image.url} for image in images]
    urls = [image.url for image in images]
    # Return the image URLs as a JSON response
    return jsonify({'images': urls})
    #return jsonify({'images': urls})

@gallery.route('/imagesmeinv') 
def img_1():
    return get_images(tb=opencompare.Imagemeinv)


@gallery.route('/imagesfengjing')
def img_2():
    return get_images(tb=opencompare.Imagefengjing)
# def get_images():
#     # Query the database to get the image URLs
#     images = opencompare.Imagefengjing.query.all()
#     # urls = [{image.title: image.url} for image in images]
#     urls = [image.url for image in images]
#     # Return the image URLs as a JSON response
#     return jsonify({'images': urls})
#     #return jsonify({'images': urls})

@gallery.route('/imagesyuanchuang')
def img_3():
    return get_images(tb=opencompare.Imageyuanchuang)
# def get_images():
#     # Query the database to get the image URLs
#     images = opencompare.Imageyuanchuang.query.all()
#     # urls = [{image.title: image.url} for image in images]
#     urls = [image.url for image in images]
#     # Return the image URLs as a JSON response
#     return jsonify({'images': urls})
#     #return jsonify({'images': urls})

@gallery.route('/imagesdongwu')
def img_4():
    return get_images(tb=opencompare.Imagedongwu)
# def get_images():
#     # Query the database to get the image URLs
#     images = opencompare.Imagedongwu.query.all()
#     # urls = [{image.title: image.url} for image in images]
#     urls = [image.url for image in images]
#     # Return the image URLs as a JSON response
#     return jsonify({'images': urls})
#     #return jsonify({'images': urls})