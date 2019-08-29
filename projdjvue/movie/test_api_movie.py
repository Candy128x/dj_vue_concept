from rest_framework.test import APITestCase
from movie.models import Movie


class MovieApiTestCase(APITestCase):
    def setUp(self):
        Movie.objects.create(
            name='Raam Katha',
            launch_date='2019-03-01'
        )

    def test_get_method(self):
        url='http://localhost:8000/api/movie/'
        response=self.client.get(url)
        print('Select all set of record, Status code:', response.status_code)
        self.assertEqual(response.status_code, 200)
        qs=Movie.objects.filter(name='Raam Katha')
        self.assertEqual(qs.count(), 1)

    def test_post_metod(self):
        url='http://localhost:8000/api/movie/'
        data={
            'name': "Pawan",
            'launch_date': "2019-02-02"
        }
        response=self.client.post(url, data, format='json')
        print('Insert set of record, Status code:', response.status_code)
        self.assertEqual(response.status_code, 201)

    def test_post_metod_fail(self):
        url = 'http://localhost:8000/api/movie/'
        data = {
            'name': "Pawan"
        }
        response = self.client.post(url, data, format='json')
        print('Insert partial set of record, Status code:', response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_put_metod(self):
        getId = Movie.objects.get(name='Raam Katha').id
        url = 'http://localhost:8000/api/movie/'+str(getId)+'/'
        data = {
            'name': "Pawan",
            'launch_date': "2019-04-02"
        }
        response = self.client.put(url, data, format='json')
        print('Update set of record, Status code:', response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_delete_method(self):
        url = 'http://localhost:8000/api/movie/1/'
        response = self.client.delete(url)
        print('Delete set of record by ID, Status code:', response.status_code)
        self.assertEqual(response.status_code, 204)
