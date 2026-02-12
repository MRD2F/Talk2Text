from flask import Blueprint
from flask_restful import Api, Resource, request

from app.convertor.service import FileService

upload_bp = Blueprint("convertor", __name__, url_prefix="/convertor")
api = Api(upload_bp)


class FileUploadResource(Resource):
    def post(self):
        file = FileService("mp3", 1000)
        return file.convert(request.files.get("file"))


api.add_resource(FileUploadResource, "/upload/")
