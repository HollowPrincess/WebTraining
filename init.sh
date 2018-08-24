#nginx conf
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#gunicorn conf
#sudo rm /etc/gunicorn.d/test
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo rm /etc/gunicorn.d/ask
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello.wsgi:application
sudo gunicorn -c /home/box/web/etc/gunicorn_django.conf wsgi:application

#sudo ln -s /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
#sudo /etc/init.d/gunicorn restart
