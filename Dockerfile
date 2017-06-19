FROM ccnmtl/django.base
RUN apt-get update && apt-get install -y fontconfig # phantomjs dependency
ADD wheelhouse /wheelhouse
ADD requirements /requirements
RUN /ve/bin/pip install --no-index -f /wheelhouse -r /wheelhouse/requirements.txt \
&& rm -rf /wheelhouse
WORKDIR /app
COPY . /app/
RUN /ve/bin/python manage.py test
EXPOSE 8000
ADD docker-run.sh /run.sh
ENV APP mediamachine
ENTRYPOINT ["/run.sh"]
CMD ["run"]
