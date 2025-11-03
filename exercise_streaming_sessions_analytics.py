# Day 1
sessions_day1 = [
    ("u01", "Aurora", 42, "2025-10-28", "mobile"),
    ("u02", "Nebula", 15, "2025-10-28", "tv"),
    ("u03", "Aurora", 57, "2025-10-28", "desktop"),
    ("u02", "Orion", 33, "2025-10-28", "mobile"),
    ("u04", "Aurora", 12, "2025-10-28", "tablet"),
    ("u05", "Nebula", 48, "2025-10-28", "tv"),
    ("u03", "Orion", 21, "2025-10-28", "desktop"),
    ("u06", "Quasar", 66, "2025-10-28", "mobile"),
    ("u02", "Aurora", 9,  "2025-10-28", "tv"),
    ("u07", "Quasar", 18, "2025-10-28", "tv"),
]

# Day 2
sessions_day2 = [
    ("u02", "Aurora", 25, "2025-10-29", "mobile"),
    ("u08", "Nebula", 51, "2025-10-29", "desktop"),
    ("u01", "Quasar", 39, "2025-10-29", "tv"),
    ("u09", "Orion", 10, "2025-10-29", "mobile"),
    ("u03", "Aurora", 44, "2025-10-29", "desktop"),
    ("u10", "Quasar", 73, "2025-10-29", "tv"),
    ("u05", "Nebula", 11, "2025-10-29", "mobile"),
    ("u06", "Quasar", 30, "2025-10-29", "desktop"),
    ("u11", "Aurora", 22, "2025-10-29", "tablet"),
    ("u02", "Orion", 27, "2025-10-29", "tv"),
]

# --------------item 1


def get_data(sessions, value):
    data_day = set()
    for data in sessions:
        data_day.add(data[value])
    return data_day


users_day1 = get_data(sessions_day1, 0)
users_day2 = get_data(sessions_day2, 0)
titles_day1 = get_data(sessions_day1, 1)
titles_day2 = get_data(sessions_day2, 1)

print(titles_day1, titles_day2)

users_same_days = users_day1 & users_day2
print(f'Users on both days: {users_same_days}')
new_users_day2 = users_day2 - users_day1
print(f'New users on Day 2: {new_users_day2}')
all_titles = titles_day1 | titles_day2
print(f'Total catalog of titles viewed on both days: {all_titles}')
titles_view_day1 = titles_day1 - titles_day2
print(f'Titles viewed only on Day 1: {titles_view_day1}')

# ----------item2
# formato por acumulación, mas eficiente

title_minutes_day1 = {}

for session in sessions_day1:
    title = session[1]
    minutes = session[2]
    title_minutes_day1[title] = title_minutes_day1.get(title, 0) + minutes

print(title_minutes_day1)

# formato por compresion, mas recursos
title_minutes_day2 = {title: sum(session[2] for session in sessions_day1 if session[1] == title)
                      for title in set(session[1] for session in sessions_day1)}
print(title_minutes_day2)


# --------------item3


def get_user_stats(sessions):
    user_stats = {}
    for session in sessions:
        user_id = session[0]
        minutes = session[2]
        if user_id not in user_stats:
            user_stats[user_id] = {
                'total_minutes': minutes, "session_count": 1}
        else:
            user_stats[user_id]['total_minutes'] += minutes
            user_stats[user_id]['session_count'] += 1
    return user_stats


users_stats_day1 = get_user_stats(sessions_day1)
users_stats_day2 = get_user_stats(sessions_day2)


def get_top_user(users_stats):
    return max(users_stats.items(), key=lambda item: item[1]['total_minutes'])
# max() ya recorre toda la lista, no hace falta recorrerla con un for


top_user_day1 = get_top_user(users_stats_day1)
top_user_day2 = get_top_user(users_stats_day2)
print(
    f"Top user Day 1: {top_user_day1[0]} with {top_user_day1[1]['total_minutes']} minutes")
print(
    f"Top user Day 2: {top_user_day2[0]} with {top_user_day2[1]['total_minutes']} minutes")

avg_minutes = {}

for user_id, stats in users_stats_day2.items():
    avg_minutes[user_id] = {
        'average': stats['total_minutes'] / stats['session_count']}

print(avg_minutes)


# ----------------------item 4

devices_day1 = get_data(sessions_day1, 4)
devices_day2 = get_data(sessions_day2, 4)

print(devices_day1 | devices_day2)

device_count_day2 = {}

for data in sessions_day2:
    device = data[4]
    if device not in device_count_day2:
        device_count_day2[device] = {'device_count': 1}
    else:
        device_count_day2[device]['device_count'] += 1

print(f'[Device count day 2: {device_count_day2}]')
top_device = max(device_count_day2.items(),
                 key=lambda item: item[1]['device_count'])
print(f'Device more use day 2: {top_device}')


# ----------------- item 5

count_sessions_day1 = len(sessions_day1)

count = 0
for data_session in sessions_day2:
    count += 1
count_sessions_day2 = count


unique_users_day1 = set(users_day1)
unique_users_day2 = set(users_day2)
unique_users_total = len(unique_users_day1 | unique_users_day2)

unique_titles_day1 = set(titles_day1)
unique_titles_day2 = set(titles_day2)
unique_titles_total = len(unique_titles_day1 | unique_titles_day2)

summary = (
    ('day1_sessions', count_sessions_day1),
    ('day2_sessions', count_sessions_day2),
    ('unique_users_total', unique_users_total),
    ('unique_titles_total', unique_titles_total)
)
print(summary)
