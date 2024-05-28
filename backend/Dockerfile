# syntax=docker/dockerfile:1
ARG PLONE_VERSION
FROM plone/server-builder:${PLONE_VERSION:-6.0.11} as builder

WORKDIR /app

# Add local code
COPY . .

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    sed -i 's/-e src\/trems\[test\]/src\/trems/g' mx.ini
    bin/mxdev -c mx.ini
    bin/pip install -r requirements-mxdev.txt
    bin/python /compile_mo.py
    rm -Rf src/
EOT

FROM plone/server-prod-config:${PLONE_VERSION:-6.0.11}

LABEL maintainer="patricia <patricia.yamasaki@tre-ms.jus.br>" \
      org.label-schema.name="trems-backend" \
      org.label-schema.description="Treinamento TRE-MS backend image." \
      org.label-schema.vendor="patricia"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    set -e
    ln -s /data /app/var
EOT
