- Referenced articles:
  - https://codelabs.developers.google.com/codelabs/cloud-run-django/index.html?index=..%2F..index#0

## Commands

### Local Setup

```sh
# Add local environment
$ echo MODE=local >> .env
```

### Create & Update
 
```
# Add module
$ poetry add {module_name}
$ poetry add -D {module_name}

# Rebuild
$ docker-compose build

# Create app
$ docker-compose run web python manage.py startapp {app_name}

# Create migration file
$ docker-compose run web python manage.py makemigrations {app_name}

# Migration
$ docker-compose run web python manage.py migrate

# Create admin
$ docker-compose run web python manage.py createsuperuser

# Start image
$ docker-compose up

# Stop image
$ docker-compose down

# Check image
$ docker-compose images
```

### Build & Migration & Deploy

```sh
# コンテナイメージのビルド
$ gcloud builds submit \
    --tag gcr.io/{PROJECT_ID}/{IMAGE_NAME} \
    --substitutions=_DB_USER={DATABASE_USER},_DB_PASS={DATABASE_PASSWORD}

# マイグレーション
$ gcloud builds submit \
    --config cloudmigrate.yaml \
    --substitutions _REGION={REGION}

# Cloud Run にデプロイ
$ gcloud run deploy {PROJECT_ID} \
    --platform managed \
    --region {REGION} \
    --image gcr.io/{PROJECT_ID}/{IMAGE_NAME} \
    --add-cloudsql-instances {PROJECT_ID}:{REGION}:{SQL_INSTANCE_NAME} \
    --allow-unauthenticated
```

### Factory boy

```sh
$ docker-compose -f docker-compose.local.yml run web python manage.py shell
```

```python
# add data
from books.factory import BookFactory
BookFactory.create_batch(10)

# check data
from books.models import Book
for x in Book.objects.all(): print('isbn={0}, title={1}, price={2}, publisher={3}, published={4}'.format(x.isbn, x.title, x.price, x.publisher, x.published))

```
