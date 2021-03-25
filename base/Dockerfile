FROM alpine:3.13

RUN set -ex && \
    apk add --update --no-cache git gcc musl-dev make argp-standalone
WORKDIR /build

RUN git clone https://github.com/KelabDev/code-runner.git .
RUN make runner

FROM alpine:3.13

COPY --from=0 /build/runner /tool/
COPY entrypoint.sh /tool/

ENV PATH="/tool:${PATH}"

WORKDIR /workspace
ENTRYPOINT [ "entrypoint.sh" ]
