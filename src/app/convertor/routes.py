from flask import Blueprint

upload_bp = Blueprint('upload-file', __name__, url_prefix='/upload')

@upload_bp.route('/')
def file_upload():
    return "file conversion"