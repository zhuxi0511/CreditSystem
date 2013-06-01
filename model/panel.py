class PanelManager:
    def __init__(self, login, people, message, applys):
        login.panel_manager = self
        self.login = login
        people.panel_manager = self
        self.people = people
        message.panel_manager = self
        self.message = message
        applys.panel_manager = self
        self.applys = applys

    def switch_panel(self, fr, to):
        if (isinstance(fr, str)):
            fr = self.get_panel(fr)
        fr.forget()
        if (isinstance(to, str)):
            to = self.get_panel(to)
        to.refresh_mutilistbox()
        to.pack()

    def get_panel(self, s):
        if s == 'login':
            return self.login
        elif s == 'people':
            return self.people
        elif s == 'message':
            return self.message
        elif s == 'applys':
            return self.applys
