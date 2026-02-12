from flask import Blueprint
from flask_restful import Api, Resource, request

upload_bp = Blueprint("convertor", __name__, url_prefix="/convertor")
api = Api(upload_bp)


class FileUploadResource(Resource):
    def post(self):
        file = request.files.get("file")

        return {"message": "file conversion done", "data": "file"}, 200


api.add_resource(FileUploadResource, "/upload/")
