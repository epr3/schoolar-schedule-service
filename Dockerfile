FROM php:7-fpm-alpine
# lumen packages
RUN docker-php-ext-install mbstring tokenizer mysqli pdo_mysql

WORKDIR /var/www/html/app/public
