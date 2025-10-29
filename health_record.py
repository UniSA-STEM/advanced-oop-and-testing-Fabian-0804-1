"""
File: health_record.py
Description: Represents an animal health record with issue details, severity, and treatment information
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class HealthRecord:
    def __init__(self, issue, severity, date, treatment=None, under_treatment=False, notes=None):
        self.__issue = issue
        self.__severity = severity
        self.__date = date
        self.__treatment = treatment
        self.__under_treatment = under_treatment
        self.__notes = notes

    def get_issue(self):
        return self.__issue

    def get_severity(self):
        return self.__severity

    def get_date(self):
        return self.__date

    def get_treatment(self):
        return self.__treatment

    def get_under_treatment(self):
        return self.__under_treatment

    def get_notes(self):
        return self.__notes

    def set_issue(self, value):
        if not value:
            raise ValueError("Issue cannot be empty.")
        self.__issue = str(value)

    def set_severity(self, value):
        allowed = ("low", "medium", "high")
        if not value or str(value).lower() not in allowed:
            raise ValueError(f"Severity must be one of: {', '.join(allowed)}.")
        self.__severity = str(value).lower()

    def set_date(self, value):
        if not value:
            raise ValueError("Date cannot be empty.")
        self.__date = str(value)

    def set_treatment(self, value):
        self.__treatment = None if value is None else str(value)

    def set_under_treatment(self, value):
        if not isinstance(value, bool):
            raise ValueError("under_treatment must be True or False.")
        self.__under_treatment = value

    def set_notes(self, value):
        self.__notes = None if value is None else str(value)

    issue = property(get_issue, set_issue)
    severity = property(get_severity, set_severity)
    date = property(get_date, set_date)
    treatment = property(get_treatment, set_treatment)
    under_treatment = property(get_under_treatment, set_under_treatment)
    notes = property(get_notes, set_notes)