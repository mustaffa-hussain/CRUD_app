from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_pymongo import PyMongo

from database_fn import database
db = database()
