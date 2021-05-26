FROM judgoo/base-alpine:v0.0.2 as base_builder
FROM alpine:3.13
RUN apk add --no-cache perl
COPY --from=base_builder /tool/ /tool/
ENV PATH="/tool:${PATH}"
WORKDIR /workspace
ENTRYPOINT ["Judger"]