from django.test import TestCase
from movie.models import Movie
import datetime

# Create your tests here.


# @pytest


class MovieTestCase(TestCase):
    def setUp(self):
        print('setUp activity.')
        Movie.objects.create(name='Mahabharat', launch_date='2018-01-11')
        Movie.objects.create(name='Mahabharat_2', launch_date='2019-01-11')

    def test_movie_info(self):
        print('Testing Movie information')
        qs=Movie.objects.all()
        self.assertEqual(qs.count(), 2)

        m1=Movie.objects.get(name='Mahabharat')
        m2=Movie.objects.get(name='Mahabharat_2')
        # print(m1.get_launch_date())
        self.assertEqual(m1.get_launch_date(), datetime.date(2018,1,11))
        self.assertEqual(m2.get_launch_date(), datetime.date(2019,1,11))