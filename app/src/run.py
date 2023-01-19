import os
from resources.factories.application import create_app
from resources.factories.celery import create_celery


app = create_app()

if __name__ == "__main__":
    create_celery(app)
    print(os.environ.get('PORT'),flush=True)
    app.run(threaded=True, port=os.environ.get('PORT'))