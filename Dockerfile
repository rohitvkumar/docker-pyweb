FROM alpine:latest
MAINTAINER Rohit Valsakumar <rvalsakumar@tivo.com>

# ENTRYPOINT ["bash"]
COPY initialize.sh /usr/bin/
RUN initialize.sh

ENV PATH /app/bin:$PATH

COPY app /app

CMD [ "web_server.py" ]
