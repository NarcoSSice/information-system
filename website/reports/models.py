from django.db import models
from django.urls import reverse


class BasedClass(models.Model):
    name = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'reports_category'


class AllReports(BasedClass):
    class Meta:
        db_table = 'reports_all'

    @classmethod
    def get_data(cls):
        return cls.objects.all()


class One(BasedClass):
    class Meta:
        db_table = 'reports_1'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Монографії затверджені вченою радою університету'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'One'})


class Two(BasedClass):
    class Meta:
        db_table = 'reports_2'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Колективні монографії'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'Two'})


class Three(BasedClass):
    class Meta:
        db_table = 'reports_3'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Підручники'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'Three'})


class Four(BasedClass):
    class Meta:
        db_table = 'reports_4'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Навчальні посібники'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'Four'})


class Six(BasedClass):
    class Meta:
        db_table = 'reports_6'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Публікації зі студентами'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'Six'})


class Seven(BasedClass):
    class Meta:
        db_table = 'reports_7'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Інші види'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'Seven'})


class FiveOne(BasedClass):
    class Meta:
        db_table = 'reports_5.1'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Статті у фахових виданнях України'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveOne'})


class FiveTwoOne(BasedClass):
    class Meta:
        db_table = 'reports_5.2.1'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Публікації у закордонних видання(Опубліковані)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveTwoOne'})


class FiveTwoTwo(BasedClass):
    class Meta:
        db_table = 'reports_5.2.2'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Публікації у закордонних видання(Прийняті до друку)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveTwoTwo'})


class FiveThreeOne(BasedClass):
    class Meta:
        db_table = 'reports_5.3.1'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Наукові праці, що входять у МНБД(Опубліковані)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveThreeOne'})


class FiveThreeTwo(BasedClass):
    class Meta:
        db_table = 'reports_5.3.2'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Наукові праці, що входять у МНБД(Прийняті до друку)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveThreeTwo'})


class FiveFourOne(BasedClass):
    class Meta:
        db_table = 'reports_5.4.1'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Наукові праці, із іноземними співавторами(Опубліковані)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveFourOne'})


class FiveFourTwo(BasedClass):
    class Meta:
        db_table = 'reports_5.4.2'

    @classmethod
    def get_data(cls):
        return cls.objects.all()

    @classmethod
    def get_name(cls):
        return 'Наукові праці, із іноземними співавторами(Прийняті до друку)'

    def get_absolute_url(self):
        return reverse('table', kwargs={'name': 'FiveFourTwo'})
