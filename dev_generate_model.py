import os

from apps.utils.generate_model import GenerateModel

if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'app'
    model_name = 'test'
    GenerateModel(app_dir, model_name)