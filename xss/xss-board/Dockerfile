FROM nimmis/apache-php5
RUN apt-get update && \
    apt-get install nodejs && \
    apt-get install npm
COPY . /var/www/public
RUN echo "*/3 * * * * cron.sh" | crontab
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
