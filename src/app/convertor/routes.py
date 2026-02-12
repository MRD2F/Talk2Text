from flask import Blueprint
from flask_restful import Api, Resource, request

from app.convertor.service import FileService

upload_bp = Blueprint("convertor", __name__, url_prefix="/convertor")
api = Api(upload_bp)


class FileUploadResource(Resource):
    def post(self):
        allowed_extensions = ["mp3", "wav", "ogg"]
        file_service = FileService(allowed_extensions, 100)
        return file_service.convert(request.files.get("file"))


api.add_resource(FileUploadResource, "/upload/")
