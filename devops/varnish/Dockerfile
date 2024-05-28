# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="patricia <patricia.yamasaki@tre-ms.jus.br>" \
      org.label-schema.name="trems-varnish" \
      org.label-schema.description="Treinamento TRE-MS Varnish image." \
      org.label-schema.vendor="patricia"

COPY etc/varnish.vcl /etc/varnish/default.vcl
