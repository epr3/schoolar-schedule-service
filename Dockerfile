FROM php:7-fpm-alpine

RUN docker-php-ext-install mbstring tokenizer mysqli pdo_mysql

WORKDIR /var/www/html

ADD . .

RUN touch ./db.sqlite
RUN chgrp -R www-data ./db.sqlite
RUN chmod -R 775 ./db.sqlite

RUN php artisan migrate
