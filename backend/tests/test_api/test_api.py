from fastapi import testclient

from app import api

client = testclient.TestClient(api.app)


class TestAPI:
    def _build_url(self, prefix):
        return f'/api/v.1/machine/{prefix}'

    # URL_ODD = '/api/v.1/machine/odd'
    # URL_TRIPLE_BALANCING = '/api/v.1/machine/triple_balancing'
    # URL_FIBONACCI = '/api/v.1/machine/fibonacci'

    def test_odd_machine_with_valid_input(self):
        response = client.post(
            self._build_url('odd'), json={'tape': '1|2|3|4|5|6|7|8|9'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': '1|1|3|1|5|1|7|1|9|#',
            'message': 'Work done!',
            'output': 'Accepted',
        }

    def test_odd_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('odd'), json={'tape': '1|a|3|4'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': '1|a|3|4|#',
            'message': 'Hey Human, I just accept numbers.',
            'output': 'Rejected',
        }

    def test_triple_balancing_machine_with_valid_input(self):
        response = client.post(
            self._build_url('triple_balancing'), json={'tape': 'a|a|b|b|c|c'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': 'A|A|B|B|C|C|#',
            'message': 'Work done!',
            'output': 'Accepted',
        }

    def test_triple_balancing_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('triple_balancing'), json={'tape': 'a|b|b|c'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': 'A|B|b|C|#',
            'message': 'Ops... Is not a triple balancing.',
            'output': 'Rejected',
        }

    def test_fibonacci_machine_with_valid_input(self):
        response = client.post(
            self._build_url('fibonacci'), json={'tape': '1|2|3|5|8|13|21|34'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': '1|2|3|5|8|13|21|34|#',
            'message': 'Work done! Is fibonacci.',
            'output': 'Accepted',
        }

    def test_fibonacci_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('fibonacci'), json={'tape': '1|2|3|5|7'}
        )
        assert response.status_code == 200
        assert response.json() == {
            'tape': '1|2|3|5|7|#',
            'message': 'Is it not fibonacci',
            'output': 'Rejected',
        }
