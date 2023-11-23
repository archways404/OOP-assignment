class RentalSystem:
  def __init__(self):
    self.system_log = []

  def log_activity(self, activity):
    self.system_log.append(activity)
    print(f"--> [Activity Logged]: {activity}")

  def display_info(self):
    print("[Rental System Information]")
