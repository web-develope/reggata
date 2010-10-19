# -*- coding: utf-8 -*-
'''
Created on 11.10.2010

@author: vlkv
'''
import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from helpers import tr
import string


Base = declarative_base()


class User(Base):
    '''
    Пользователь системы reggata.
    '''
    __tablename__ = "users"
    
    login = sqa.Column(sqa.String, primary_key=True)
#    name = sqa.Column(sqa.String)
    password = sqa.Column(sqa.String)
#    notes = sqa.Column(sqa.String)
    group = sqa.Column(sqa.Enum("USER", "ADMIN"), nullable=False, default="USER")
    
    def check_valid(self):
        if self.login is None or self.login=="":
            raise ValueError("Поле login не должно быть пустым.")        
        return True



#Таблица связей Tag и Item
tags_items = sqa.Table('tags_items', Base.metadata,
    sqa.Column('item_id', sqa.Integer, ForeignKey('items.id'), primary_key=True),
    sqa.Column('tag_name', sqa.String, primary_key=True),
    sqa.Column('tag_user_login', sqa.String, primary_key=True),
    ForeignKeyConstraint(['tag_name', 'tag_user_login'], ['tags.name', 'tags.user_login'])
)



class Item(Base):
    '''
    Элемент (запись, объект) хранилища.
    '''
    __tablename__ = "items"
    
    id = sqa.Column(sqa.Integer, primary_key=True)
    title = sqa.Column(sqa.String, nullable=False)
    notes = sqa.Column(sqa.String)
    user_login = sqa.Column(sqa.String, ForeignKey("users.login"))
    
    #пользователь-владелец данного элемента
    user = relationship(User, backref=backref("items"))
    
    #список связанных файлов/ссылок URL
    data_refs = relationship("DataRef", order_by="DataRef.order_by_key", backref=backref("item"))
    
    #tags - список связанных тегов
    tags = relationship("Tag", secondary=tags_items, backref="items")
    
    #field_vals - список связанных полей
    field_vals = relationship("FieldVal", backref="item")

    def __init__(self, user_login="", title=""):
        self.user_login = user_login
        self.title = title
        #TODO
        
    def check_valid(self):
        '''Проверяет, что состояние объекта допустимое. Связи с другими объектами не учитываются.'''
        if self.title == "" or self.title is None:
            raise Exception(tr("Необходимо указать название (поле title) элемента."))        
        return True
        
        
        
class DataRef(Base):
    '''
    Ссылка на файл или URL.
    '''
    __tablename__ = "data_refs"
    
    url = sqa.Column(sqa.String, primary_key=True)
    type = sqa.Column(sqa.Enum("FILE", "URL"), nullable=False)
    hash = sqa.Column(sqa.String)
    hash_date = sqa.Column(sqa.DateTime)
    size = sqa.Column(sqa.Integer, nullable=False, default=0)    
    order_by_key = sqa.Column(sqa.Integer)
    item_id = sqa.Column(sqa.Integer, ForeignKey("items.id"))
    user_login = sqa.Column(sqa.String, ForeignKey("users.login"))
    
    user = relationship(User)

    def __init__(self, url=""):
        self.url = url
        
        
        
        
class Tag(Base):
    '''
    Тег (ключевое слово), описывающий элементы хранилища.
    '''
    __tablename__ = "tags"
    
    name = sqa.Column(sqa.String, primary_key=True)
    user_login = sqa.Column(sqa.String, ForeignKey("users.login"), primary_key=True)
    
    #TODO Нужно сделать синонимы для тегов
    
    #Пользователь, кто создал данный тег
    user = relationship(User, backref=backref("tags"))

    def __init__(self):
        '''
        Constructor
        '''
        
class Field(Base):
    '''
    Поле вида ключ=значение, описывающее элементы хранилища.
    '''
    __tablename__ = "fields"
    
    #TODO Нужно сделать синонимы для полей
    
    name = sqa.Column(sqa.String, primary_key=True)
    user_login = sqa.Column(sqa.String, ForeignKey("users.login"), primary_key=True)
    value_type = sqa.Column(sqa.Enum("STRING, NUMBER"), nullable=False, default="STRING")
    

class FieldVal(Base):
    '''
    Значение поля, связанное с элементом хранилища.
    '''
    __tablename__ = "fields_items"
    __table_args__ = (ForeignKeyConstraint(["field_name", "field_user_login"], ["fields.name", "fields.user_login"]),
        {} #{} обязательно нужны, даже если внутри них - пусто
        )
    item_id = sqa.Column(sqa.Integer, ForeignKey("items.id"), primary_key=True)
    field_name = sqa.Column(sqa.String, primary_key=True)
    field_user_login = sqa.Column(sqa.String, primary_key=True)
    field_value = sqa.Column(sqa.String, nullable=False, default="")

    field = relationship(Field)
    
    
    
    


#TODO сделать классы групп полей и тегов




