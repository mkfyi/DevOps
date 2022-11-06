FROM alpine:3.16 AS builder

ENV BUILD_DEPS="gettext"  \
    RUNTIME_DEPS="libintl"

RUN set -xe \
  && apk add --update $RUNTIME_DEPS \
  && apk add --virtual build_deps $BUILD_DEPS \
  && cp /usr/bin/envsubst /usr/local/bin/envsubst

FROM php:8.1-fpm-alpine

RUN set -xe \
  && apk add \
    nginx \
    supervisor \
  && curl -sS https://getcomposer.org/installer | php -- \
     --install-dir=/usr/local/bin \
     --filename=composer \
     --2 \
  && rm /etc/nginx/http.d/default.conf \
  && rm /etc/nginx/nginx.conf \
  && mkdir -p /var/{lib,tmp,log}/nginx

COPY --from=builder /usr/local/bin/envsubst /usr/local/bin/
COPY --from=builder /usr/lib/libintl.so.8 /usr/lib/
COPY conf/etc /etc
COPY conf/usr /usr

EXPOSE 8000

ENV NGINX_BUILD_TEMPLATES=1 \
    NGINX_DEFAULT_SERVER_ROOT='/var/www/html' \
    SUPERVISOR_CONFIG_FILE="/etc/supervisor/conf.d/supervisord.conf"

ENTRYPOINT ["/usr/local/bin/mkilian-docker-entrypoint"]
