import os

from apps.utils.system_utils.generate_model import GenerateModel

if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'apps'
    model_name = 'hello'
    GenerateModel(app_dir, model_name)
