FROM alpine:3.13

RUN set -ex && apk add --update --no-cache git gcc musl-dev make argp-standalone
WORKDIR /build

RUN git clone https://github.com/KelabDev/code-runner.git .
RUN make runner

FROM golang:alpine3.13

WORKDIR /build
RUN set -ex && apk add --update --no-cache git
RUN git clone https://github.com/Judgoo/Judger .
RUN go build -ldflags "-s -w" .

FROM alpine:3.13

COPY --from=0 /build/runner /tool/
COPY --from=1 /build/Judger /tool/

ENV PATH="/tool:${PATH}"

WORKDIR /workspace
ENTRYPOINT [ "Judger" ]
