# -*- coding: utf-8 -*-
from datetime import datetime
from mongoengine import (connect, Document, StringField,
                         IntField, DateTimeField, ListField)
from dateutil.relativedelta import relativedelta


connect('another-one')


class OneIssue(Document):
    issue_number        = IntField()
    create_time         = DateTimeField()
    articles            = ListField(StringField())

    @classmethod
    def create(cls, issue_number=None, articles=None):
        if not articles:
            return
        one_issue = cls.get_issue_by_issue_number(issue_number=issue_number) or \
                    cls(issue_number=issue_number, articles=articles)
        one_issue.create_time = one_issue.gen_time()
        one_issue.save()

    @classmethod
    def get_issue_by_issue_number(cls, issue_number=0):
        return cls.objects(issue_number=issue_number).first()

    def gen_time(self):
        return datetime(2012, 6, 11) + relativedelta(days=(self.issue_number-1))
