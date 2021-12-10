class User:
    """class to create a user, this user can create a channel"""

    def __init__(self, pseudo, password, email, status):
        """create a new user based on a pseudo, password, email and status"""
        """
        PRE : pseudo, password, email and status are strings
        POST : a new User object is created
        """
        self.pseudo = pseudo
        self.password = password
        self.email = email
        self.status = status  # quel est le status par défaut ?

    def login(self, pseudo, password):
        """Groupe authentification ?"""
        pass

    def sign_up(self, pseudo, password, confirm_password, email):
        """Groupe authentification ?"""
        pass

    def create_new_channel(self, channel_name, channel_members=None):
        """create a new discution channel"""
        """
        PRE : channel_name is a string, channel.pseudo is a string, (optional) channel_members is a list of strings
        POST : a new Channel object is created, return this Channel
        """
        new_channel = Channel(channel_name, self.pseudo, channel_members)
        return new_channel
