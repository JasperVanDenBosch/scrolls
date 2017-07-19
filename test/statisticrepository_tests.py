from test.ditestcase import DITestCase


class StatisticRepositoryTests(DITestCase):

    def test_update_sums_old_and_new(self):
        from scrolls.repositories.statistic import StatisticRepository
        self.filesys.readJson.return_value = {
            'app,mongodb': 20,
            'app,nginx': 10
        }
        stats = StatisticRepository(self.dependencies)
        stats.update('blub', {
            ('app', 'mongodb'): 5,
            ('app', 'other'): 30
        })
        saved = self.filesys.writeJson.call_args[0][1]
        self.assertEqual({
            'app,mongodb': 25,
            'app,nginx': 10,
            'app,other': 30
        }, saved)
        fpath = saved = self.filesys.writeJson.call_args[0][0]
        self.assertEqual(fpath, 'blub.json')
