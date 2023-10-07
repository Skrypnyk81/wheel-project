migration:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

reload:
	sudo supervisorctl reload
	sudo systemctl reload nginx