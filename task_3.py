data = {
    1: {
        'inner_field': {
            'inner_inner_field': {
                'user_status': 'Basic',
                'some_info': 'some_info_str',
            },
            'some_another_inner_field': 'some_str',
        },
        'some_inner_field': [1, 2, 3],
    },
    2: {
        'inner_field': {
            'inner_inner_field': {
                'user_status': 'Premium',
                'some_info': 'some_info_str',
            },
            'some_another_inner_field': 'some_str',
        },
        'some_inner_field': [4, 5, 6],
    },
}


class Profile:
    def __init__(self, user_id, data):
        self.user_id = user_id
        self.data = data
        self._cache = {}

    def status(self):
        if self.user_id in self._cache:
            return self._cache[self.user_id]
        else:
            status = self.data[self.user_id]['inner_field']['inner_inner_field']['user_status']
            self._cache[self.user_id] = status
            return status


profile = Profile(2, data)
print(profile.status())

profile1 = Profile(1, data)
print(profile1.status())























































