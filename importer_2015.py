import django
from django.contrib.auth.models import User
from api.models import Speaker, Talk
import pandas as pd
django.setup()
df = pd.read_csv(
    '../evg-dashboard/2015/sessions.csv',
    sep='|',
    keep_default_na=False,
    parse_dates=[1]
)
del df[df.columns[0]]
df.rename(columns=lambda x: x.lower().strip().strip('\t'), inplace=True)
df['speaker'] = df['speaker'].map(lambda x: x.strip().strip('\t'))
df['name'] = df['name'].map(lambda x: x.strip().strip('\t'))
df['type'] = df['type'].map(lambda x: x.strip().strip('\t'))
df['location'] = df['location'].map(lambda x: x.strip().strip('\t'))
df['region'] = df['region'].map(lambda x: x.strip().strip('\t'))
df['campaign'] = df['campaign'].map(lambda x: str(x).strip().strip('\t'))


for row in df.to_dict('records'):
    username = row['speaker']
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'password': 'password'}
    )
    speaker = Speaker.objects.get(username=username)
    print speaker.username
    talk = Talk(
        date=row['date'],
        speaker=speaker,
        title=unicode(row['name'], 'utf-8', 'ignore'),
        size=row['size'],
        campaign_url=row['campaign'],
        region=row['region'],
        event_type=row['type'],
        location=row['location'],
        approved=True
    )
    talk.save()
