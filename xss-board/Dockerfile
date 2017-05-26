FROM nimmis/apache-php5
RUN apt-get update -y && \
    apt-get install nodejs -y && \
    apt-get install npm -y
RUN npm install zombie
COPY . /var/www/public
WORKDIR /var/www/public
RUN npm install zombie
RUN chmod +777 /var/www/public/comments
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN cat cron.sh | crontab
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
