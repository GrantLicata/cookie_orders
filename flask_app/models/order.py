from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re

class Order:
    def __init__(self ,data):
        self.id = data['id']
        self.type = data['type']
        self.box_count = data['box_count']
        self.customer_name = data['customer_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookie_orders').query_db(query)
        data = []
        for item in results:
            data.append( cls(item) )
        return data

    @classmethod
    def get_order(cls , data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL('cookie_orders').query_db(query , data)
        data = []
        for item in results:
            data.append( cls(item) )
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (type ,box_count ,created_at, updated_at, customer_name) VALUES ( %(type)s , %(box_count)s , NOW() , NOW() , %(customer_name)s );"
        return connectToMySQL('cookie_orders').query_db( query, data )

    @classmethod
    def edit(cls, data):
        query = "UPDATE orders SET customer_name = %(customer_name)s, type = %(type)s, box_count = %(box_count)s, updated_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('cookie_orders').query_db( query, data )

    @staticmethod
    def validate_edit(data):
        is_valid = True # we assume this is true
        if len(data['customer_name']) < 1:
            flash("Customer name is required.")
            is_valid = False
        if len(data['type']) < 1:
            flash("Cookie type is required.")
            is_valid = False
        if int(data['box_count']) < 0:
            flash("Number of boxes is required.")
            is_valid = False
        return is_valid


    @staticmethod
    def validate_order(data):
        is_valid = True # we assume this is true
        if len(data['customer_name']) < 2:
            flash("Customer name is required.")
            is_valid = False
        if len(data['type']) < 2:
            flash("Cookie type is required.")
            is_valid = False
        if int(data['box_count']) < 0:
            flash("Number of boxes is required.")
            is_valid = False
        return is_valid