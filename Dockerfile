FROM        seongwonhan88/eb-fc-airbnb:base
ENV         DJANGO_SETTINGS_MODULE  config.settings.production
ENV         LANG                    C.UTF-8
# 전체 소스코드 복사
COPY        ./   /srv/project
WORKDIR     /srv/project

# 프로세스를 실행할 명령
WORKDIR     /srv/project/app
RUN         python3 manage.py collectstatic --noinput

# delete default Nginx and copy my link setup
RUN         rm -rf  /etc/nginx/sites-available/* && \
            rm -rf  /etc/nginx/sites-enabled/* && \
            cp -f   /srv/project/.config/app.nginx \
                    /etc/nginx/sites-available/ && \
            ln -sf  /etc/nginx/sites-available/app.nginx \
                    /etc/nginx/sites-enabled/app.nginx

# supervisor설정파일 복사
RUN         cp -f   /srv/project/.config/supervisord.conf \
                    /etc/supervisor/conf.d/

# 80번 포트 개방
EXPOSE      80

# Command로 supervisor실행
CMD         supervisord -n