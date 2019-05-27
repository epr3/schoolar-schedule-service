FROM php:7-fpm-alpine

RUN docker-php-ext-install mbstring tokenizer mysqli pdo_mysql

WORKDIR /database

RUN touch ./db.sqlite
RUN chgrp -R www-data /database
RUN chmod -R 775 /database

WORKDIR /var/www/html

ADD . .

RUN php artisan migrate

EXPOSE 9000
