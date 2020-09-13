import os

import environ

from .basesettings import *  # noqa

env_file = os.path.join(BASE_DIR, ".env")  # noqa

SETTINGS_NAME = "application_settings"

if not os.path.isfile(".env"):
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm

    _, project = google.auth.default()

    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, SETTINGS_NAME, "latest")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")

        with open(env_file, "w") as f:
            f.write(payload)

env = environ.Env()
env.read_env(env_file)

is_Local = env("MODE") == "local"

if not is_Local:

    # Setting this value from django-environ
    SECRET_KEY = env("SECRET_KEY")

    ALLOWED_HOSTS = ["demo-django-rest-api-t7kdneksxa-uc.a.run.app"]

    # Default false. True allows default landing pages to be visible
    DEBUG = env("DEBUG")

    # Setting this value from django-environ
    DATABASES = {"default": env.db()}

    INSTALLED_APPS += ["storages"]  # noqa # for django-storages
    if "config" not in INSTALLED_APPS:
        INSTALLED_APPS += ["config"]  # for custom data migration

    # Define static storage via django-storages[google]
    GS_BUCKET_NAME = env("GS_BUCKET_NAME")
    STATICFILES_DIRS = []
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    GS_DEFAULT_ACL = "publicRead"
