from fastapi import testclient

from app import api

client = testclient.TestClient(api.app)


class TestAPI:
    def _build_url(self, sufix):
        return f'/api/v.1/machine/{sufix}'

    def test_odd_machine_with_valid_input(self):
        response = client.post(
            self._build_url('odd'), json={'tape': '1|2|3|4|5|6|7|8|9'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': '1|1|3|1|5|1|7|1|9|#',
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,1,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '4,1,R'},
                {'q4->q5': '5,5,R'},
                {'q5->q6': '6,1,R'},
                {'q6->q7': '7,7,R'},
                {'q7->q8': '8,1,R'},
                {'q8->q9': '9,9,R'},
                {'q9->qf': '#,#,R'},
            ],
        }
        assert response.json() == expected_response

    def test_odd_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('odd'), json={'tape': '1|a|3|4'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': '1|a|3|4|#',
            'message': 'Hey Human, I just accept numbers.',
            'output': 'Rejected',
            'transitions': [{'q0->q1': '1,1,R'}, {'fail': '*,*,*'}],
        }
        assert response.json() == expected_response

    def test_triple_balancing_machine_with_valid_input(self):
        response = client.post(
            self._build_url('triple_balancing'), json={'tape': 'a|a|b|b|c|c'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': 'A|A|B|B|C|C|#',
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': 'a,A,R'},
                {'q1->q1': 'a,a,R'},
                {'q1->q2': 'b,B,R'},
                {'q2->q2': 'b,b,R'},
                {'q2->q3': 'c,C,L'},
                {'q3->q3': 'b,b,L'},
                {'q3->q4': 'B,B,L'},
                {'q4->q4': 'a,a,L'},
                {'q4->q0': 'A,A,R'},
                {'q0->q1': 'a,A,R'},
                {'q1->q1': 'B,B,R'},
                {'q1->q2': 'b,B,R'},
                {'q2->q2': 'C,C,R'},
                {'q2->q3': 'c,C,L'},
                {'q3->q3': 'C,C,L'},
                {'q3->q4': 'B,B,L'},
                {'q4->q4': 'B,B,L'},
                {'q4->q0': 'A,A,R'},
                {'q0->q5': 'B,B,R'},
                {'q5->q5': 'B,B,R'},
                {'q5->q6': 'C,C,R'},
                {'q6->q6': 'C,C,R'},
                {'q6->qf': '#,#,R'},
            ],
        }
        assert response.json() == expected_response

    def test_triple_balancing_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('triple_balancing'), json={'tape': 'a|b|b|c'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': 'A|B|b|C|#',
            'message': 'Ops... Is not a triple balancing.',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': 'a,A,R'},
                {'q1->q2': 'b,B,R'},
                {'q2->q2': 'b,b,R'},
                {'q2->q3': 'c,C,L'},
                {'q3->q3': 'b,b,L'},
                {'q3->q4': 'B,B,L'},
                {'q4->q0': 'A,A,R'},
                {'q0->q5': 'B,B,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert response.json() == expected_response

    def test_fibonacci_machine_with_valid_input(self):
        response = client.post(
            self._build_url('fibonacci'), json={'tape': '1|2|3|5|8|13|21|34'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': '1|2|3|5|8|13|21|34|#',
            'message': 'Work done! Is fibonacci.',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '5,5,R'},
                {'q4->q5': '8,8,R'},
                {'q5->q6': '13,13,R'},
                {'q6->q7': '21,21,R'},
                {'q7->q8': '34,34,R'},
                {'q8->qf': '#,#,R'},
            ],
        }
        assert response.json() == expected_response

    def test_fibonacci_machine_with_invalid_input(self):
        response = client.post(
            self._build_url('fibonacci'), json={'tape': '1|2|3|5|7'}
        )
        assert response.status_code == 200

        expected_response = {
            'tape': '1|2|3|5|7|#',
            'message': 'Is it not fibonacci',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '5,5,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert response.json() == expected_response
