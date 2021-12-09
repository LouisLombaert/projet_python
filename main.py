class ParamNotFoundException(Exception):
    pass


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


class Message:
    """class to create a new message, this can send, receive and edit messages"""

    def __init__(self, message_author, message_type, is_edited=False, tagged_user=None):
        """create a new Message based on an author, a type, an edition, and a tagged user"""
        """
        PRE : message_author, message_type and tagged_user are strings, is_edited is a boolean
        POST : a new Message object is created
        """
        self.message_author = message_author
        self.message_type = message_type
        self.is_edited = is_edited
        self.tagged_user = tagged_user

    def send_message(self):
        """send a message"""  # ici le code du mvp ( à mon avis côté client)
        """
        PRE :
        POST :
        """
        pass

    def receive_message(self):
        """receive a message if a message was sent to the target user"""  # ici le code du mvp (à mon avis côté serveur)
        """
        PRE : 
        POST :
        """
        pass

    def edit_message(self):
        """edit the message"""
        """
        PRE :
        POST :
        """
        # comment éditer ( changer le contenu ?)
        pass


class Channel:
    """class to create a new channel, it can add and remove members to this channel"""

    def __init__(self, channel_name, channel_admin, channel_members=None, chat_history=None):
        """create a new channel based on a name, an administrator, some members and a chat history"""
        """
        PRE : channel_name and channel_admin are strings, channel_members and chat_history are lists of strings
        POST : a new Channel object is created
        """
        if channel_members is None:
            channel_members = []
        if chat_history is None:
            chat_history = []
        self.channel_name = channel_name
        self.channel_admin = channel_admin
        self.channel_members = channel_members.append(self.channel_admin)  # pour moi channel_members serait une
        # liste de string (comme ça on peut ajouter et supprimer des membres facilement
        self.chat_history = chat_history  # même chose que pour channel_members

    def add_member(self, member):
        """add a new member to the channel"""
        """
        PRE : member is a string
        POST : member is added to the list of members of the channel
        """
        self.channel_members.append(member)

    def remove_member(self, member):
        """remove a member from the channel, it remove all the members that have the pseudo member"""
        """
        PRE : member is a string that is in the list channel_members
        POST : all the element 'member' of the list channel_members are removed
        RAISE : paramNotFoundException if member is not in channel_members
        """
        if member not in self.channel_members:
            raise ParamNotFoundException(Exception)
        self.channel_members = [i for i in self.channel_members if i != member]  # permet de supprimer chaque élément
        # member de la liste (même si il revient plsrs fois), remove ne supprime que la premiere occurrence

    def mute_group(self):
        pass
    # delete_channel dans catégories ou dans channel ?


class Categories:
    """class to create a new Category, it can add and remove members to this channel"""

    def __init__(self, category_name, category_channels=None):
        """create a new category based on a name and channels (that are contained in the category)"""
        """
        PRE : category_name is a string, category_channels is a list of strings
        POST : a new Category object is created
        """
        if category_channels is None:
            category_channels = []
        self.category_name = category_name
        self.category_channels = category_channels  # pareil que pour members dans channel

    def add_channel(self, channel):
        """add a new channel to the category"""
        """
        PRE : channel is a string
        POST :the channel is added to the list category_channels
        """
        self.category_channels.append(channel)

    def delete_channel(self, channel):
        """remove a channel from the category"""
        """
        PRE : channel is a string that is in the list category_channels
        POST : all the element 'channel' of the list category_channels are removed
        RAISE : paramNOtFoundException if channel is not in category_channels
        """
        if channel not in self.category_channels:
            raise ParamNotFoundException(Exception)
        self.category_channels = [i for i in self.category_channels if i != channel]

    def delete_all_channel(self):
        """delete all the channel of the category"""
        """
        PRE : -
        POST : all the element of the list category_channel are removed
        """
        self.category_channels = []

    def delete_category(self):
        pass
