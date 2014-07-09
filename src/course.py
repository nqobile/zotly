"""
course.py defines the course objects and class objects and their methods
"""
__author__ = 'Ian Stephenson'


class Course():
    def __init__(self, department=None, course_number=None, description=None, classes=[]):
        self.__department = department
        self.__course_number = course_number
        self.__description = description
        self.__classes = classes

    def get_department(self):
        return self.__department

    def get_course_number(self):
        return self.__course_number

    def get_description(self):
        return self.__description

    def get_list_of_classes_for_course(self):
        return self.__classes


class Class():
    def __init__(self, code, kind, section, units, instructor, time, place, final, max_number_allowed_to_enroll,
                 number_currently_enrolled, number_currently_waitlisted, number_of_enrollment_requests,
                 number_of_slots_reserved, enrollment_restrictions, status):
        self.__code = code
        self.__kind = kind
        self.__section = section
        self.__units = units
        self.__instructor = instructor
        self.__time = time
        self.__place = place
        self.__final = final
        self.__max_number_allowed_to_enroll = max_number_allowed_to_enroll
        self.__number_currently_enrolled = number_currently_enrolled
        self.__number_currently_waitlisted = number_currently_waitlisted
        self.__number_of_enrollment_requests = number_of_enrollment_requests
        self.__number_of_slots_reserved = number_of_slots_reserved
        self.__enrollment_restrictions = enrollment_restrictions
        self.__status = status

    def get_class_code(self):
        return self.__code

    def get_type_of_class(self):
        return self.__kind

    def get_section(self):
        return self.__section

    def get_number_of_units(self):
        return self.__units

    def get_instructor(self):
        return self.__instructor

    def get_meeting_time(self):
        return self.__time

    def get_meeting_place(self):
        return self.__place

    def get_date_of_final(self):
        return self.__final

    def get_max_number_of_students_allowed_to_enroll(self):
        return self.__max_number_allowed_to_enroll

    def get_number_of_students_currently_enrolled(self):
        return self.__number_currently_enrolled

    def get_number_of_students_currently_waitlisted(self):
        return self.__number_currently_waitlisted

    def get_number_of_enrollment_requests(self):
        return self.__number_of_enrollment_requests

    def get_number_of_slots_reserved(self):
        return self.__number_of_slots_reserved

    def get_enrollment_restrictions(self):
        return self.__enrollment_restrictions

    def get_status(self):
        return self.__status