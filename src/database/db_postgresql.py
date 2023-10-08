from decouple import config
import psycopg
from flask import Flask, request, jsonify


def get_connection():
    try:
        return psycopg.connect(
            host=config('POSTGRESQL_HOST'),
            port=config('POSTGRESQL_PORT'),
            dbname=config('POSTGRESQL_DB'),
            user=config('POSTGRESQL_USER'),
            password=config('POSTGRESQL_PASSWORD')
        )
    except Exception as ex:
        print(ex)

