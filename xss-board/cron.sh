#! /bin/bash
node /var/www/public/bot.js >> /tmp/xss-bot.log
rm /var/www/public/comments/*
