FROM nimmis/apache-php5
RUN apt-get update -y && \
    apt-get install nodejs -y && \
    apt-get install npm -y
COPY . /var/www/public
WORKDIR /var/www/public
RUN npm install zombie
RUN chmod +777 /var/www/public/*
RUN chmod +x /var/www/public/cron.sh
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN echo "*/3 * * * * /var/www/public/cron.sh" | crontab
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
