import datetime
import json

class ScheduleManager:
    def __init__(self, file_path='schedule_data.json'):
        self.file_path = file_path
        self.schedule = self.load_schedule()

    def load_schedule(self):
        try:
            with open(self.file_path, 'r') as file:
                schedule_data = json.load(file)
                return schedule_data
        except FileNotFoundError:
            return {}

    def save_schedule(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.schedule, file, indent=2)

    def get_date_key(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def add_activity(self, activity):
        date_key = self.get_date_key()
        if date_key not in self.schedule:
            self.schedule[date_key] = {'yesterday': '', 'today': ''}

        self.schedule[date_key]['today'] = activity
        self.save_schedule()

    def get_yesterday_activity(self):
        date_key = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        return self.schedule.get(date_key, {}).get('today', '')

    def get_today_activity(self):
        date_key = self.get_date_key()
        return self.schedule.get(date_key, {}).get('today', '')

if __name__ == "__main__":
    schedule_manager = ScheduleManager()

    # Get yesterday's activity
    yesterday_activity = schedule_manager.get_yesterday_activity()
    print(f"Yesterday's activity: {yesterday_activity}")

    # Get today's activity
    today_activity = schedule_manager.get_today_activity()
    print(f"Today's planned activity: {today_activity}")

    # Add a new activity for today
    new_activity = input("Enter a new activity for today: ")
    schedule_manager.add_activity(new_activity)

    # Display updated today's activity
    today_activity = schedule_manager.get_today_activity()
    print(f"Updated today's planned activity: {today_activity}")
