from channel import Channel
from exception import ParamNotFoundException


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
