class User(object):

    def __init__(self, _id, email, password):
        self.id = _id
        self.email = username
        self.password = password

    def __str__(self):
        return f"User({self.email},'*******',{self.password})"

#
# import dbconfig
#
# client=dbconfig.dbConnect()
#
# db=client['surveydb']
# col=db['users']
#
# user_list= { user.email:user  for user in col}
#
# def authenticate(email,password):
#     user = user_list.get(username,None)
#     if user and user.password == password:
#         return user
