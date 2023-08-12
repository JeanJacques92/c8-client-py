class C8Instance(object):
    """_summary_
    """
    server: str
    user: str
    password:str
    token: str

    def __init__(self, server, user,password) -> None:

        self.server = server
        self.user = user
        self.password = password

    def connect(self):
        """_summary_

        Args:
            _self (_type_): _description_
        """
        print("connect")

    def c8_info(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.user , self.server  


def main():
    """_summary_
    """
    print ("C8 Instance creation")

if __name__ == "__main__":
    main()