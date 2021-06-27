from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    interviewer = models.BooleanField(default=False, db_index=True)
    email = models.EmailField()

    def __str__(self):
        return '{} - ({})'.format(
            self.name, 
            'Interviewer' if self.interviewer else 'Candidate'
        )


class TimeSlot(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    from_time = models.TimeField()
    to_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.person.name

