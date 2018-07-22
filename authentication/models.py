from django.db import models

class BookUsers(models.Model):
    user_id = models.IntegerField(default=1)
    email = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    joined_datetime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Users.objects.all().aggregate(largest=models.Max('user_id'))['largest']

            if last_id is not None:
                self.user_id = last_id + 1

        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
