FROM nimmis/apache-php5


RUN apt-get update -y
RUN apt-get install build-essential chrpath libssl-dev libxft-dev -y
RUN apt-get install libfreetype6 libfreetype6-dev -y
RUN apt-get install libfontconfig1 libfontconfig1-dev -y

WORKDIR /root
RUN export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
RUN tar xvjf $PHANTOM_JS.tar.bz2
RUN mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

COPY . /var/www/public
WORKDIR /var/www/public
RUN chmod +777 /var/www/public/comments
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
RUN while sleep 1; do phantomjs --ignore-ssl-errors=true --local-to-remote-url-access=true --web-security=false --ssl-protocol=any phantbot.js; done;
