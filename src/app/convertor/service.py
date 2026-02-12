class FileService:
    def __init__(self, allowed_extensions, max_size_mb):
        self.allowed_extensions = allowed_extensions
        self.max_size_mb = max_size_mb

    def validate(self, file):
        if not file:
            return {"error": "Missing file"}, 400

    def convert(self, file):
        self.validate(file)
        return f"{file} converted"
