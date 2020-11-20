FROM postgres:13

COPY ./data/* /var/lib/postgresql/

COPY init.sql /docker-entrypoint-initdb.d/
