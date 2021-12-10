import exception
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
            raise exception.ParamNotFoundException(Exception)
        self.channel_members = [i for i in self.channel_members if i != member]  # permet de supprimer chaque élément
        # member de la liste (même si il revient plsrs fois), remove ne supprime que la premiere occurrence

    def mute_group(self):
        pass
    # delete_channel dans catégories ou dans channel ?

