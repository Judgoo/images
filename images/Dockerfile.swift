FROM judgoo/base-debian:v0.0.1 as base_builder
FROM swift:5.3.3-focal
COPY --from=base_builder /tool/ /tool/
ENV PATH="/tool:${PATH}"
WORKDIR /workspace
ENTRYPOINT ["Judger"]
ENV PATH $PATH:/usr/lib/