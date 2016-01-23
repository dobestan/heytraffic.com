# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python heytraffic/manage.py makemigrations
	python heytraffic/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls heytraffic/ | grep -v -e 'manage.py' | xargs -I{} rm -rf heytraffic/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 heytraffic/
	heytraffic/manage.py test heytraffic/ -v 2


# target: collectstatic - manages all static files including scss, es6 compile and django collectstatic
collectstatic:
	grunt bowercopy
	grunt compass
	grunt browserify
	# heytraffic/manage.py collectstatic --noinput
