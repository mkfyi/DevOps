FROM alpine:3.16

WORKDIR /ansible

ADD . .

RUN apk add --no-cache \
  bash \
  openssh \
  python3 \
  ansible \
  sshpass
