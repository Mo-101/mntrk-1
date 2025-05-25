import os
import connexion # type: ignore

def create_app():
    app = connexion.App(__name__, specification_dir="src/swagger_server/swagger")
    # Set the environment variable for the OpenAPI specification
    os.environ["SWAGGER_SPEC"] = "mntrk.yaml"
    app.add_api("mntrk.yaml", pythonic_params=True)
    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=8000, debug=True)
