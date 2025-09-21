task = input('Enter your task:')
priority = input('Priority (high/medium/low):')
time_bound: input('Is it time-bound?(yes/no):')

Match priority:
case 'high': 
    message = 'task, is a high priority task'
    label = 'Reminder'
case "medium":
    message = 'task, is a medium priority task'
    label = 'Reminder'
case "low":
    message = 'task, is a low priority task'
    label = 'Reminder'
case _:
    message = 'task, has an unspecified priority'

if time_bound == 'yes':
    message += 'that requires immediate attention today!'
else:
    message += 'Consider completing it when you have free time.'


print(label:, message)
