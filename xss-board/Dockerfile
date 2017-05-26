FROM nimmis/apache-php5
RUN apt-get update && \
    apt-get install nodejs && \
    apt-get install npm
COPY . /var/www/public
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN echo "*/3 * * * * cron.sh" | crontab
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
