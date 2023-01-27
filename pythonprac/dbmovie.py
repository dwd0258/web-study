from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.68jda7j.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# all_movie = list(db.movies.find({'star':'9.60'},{'_id':False}))
# for movie in all_movie:
#     print(movie['title'])


# db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})