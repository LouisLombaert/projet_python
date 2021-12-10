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
