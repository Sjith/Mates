#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, String, Integer, Float, Text, DateTime, Date, Time, func
from sqlalchemy.orm import relationship, backref
from database import db

class User(db.Model):
    uid = Column(String(16), nullable=False)    #微博id
    screen_name = Column(String(32), nullable=False)   #微博用户名
    description = Column(Text(100))    #微博一句话简介
    gender = Column(String(1), nullable=False, default='n')    #m,f,n(未知)
    profile_image_url = Column(String(100))    #用户头像地址（小头像)
    avatar_large = Column(String(100))    #用户头像地址（大头像)
    college_id = Column(Integer, ForeignKey("college.id", onupdate="CASCADE"))
    college = relationship("College", backref="user")
    join_time = Column(DateTime, default=func.now(), nullable=False)   #首次登录时间
    favourite_activities = relationship("Activity",
                    secondary='favourite',
                    backref="favourited_users")

    def __repr__(self):
        
        return str(self.__dict__)
        
class Activity(db.Model):
    title = Column(String(20), nullable=False)    #活动名
    description = Column(Text, nullable=False)    #活动简介
    category_id = Column(Integer, ForeignKey("category.id", onupdate="CASCADE"), nullable=False)    #活动分类
    category = relationship("Category", backref="activity")
    city_id = Column(Integer, ForeignKey("city.id", onupdate="CASCADE"), nullable=False)  #城市名
    city = relationship("City", backref="activity")
    college_id = Column(Integer, ForeignKey("college.id", onupdate="CASCADE"), nullable=False)   
    college = relationship("College", backref="activity")
    address = Column(String(50), nullable=False)    #详细地址
    poster_url = Column(String(100), nullable=False)    #活动海报地址（原尺寸）
    poster_small_url = Column(String(100), nullable=False)    #活动海报（小尺寸）
    time_type = Column(Integer, nullable=False)    #活动时间类型——单一时间、连续时间、自定义时间
    lat = Column(Float)    #纬度
    lon = Column(Float)    #经度
    creator_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE"), nullable=False)  #创建人id
    creator = relationship("User", backref="activity")
    create_time = Column(DateTime, default=func.now(), nullable=False)    #活动创建时间
    

class Category(db.Model):
    name = Column(String(20), nullable=False)   #活动类型名称


class Favourite(db.Model):
    user_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE"), nullable=False)     #用户id
    activity_id = Column(Integer, ForeignKey("activity.id", onupdate="CASCADE"), nullable=False)    #活动id
    favourited_time = Column(DateTime, default=func.now(), nullable=False)   #加星时间


class Time(db.Model):
    activity_id = Column(Integer, ForeignKey("activity.id", onupdate="CASCADE"), nullable=False)    #活动id
    activity = relationship("Activity", backref="time")
    date_begin = Column(Date, nullable=False)    #开始日期
    date_end = Column(Date, nullable=False)    #结束日期
    time_begin = Column(Time, nullable=False)    #开始时间
    time_end = Column(Time, nullable=False)    #结束时间


class College(db.Model):
    name = Column(String(30), nullable=False)    #学校名称
    city_id = Column(Integer, ForeignKey("city.id", onupdate="CASCADE"), nullable=False)
    city = relationship("City", backref="college")
    address = Column(String(60))    #学校地址
    lat = Column(Float)    #纬度
    lon = Column(Float)    #经度


class City(db.Model):
    name = Column(String(50), nullable=False)    #城市名称
    province_id = Column(Integer, ForeignKey("province.id", onupdate="CASCADE"), nullable=False)    #省id
    province = relationship("Province", backref="city")


class Province(db.Model):
    name = Column(String(50), nullable=False)    #省名



