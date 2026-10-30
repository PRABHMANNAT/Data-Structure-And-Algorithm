from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
import json
import threading
import unittest
from workbench.server import Handler
from workbench.registry import projects


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def request(self,path,body=None,headers=None):
        connection=HTTPConnection('127.0.0.1',self.server.server_port,timeout=120)
        connection.request('POST' if body is not None else 'GET',path,body=body,headers=headers or {})
        response=connection.getresponse();result=response.status,response.read(),dict(response.getheaders())
        connection.close();return result

    def test_collection_and_assets(self):
        status,body,headers=self.request('/api/projects')
        self.assertEqual(status,200);self.assertEqual(len(json.loads(body)),len(projects()))
        self.assertEqual(headers['X-Content-Type-Options'],'nosniff')
        self.assertEqual(self.request('/')[0],200)
        self.assertEqual(self.request('/workbench/app.js')[0],200)

    def test_real_execution(self):
        status,body,_=self.request('/api/run/strings',json.dumps({'text':'aaaa','pattern':'aa'}))
        self.assertEqual(status,200);self.assertEqual(json.loads(body)['result']['positions'],[0,1,2])

    def test_every_bundled_scenario(self):
        for project in projects().values():
            for preset in project['presets']:
                with self.subTest(project=project['id'],scenario=preset['name']):
                    status,body,_=self.request('/api/run/'+project['id'],json.dumps(preset['input']))
                    self.assertEqual(status,200,body.decode())
                    self.assertIn('result',json.loads(body))

    def test_input_errors(self):
        self.assertEqual(self.request('/api/run/strings','[')[0],400)
        self.assertEqual(self.request('/api/run/strings','[]')[0],400)
        self.assertEqual(self.request('/api/run/missing','{}')[0],404)
        self.assertEqual(self.request('/api/run/strings','x'*65537)[0],413)

    def test_origin_checks(self):
        self.assertEqual(self.request('/api/run/strings','{}',{'Origin':'https://example.com'})[0],403)
        self.assertEqual(self.request('/api/run/strings','{}',{'Host':'attacker.test'})[0],403)

    def test_hidden_paths_and_directories(self):
        for path in ['/.git/config','/%2e%2e/README.md','/.workbench-cache/','/workbench/../.git/HEAD','/go_data_structures_lab/']:
            with self.subTest(path=path):self.assertEqual(self.request(path)[0],404)
