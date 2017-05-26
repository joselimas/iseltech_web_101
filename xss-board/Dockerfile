FROM nimmis/apache-php5
RUN apt-get update -y && \
    apt-get install nodejs -y && \
    apt-get install npm -y
RUN npm install zombie
COPY . /var/www/public
RUN chmod +x cron.sh
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN echo "*/3 * * * * /var/www/public/cron.sh" | crontab
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
