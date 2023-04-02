#A small code to calculate enagement of an user.

class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'User {self.name}: {self.engagement_metrics}'

def get_user_score(user):
    try:
        user.score = calculate_engagement(user.engagement_metrics)
    except KeyError:
        print("Wrong values added")
        raise
    else:
        if user.score > 500:
            send_notification(user)

def calculate_engagement(metric):
    return metric['clicks'] * 5 + metric['hits'] * 6
def send_notification(user):
    print(f'Notification has been sent to {user.name}')

User = User('Lipi', {'clicks':60, 'hits': 40})
get_user_score(User)
