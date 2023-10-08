migration:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver --settings=wheel.local_settings

reload:
	sudo supervisorctl reload
	sudo systemctl reload nginx