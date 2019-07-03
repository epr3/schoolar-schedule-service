FROM php:7-fpm

RUN apt-get update -y && apt-get install -y nginx supervisor

RUN docker-php-ext-install mbstring tokenizer mysqli pdo_mysql

COPY ./containers/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY containers/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /database

RUN touch ./db.sqlite
RUN chgrp -R www-data /database
RUN chmod -R 775 /database

WORKDIR /var/www/html

ADD . .

# RUN php artisan migrate

EXPOSE 3000
