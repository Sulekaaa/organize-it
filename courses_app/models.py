from django.db import models

# Create your models here.
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    office = models.CharField(max_length=255)
    office_details = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=6)
    credits = models.IntegerField()
    TYPE_CHOICES = (
        ('in-person', 'In-person'),
        ('online', 'Online')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    ta_info = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.name

class CourseMeeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course_id} - {self.day} - {self.start_time}"

class CourseAttachments(models.Model):
    attachments_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField()

    def __str__(self):
        return f"{self.course_id} - {self.file.name}"