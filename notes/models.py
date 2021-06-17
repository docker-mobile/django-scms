from django.db import models

from schedule.models import Subject
from sis.models import ClassLevel, Student
from users.models import Teacher


class Topic(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GradedAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student.username


class Choice(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question


class ListOfSpecificExplanations(models.Model):
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField()
    examples = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.name} {self.sub_topic}"


class Concept(models.Model):
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField()
    image = models.ImageField(verbose_name=None, upload_to="concept images")
    list_of_explanations = models.ManyToManyField(ListOfSpecificExplanations)

    def __str__(self):
        return f"{self.name} {self.sub_topic}"


class Note(models.Model):
    _class = models.ForeignKey(ClassLevel, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.OneToOneField(Subject, related_name='period', on_delete=models.CASCADE)
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.ManyToManyField(Concept)

    def __str__(self):
        return f"{self.subject} {self.sub_topic}"
