import twitter

api = twitter.Api(consumer_key="BEuDtS9tVhzVvys2Rsx22r59I",
                  consumer_secret="rZjHG7MjXBESsWciO4KOb5rP9mYV7brHdJ6JTbMFGWiDdto5sU",
                  access_token_key="1313485732783230979-86rtYh2axsREPeZPpNSMh3NDkLODDz",
                  access_token_secret="5rdSV9HE4EbixO0CVuX1L8UukBt76CCSyrSRY2r6wok50")

# esempio online
x = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

# test
data = api.GetSearch(term="coronavirus",
                  count=5,
                  locale="it",
                  )

# tipo di ritorno: lista di twitter.models.status    
print(type(data))
for i in data:
    print(type(i))
    
print('\n')
    
# I want to access the list

# by interation
for status in data:
    print(status.text + '\n')

#using pop
status = data.pop()
print(status)

#indexing
status = data[0]
print(status)

# to access twitter.models.Status use the dot notation
print(status.created_at)
print(type(status.created_at))
print(type(status.hashtags))
print(type(status.id))
# other ways?
# Status is no iterable.

id = status.user.id
user = api.GetUser(user_id=id)
print(type(user))
print(user.name)